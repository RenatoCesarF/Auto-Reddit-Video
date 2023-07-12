from requests import get, post
from os import getenv
from time import sleep
from typing import Dict
from dotenv import load_dotenv

from classes.log import log

BASE_URL = "https://graph.facebook.com/v14.0"
status_problems_response = ["EXPIRED", "ERROR"]


class InstagramAPI:
    """Can publish videos/reels on instagram
    :param: publication_type = VIDEO | REELS
    """
    user_id: str
    __access_token: str
    publication_type: str

    def __init__(self, publication_type: str = "VIDEO"):
        load_dotenv()
        self.user_id = getenv("INSTAGRAM_USER_ID")
        self.__access_token = getenv("FACEBOOK_ACCESS_TOKEN")
        self.publication_type = publication_type
        
        if self.user_id is None:
            log.error("Get enviroment fail")

    def publish(self, video_url: str, caption: str) -> Dict:
        """Do all the process of creating a container, checking its status until it
        gets finished and then publishing it"""
        log.info("Creating content Container...")
        container_id = self.create_content_container(video_url, caption)
        log.info(f"Container created, id: {container_id}")
        status = self.get_container_status(container_id)
        
        log.info("Checking status...")
        while status == "IN_PROGRESS":
            status = self.get_container_status(container_id)
            log.info(f"status: {status}...")

            sleep(1)
        log.info("Publishing container...")
        publish_response = self.publish_container(container_id)
        log.info("Finish publication!")
        return publish_response

    def create_content_container(self, video_url: str, caption: str) -> Dict:
        """Create a content container in instagram service that can receive
        media that will be publish when the container get published.

        return: the id of the container"""
        response = post(
            f"{BASE_URL}/{self.user_id}/media?video_url={video_url}&caption={caption}&access_token={self.__access_token}&media_type={self.publication_type}"
        ).json()
        
        if response.get("error") is not None:
            log.error(f"Container creation raise an error while requesting: {response}")
            raise Exception("ERROR was given creating the container " + str(response))
        
        return response.get("id")

    def get_container_status(self, container_id: str):
        """Return the status of the container passed in.
        it can be: EXPIRED, ERROR, FINISHED, PUBLISHED
        """
        response = get(
            f"{BASE_URL}/{container_id}?fields=status_code&access_token={self.__access_token}"
        ).json()
        status = response.get("status_code")
        if status in status_problems_response:
            log.error(f"An error ocurred while checking container's status {status}")
            raise Exception("Something broke while checking container status")
        
        return status

    def publish_container(self, container_id: str) -> Dict:
        """Try to publish a container, if it's status is not published or finished,
        it will not publish. returns the response of the operation
        """
        response = post(
            f"{BASE_URL}/{self.user_id}/media_publish?creation_id={container_id}&access_token={self.__access_token}"
        ).json()
        if response.get("error") is not None:
            log.error(f"An error ocurred trying to publish an container {response}")
            raise Exception("Post was not publish due to " + str(response))
        return response
