from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

from utils.log import log, LogType
from classes.RedditApi import RedditApi
from classes.post import Post
from controller.get_post_controller import PostController
from utils.await_after_multiple_calls import await_after_multiple_calls


log(LogType.INFO, "STARTING SERVER...")

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
        return  json.dumps(response)
    except Exception as e:
        log(LogType.ERROR, f"Server error:\n{e}")
        return {"message": e, "type": "ERROR"}



if __name__ == '__main__':
    app.run()