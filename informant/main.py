from controller.get_post_controller import PostController
from classes.RedditApi import redditApi



# https://www.reddit.com/r/gamedev/comments/vekco1/questions_for_game_developers/
# posts = PostController.get_post_by_url('gamedev', post_id="vekco1",
                                        # url_posfix="questions_for_game_developers")
posts = PostController.get_single_post('gamedev')
print(posts)

# print(PostController.get_single_post('askReddit'))