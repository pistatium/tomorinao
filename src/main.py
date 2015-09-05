# coding: utf-8

from flask import Flask, request, make_response, render_template, redirect, url_for
from flask.ext.login import LoginManager, login_user, current_user, login_required
from google.appengine.api import memcache

from oauth import oauth
import logging

from models.login_user import LoginUser
from models.twitter import Twitter
from setting import *


app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY
login_manager = LoginManager(app)
logger = logging.getLogger(__name__)

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

@app.route('/api/timeline')
@login_required
def api_timeline():
    since_id = request.args.get("since_id", '')
    max_id = request.args.get("max_id", '')
    tweets = _get_tweets(twitter_client, current_user, since_id, max_id) 
    resp = make_response(
        '''{{ "tweets":{} }}'''.format(tweets),
    ) 
    resp.headers["Content-type"] = "application/json";
    return resp


def _get_tweets(twitter_client, current_user, since_id, max_id):
    key = "tweets_{}_{}_{}".format(current_user.token, since_id, max_id)
    value = memcache.get(key)
    if value:
        return value
    tw = Twitter(twitter_client, current_user.token, current_user.secret)
    data = tw.get_timeline(since_id, max_id)
    if data.status_code != 200:
        logger.error(data.status_code)
        return {}
    value = data.content
    memcache.set(key, value, time=30) 
    return value

