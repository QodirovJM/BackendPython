from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import joinedload
from db import SessionLocal, User, Post

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    db = SessionLocal()
    users = db.query(User).all()
    posts = db.query(Post).options(joinedload(Post.author)).all()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request, "users": users, "posts": posts})

@app.post("/users/create")
def create_user(username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    db = SessionLocal()
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    db.close()
    return RedirectResponse("/", status_code=303)

@app.post("/posts/create")
def create_post(title: str = Form(...), content: str = Form(...), user_id: int = Form(...)):
    db = SessionLocal()
    post = Post(title=title, content=content, user_id=user_id)
    db.add(post)
    db.commit()
    db.close()
    return RedirectResponse("/", status_code=303)

@app.get("/users/edit/{user_id}", response_class=HTMLResponse)
def edit_user_form(request: Request, user_id: int):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    db.close()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("edit_user.html", {"request": request, "user": user})

@app.put("/users/edit/{user_id}")
def update_user(user_id: int, username: str = Form(...), email: str = Form(...)):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    if user:
        user.username = username
        user.email = email
        db.commit()
    db.close()
    return RedirectResponse("/", status_code=303)

@app.delete("/users/delete/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).get(user_id)
    if user:
        db.delete(user)  # автоматически удалятся и его посты (если настроен cascade)
        db.commit()
    db.close()
    return RedirectResponse("/", status_code=303)

@app.get("/posts/edit/{post_id}", response_class=HTMLResponse)
def edit_post_form(request: Request, post_id: int):
    db = SessionLocal()
    post = db.query(Post).get(post_id)
    users = db.query(User).all()
    db.close()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return templates.TemplateResponse("edit_post.html", {"request": request, "post": post, "users": users})

@app.put("/posts/edit/{post_id}")
def update_post(post_id: int, title: str = Form(...), content: str = Form(...), user_id: int = Form(...)):
    db = SessionLocal()
    post = db.query(Post).get(post_id)
    if post:
        post.title = title
        post.content = content
        post.user_id = user_id
        db.commit()
    db.close()
    return RedirectResponse("/", status_code=303)

@app.delete("/posts/delete/{post_id}")
def delete_post(post_id: int):
    db = SessionLocal()
    post = db.query(Post).get(post_id)
    if post:
        db.delete(post)
        db.commit()
    db.close()
    return RedirectResponse("/", status_code=303)
