from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)
@main.route("/forum")
def forum():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('forum.html',posts=posts)
@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html',title='home')
# @main.route("/contact us")
# def contactus():
#     return render_template('contactus.html',title='contactus')
# @main.route("/bonus")
# @login_required
# def bonus():
    
#     return render_template('bonus.html',title='bonus')
# @main.route("/interpreter")
# def interpreter():
#     return render_template('interpreter.html',title='interpreter')
