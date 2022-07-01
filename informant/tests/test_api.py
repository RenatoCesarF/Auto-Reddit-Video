
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from controller.get_post_controller import PostController
from text_to_speak.tik_tok_text_to_speak import tik_tok_text_to_speak
from classes.RedditApi import redditApi

def test_audio_exist():
    path = PostController.get_single_post().get("post").get("speech").get("path")
    path = f"../producer/public{path}"
    assert os.path.exists(path)