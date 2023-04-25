from app import create_app, db, cli
from app.models import User, Post, Message, Notification, Task



app = create_app()
cli.register(app)

def clean_up_database():
    Post.query.delete()
    User.query.delete()
    db.session.commit()
    print("Database cleaned up.")

def add_sample_posts(num_posts):
    user1 = User(username='user1', email='user1@example.com')
    db.session.add(user1)
    db.session.commit()

    posts = [Post(body=f'Hello, this is user1 post {i + 1}.', author=user1) for i in range(num_posts)]
    db.session.add_all(posts)
    db.session.commit()
    print(f"{num_posts} sample posts added for user1.")


def print_database_content():
    print("Printing database content:")
    users = User.query.all()
    for user in users:
        print(f"User: {user.username}, Email: {user.email}")
        posts = Post.query.filter_by(user_id=user.id).all()
        for post in posts:
            print(f"\tPost: {post.body}, Timestamp: {post.timestamp}")

if __name__ == "__main__":
    with app.app_context():
        clean_up_database()
        add_sample_posts(10)
        print_database_content()
    app.run()
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification, 'Task': Task}
