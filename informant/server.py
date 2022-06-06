import json
from re import A
from flask import Flask

from classes.RedditApi import RedditApi
from classes.post import Post
from controller.get_post_controller import PostController
from text_to_speak.tik_tok_text_to_speak import text_to_speak

app = Flask(__name__)

@app.route('/get_post_speach_data', methods=['GET'])
def get_post_speach_data():
    return  PostController.get_single_post('AskReddit')