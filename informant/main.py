from controller.get_post_controller import PostController
from classes.RedditApi import redditApi

posts = PostController.get_single_post('gamedev')
print(posts)
