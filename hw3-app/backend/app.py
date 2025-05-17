from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from pymongo import MongoClient
import os

app = Flask(__name__)
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
db = mongo.get_default_database()

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

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

#Get all the comments in the database
@app.route("/api/commments", methods=['GET'])
def get_comments():
    return jsonify(db["comments"])

# Adds a comment to database 
@app.route("/api/comments", methods=['POST'])
def post_comment():
    pass

# Edits comment to say it is deleted
@app.route("/api/comments/<id>", methods=['DELETE'])
def delete_comment():
    pass

# Adds reply to comment (PUT)
@app.route("/api/comments/<id>", methods=['PUT'])
def put_reply_in_comment():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
