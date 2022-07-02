import sys
import json
from os import getenv

from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
load_dotenv()

BASE_URL = "https://graph.facebook.com/v14.0"


@app.route("/", methods=["GET"])
def home():
    print(str(getenv('FACEBOOK_ENDPOINT_SECRET')), file=sys.stderr)
    if request.args.get("hub.verify_token") == getenv('FACEBOOK_ENDPOINT_SECRET'):
        print("ITS THE SAME", file=sys.stderr)
        return request.args.get("hub.challenge")
    return "success"

if __name__ == '__main__':
    app.run()