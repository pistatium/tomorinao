# coding: utf-8

from flask import Flask, request, render_template, redirect

from oauth import oauth

from setting import *


app = Flask(__name__)
app.debug = True

consumer_key = "LKlkj83kaio2fjiudjd9...etc"
consumer_secret = "58kdujslkfojkjsjsdk...etc"
callback_url = "http://www.myurl.com/callback/twitter"
twitter_client = oauth.TwitterClient(CONSUMER_KEY, CONSUMER_SECRET, CALLBACK_URL)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/twitter_login')
def twitter_login():
    return redirect(twitter_client.get_authorization_url())

@app.route('/twitter_callback')
def twitter_callback():
    auth_token = request.args.get("oauth_token", '')
    auth_verifier = request.args.get("oauth_verifier", '')
    user_info = twitter_client.get_user_info(auth_token, auth_verifier=auth_verifier)
    import json
    return json.dumps(user_info)


