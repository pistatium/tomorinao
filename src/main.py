# coding: utf-8

from flask import Flask, request, render_template, redirect, url_for
from flask.ext.login import LoginManager, login_user, current_user

from oauth import oauth

from models.login_user import LoginUser
from setting import *


app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY
app.debug = True
login_manager = LoginManager(app)

consumer_key = "LKlkj83kaio2fjiudjd9...etc"
consumer_secret = "58kdujslkfojkjsjsdk...etc"
callback_url = "http://www.myurl.com/callback/twitter"
twitter_client = oauth.TwitterClient(CONSUMER_KEY, CONSUMER_SECRET, CALLBACK_URL)

@login_manager.user_loader
def load_user(unique_id):
        return LoginUser.get_by_id(unique_id)

@app.route('/')
def index(): 
    return render_template("index.html", user=current_user)

@app.route('/twitter_login')
def twitter_login():
    return redirect(twitter_client.get_authorization_url())

@app.route('/twitter_callback')
def twitter_callback():
    auth_token = request.args.get("oauth_token", '')
    auth_verifier = request.args.get("oauth_verifier", '')
    user_info = twitter_client.get_user_info(auth_token, auth_verifier=auth_verifier)
    user = LoginUser.load(user_info)
    user.put()
    login_user(user)
    return redirect(url_for("index"))


