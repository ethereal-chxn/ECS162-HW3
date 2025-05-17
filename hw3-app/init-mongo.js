db = db.getSiblingDB('mydatabase');  // Switch to the 'mydatabase' database

// Check if the users collection exists, and if not, insert the static user
db.createCollection('users');
db.users.find().count() === 0 && db.users.insertOne({
    email: 'alice@example.com',
    hash: '$2a$10$CwTycUXWue0Thq9StjUM0uJ8DPLKXt1FYlwYpQW2G3cAwjKoh2WZK',  // hashed password
    username: 'alice',
    userID: '123'
});

// Create comments collection
db.createCollection('comments')

// Insert comments
db.comments.insertOne({
  id: '0',
  author: '',
  responseTo: '',
  body: '' //content of comment
})

//Insert many commments
db.comments.insertMany([{}, {}])

//accepts a query object
//could use to fetch pre-existing comments
//debugging, check if things are updated
db.comments.find({})
//if left empty it will return the first document it finds. selects only one doc
db.comments.findOne()

//update comment to hold redacted text!!
db.comments.updateOne(
  {
    /*query selector*/
  },
  {
    $set: {
      /* query & update */
    }
  }
) //set to a particular value

//prolly wont need this
db.comments.updateOne(
  {
    /*query selector*/
  },
  {
    $inc: {
      /* query & update */
    }
  }
) //incremenet a number

// logical operators for queries are $and, $or, $nor, $not
// evaluating docs with $regex (eval field vals), $text (test search), $where (uses JS expression to match docs)

// update fields with $currentDate, $inc, $rename, $set, $unset
// update arrays with $addToSet, $pop, $pull, $push

// Create articles collection
db.createCollection('articles')
