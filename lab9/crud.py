# crud.py
from db import SessionLocal, User, Post

def create_users():
    db = SessionLocal()
    users = [
        User(username="alice", email="alice@example.com", password="pass123"),
        User(username="bob", email="bob@example.com", password="bobpass"),
    ]
    db.add_all(users)
    db.commit()
    db.close()

def create_posts():
    db = SessionLocal()
    alice = db.query(User).filter_by(username="alice").first()
    bob = db.query(User).filter_by(username="bob").first()

    posts = [
        Post(title="Alice's First Post", content="Hello world!", user_id=alice.id),
        Post(title="Bob's Post", content="Hi, I'm Bob", user_id=bob.id),
    ]
    db.add_all(posts)
    db.commit()
    db.close()

def get_all_users():
    db = SessionLocal()
    users = db.query(User).all()
    for user in users:
        print(user.id, user.username, user.email)
    db.close()

def get_all_posts_with_users():
    db = SessionLocal()
    posts = db.query(Post).all()
    for post in posts:
        print(post.title, "-", post.author.username)
    db.close()

def get_posts_by_user(username):
    db = SessionLocal()
    user = db.query(User).filter_by(username=username).first()
    if user:
        for post in user.posts:
            print(post.title)
    db.close()

def update_user_email(user_id, new_email):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    if user:
        user.email = new_email
        db.commit()
    db.close()

def update_post_content(post_id, new_content):
    db = SessionLocal()
    post = db.query(Post).get(post_id)
    if post:
        post.content = new_content
        db.commit()
    db.close()

def delete_post(post_id):
    db = SessionLocal()
    post = db.query(Post).get(post_id)
    if post:
        db.delete(post)
        db.commit()
    db.close()

def delete_user_and_posts(user_id):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    if user:
        db.delete(user)
        db.commit()
    db.close()
