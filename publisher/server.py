import sys
import json
from os import getenv
import requests

from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

from classes.instagram_api import InstagramAPI
from classes.log import log

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
load_dotenv()


@app.route("/publish", methods=["POST"])
def publish():
    try:
        video_url = request.args.get('video_url') 
        caption = request.args.get('caption') 
        
        insta = InstagramAPI(publication_type="REELS")
        response = insta.publish(video_url, caption)
        return json.dumps(response)
        
    except Exception as e:
        log.error(f"Server error:\n{e}")
        return {"message": e, "type": "ERROR"}



@app.route("/", methods=["GET"])
def home():
    print(str(getenv('FACEBOOK_ENDPOINT_SECRET')), file=sys.stderr)
    if request.args.get("hub.verify_token") == getenv('FACEBOOK_ENDPOINT_SECRET'):
        print("ITS THE SAME", file=sys.stderr)
        return request.args.get("hub.challenge")
    return "success"

if __name__ == '__main__':
    app.run()