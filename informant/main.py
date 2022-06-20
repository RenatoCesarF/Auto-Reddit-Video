from controller.get_post_controller import PostController
from classes.RedditApi import redditApi

post = PostController.get_single_post('rust')
print(str(post))