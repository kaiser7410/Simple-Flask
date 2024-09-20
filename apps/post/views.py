from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import Post
from config.setting import db
from flask_login import login_required, current_user
from .forms import PostForm

post_bp = Blueprint("post", __name__)

@post_bp.route("/")
def index():
    posts = Post.query.order_by(-Post.id).all() # 相等於 posts = models.Post.query.order_by(models.Post.id.desc()).all()
    return render_template("posts/index.html", posts=posts)



@post_bp.route("/new")
@login_required
def new():
    form = PostForm()
    return render_template("posts/news.html", form=form)

@post_bp.route("/create", methods=["POST"])
@login_required
def create():
    form = PostForm(request.form)
    
    if form.validate():
        # 從前端獲取資料
        title = form.title.data
        content = form.content.data

        post = Post(title=title, content=content)

        post.author = current_user
        
        # 寫入 DB
        db.session.add(post)
        db.session.commit()
        
        # 設定快閃訊息
        flash("新增文章成功!")

        # 表單按下送出後自動跳回首頁
        return redirect(url_for("post.index"))
    return render_template("posts/news.html", form=form)

@post_bp.route("/<int:id>")
def show(id):
    post = Post.query.get_or_404(id)
    return render_template("posts/show.html", post=post)


@post_bp.route("/<int:id>/edit")
@login_required
def edit(id):
    post = Post.query.filter_by(id=id, author=current_user).first_or_404()
    form = PostForm(obj=post)
    return render_template("posts/edit.html", post=post, form=form)

@post_bp.route("/<int:id>/update", methods=["POST"])
@login_required
def update(id):
    post = Post.query.filter_by(id=id, author=current_user).first_or_404()
    form = PostForm(request.form, obj=post)

    if form.validate():
        form.populate_obj(post)
        
        # 寫入 DB
        
        db.session.commit()
        
        # 快閃訊息
        flash("文章更新成功")
        
        return redirect(url_for("post.show", id=id))
    return render_template("/posts/edit.html", post=post, form=form)

@post_bp.route("/<int:id>/deltet", methods=["POST"])
@login_required
def delete(id):
    post = Post.query.filter_by(id=id, author=current_user).first_or_404()

    db.session.delete(post)
    db.session.commit()

    flash("文章已刪除")

    return redirect(url_for("post.index"))