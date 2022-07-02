import sys
import json
from os import getenv
from time import sleep
from typing import Dict
from dotenv import load_dotenv
import asyncio
import requests

load_dotenv()

BASE_URL = "https://graph.facebook.com/v14.0"
user_id = getenv("INSTAGRAM_USER_ID")
access_token = getenv("FACEBOOK_ACCESS_TOKEN")


def get_content_container_id(video_url: str, caption: str) -> Dict:
    response = requests.post(
        f"{BASE_URL}/{user_id}/media?video_url={video_url}&caption={caption}&access_token={access_token}&media_type=VIDEO"
    ).json()
    if response.get("error") is not None:
        raise Exception("ERROR was given creating the container " + str(response))
    return response.get("id")

def get_container_status(container_id):
    response = requests.get(
        f"{BASE_URL}/{container_id}?fields=status_code&access_token={access_token}"
    ).json()
    return response.get('status_code')
def publish_container(container_id: str):
    response = requests.post(
        f"{BASE_URL}/{user_id}/media_publish?creation_id={container_id}&access_token={access_token}"
    ).json()
    if response.get("error") is not None:
        raise Exception("Post was not publish due to " + str(response))
    return response

status_problems_response = ["EXPIRED", "ERROR"]



container_id = get_content_container_id("http://techslides.com/demos/sample-videos/small.mp4", "testing api posting")

status = get_container_status(container_id)
while status == "IN_PROGRESS":
    status = get_container_status(container_id)
    print(str(status))
    if status in status_problems_response:
        raise Exception("Something broke while checking container status")
    sleep(5)
    
print(publish_container(container_id))

