from __future__ import print_function # In python 2.7
import json
from flask import Flask, request
from flask_cors import CORS
from flask_ngrok import run_with_ngrok

from classes.RedditApi import RedditApi
from classes.post import Post
from controller.get_post_controller import PostController
from text_to_speak.tik_tok_text_to_speak import text_to_speak
import sys

class RA():
    request_amount = 0

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
run_with_ngrok(app)

@app.route('/get_post_data', methods=['GET'])
def get_post_speach_data():
    subreddit = request.args.get('subreddit')
    
    if RA.request_amount > 10:
        print("[ERROR] " + str(RA.request_amount), file=sys.stderr)
        time.sleep(20)
        RA.request_amount = 0
    RA.request_amount += 1
    
    print("[COUNT] " + str(RA.request_amount), file=sys.stderr)
    response = PostController.get_single_post(subreddit)

    return  response

# @app.route('/get_single_post', methods=(['GET']))
# def get_single_post():
#     subreddit = request.args.get('subreddit')
#     post_id = request.args.get('post_id')
#     url_posfix = request.args.get('url_posfix')
    
#     result = PostController.get_post_by_url(post_id=post_id, subreddit=subreddit,
#                                           url_posfix=url_posfix)
#     return json.dump(result)


@app.route('/')
def home():
    return "WORKING"


if __name__ == '__main__':
    app.run()