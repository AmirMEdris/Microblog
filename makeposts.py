from app import db
from app.models import User, Post

# Create some users
user1 = User(username='user1', email='user1@example.com')
user1.set_password('password')
user2 = User(username='user2', email='user2@example.com')
user2.set_password('password')

# Add users to the database
db.session.add(user1)
db.session.add(user2)
db.session.commit()

# Create some posts
post1 = Post(body='my first post!', user_id=user1.id, language='EN')
post2 = Post(body='my second post!', user_id=user2.id, language='EN')

# Add posts to the database
db.session.add(post1)
db.session.add(post2)
db.session.commit()