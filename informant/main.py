from controller.get_post_controller import PostController
from classes.RedditApi import redditApi

posts = PostController.get_post_by_ur('Funnymemes', post_id="v93aw5",
                                        url_posfix="americans_do_this")

print(posts)

# print(PostController.get_single_post('askReddit'))