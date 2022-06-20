from __future__ import print_function 

from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_ngrok import run_with_ngrok

from classes.RedditApi import RedditApi
from classes.post import Post
from controller.get_post_controller import PostController
from text_to_speak.tik_tok_text_to_speak import text_to_speak
from utils.await_after_multiple_calls import await_after_multiple_calls


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/get_post_data', methods=['GET'])
@cross_origin()
def get_post_speech_data():
    try:
        subreddit = request.args.get('subreddit') 
        await_after_multiple_calls(100)
        response = PostController.get_single_post(subreddit)
        return  response
    except Exception as e:
        print(f"[SERVER ERROR] {e}")
        return {"message": e, "type": "ERROR"}


@app.route('/')
@cross_origin()
def home():
    return "WORKING"


if __name__ == '__main__':
    app.run()