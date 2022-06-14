from crypt import methods
import json
from re import A
from flask import Flask, request

from classes.RedditApi import RedditApi
from classes.post import Post
from controller.get_post_controller import PostController
from text_to_speak.tik_tok_text_to_speak import text_to_speak

app = Flask(__name__)

# @app.route('/get_post_data', methods=['GET'])
# def get_post_speach_data():
#     return  PostController.get_single_post('AskReddit')

@app.route('/get_single_post', methods=('GET'))
def get_single_post():
    subreddit = request.args.get('subreddit')
    post_id = request.args.get('post_id')
    url_posfix = request.args.get('url_posfix')
    
    result = PostController.get_post_by_url(post_id=post_id, subreddit=subreddit,
                                          url_posfix=url_posfix)
    return json.dump(result)