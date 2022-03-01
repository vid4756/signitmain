from flask import render_template, request, Blueprint,url_for
from flaskblog.models import Post
# from flaskblog.main.random_img import ri
import os
import random

main = Blueprint('main', __name__)
@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html',posts=posts)
@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html',title='home')


# imgs = os.listdir('static/img')
# imgs = ['img/' + file for file in imgs]
# @main.route('/index')
# def index(imgrand = random.sample(imgs,k=5)):
   
    
#     return render_template('home.html', imgrand=imgrand)








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
# @main.route("/")
# def index():
#  random_bird = BirdDetails.query.order_by(func.random()).first()
#  return render_template('main/index.html', bird = random_bird)
# from birdnet.models import User, Thread, Reply, BirdDetails, db
