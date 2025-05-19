from flask import Flask, redirect, url_for, session, jsonify, request
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)



oauth = OAuth(app)

nonce = generate_token()



oauth.register(
    name='flask_app',
    client_id=os.getenv('OIDC_CLIENT_ID'),
    client_secret=os.getenv('OIDC_CLIENT_SECRET'),
    #server_metadata_url='http://dex:5556/.well-known/openid-configuration',
    authorization_endpoint="http://localhost:5556/auth",
    token_endpoint="http://dex:5556/token",
    jwks_uri="http://dex:5556/keys",
    userinfo_endpoint="http://dex:5556/userinfo",
    device_authorization_endpoint="http://dex:5556/device/code",
    client_kwargs={'scope': 'openid email profile'}
)

mongo_uri = os.getenv("MONGO_URI")
mongo = MongoClient(mongo_uri)
db = mongo["mydatabase"]
comments_collection = db["comments"]

@app.route('/')
def home():
    user = session.get('user')
    if user:
        return f"<h2>Logged in as {user['email']}</h2><a href='/logout'>Logout</a>"
    return '<a href="/login">Login with Dex</a>'

@app.route('/api/key')
def get_key():
    return jsonify({'apiKey': os.getenv('NYT_API_KEY')})

@app.route('/login')
def login():
    session['nonce'] = nonce
    redirect_uri = 'http://localhost:8000/authorize'
    return oauth.flask_app.authorize_redirect(redirect_uri, nonce=nonce)

@app.route('/authorize')
def authorize():
    token = oauth.flask_app.authorize_access_token()
    nonce = session.get('nonce')

    user_info = oauth.flask_app.parse_id_token(token, nonce=nonce)  # or use .get('userinfo').json()
    session['user'] = user_info
    # From dicussion
    return redirect(f"http://localhost:5173/login?user={user_info['email']}")

@app.route('/get_user')
def get_user():
    return jsonify({'userInfo': session.get('user')})

@app.route('/logout')
def logout():
    session.clear()
    return redirect('http://localhost:5173')

# Get all the comments in the database
@app.route("/api/comments", methods=['GET'])
def get_comments():
    comments = list(comments_collection.find())
    for comment in comments:
        comment['_id'] = str(comment['_id'])
    return jsonify(comments)

# Get all comments under specified article
@app.route("/api/comments/article/<int:article_id>", methods=['GET'])
def get_comment_article(article_id):
    comments_in_article = list(comments_collection.find({"articleId": article_id}))
    # comments_in_article = list(comments_collection.find())
    # print(comments_in_article)
    for comment in comments_in_article:
        comment['_id'] = str(comment['_id'])
    return jsonify({'comments': comments_in_article})

# Adds a comment to database 
@app.route("/api/comments", methods=['POST'])
def post_comment():
    commentData = request.get_json()
    result = comments_collection.insert_one(commentData)
    return jsonify({"inserted_id": str(result.inserted_id)})

# Edits comment to say it is deleted
@app.route("/api/comments/<comment_id>", methods=['DELETE'])
def delete_comment(comment_id):
    query = {'_id': ObjectId(comment_id)}
    result = comments_collection.update_one(query, {"$set": {'commentBody': "COMMENT REMOVED BY MODERATOR!"}})
    modifiedComment = comments_collection.find_one({"_id": ObjectId(comment_id)})
    return jsonify({"modifiedComment": list(modifiedComment)})

# Adds reply to comment (PUT)
@app.route("/api/comments/<id>", methods=['PUT'])
def put_reply_in_comment():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
