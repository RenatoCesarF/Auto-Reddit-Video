from ctypes import Array
from typing import Dict
import requests
from os import getenv
from dotenv import load_dotenv

from classes.post import Post

USERNAME = 'auto-reddit-video'
DEFAULT_REDDIT_URL = 'https://oauth.reddit.com'

class RedditApi:
    def __init__(self):
        load_dotenv()
        self.__REDDIT_SECRET = getenv('REDDIT_SECRET')
        self.__REDDIT_CLIENT_KEY = getenv('REDDIT_CLIENT_KEY')
        self.__REDDIT_PASSWORD = getenv('REDDIT_PASSWORD')
        self.__headers = {'User-Agent': 'auto-video/0.0.1'}
        self.__token = ''
        self.__token = self.__get_access_token()
        self.__headers['Authorization'] = f'bearer {self.__token}'

    def __get_access_token(self):    
        auth = requests.auth.HTTPBasicAuth(self.__REDDIT_CLIENT_KEY, self.__REDDIT_SECRET)
        data = {
            'grant_type': 'password',
            'username': USERNAME,
            'password': self.__REDDIT_PASSWORD
        }

        res = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=self.__headers)
        return res.json()['access_token']

    def get_subreddit_hot_posts(self, subreddit: str):
        postsResponse = self.request_reddit_api(f'/r/{subreddit}/hot')
        postsData: Array[Post] = self.__get_posts_from_response(postsResponse)
        return postsData
    
    @staticmethod
    def format_single_post_path_request(subreddit: str, post_id: str, url_posfix:str) -> str:
        path = f'/r/{subreddit}/comments/{post_id}/{url_posfix}/'
        return path
    
    def get_post_replies(self, post: Post) -> Array[Dict]:
        path = RedditApi.format_single_post_path_request(post.subreddit, post.id, post.url_posfix)
        replies = self.request_reddit_api(path).get('data').get('children')
        
        return replies

    def get_post_by_url_paramters(self,subreddit: str, post_id: str, url_posfix: str) -> Post:
        path = RedditApi.format_single_post_path_request(subreddit, post_id, url_posfix)
        response = self.request_reddit_api(path)
        return self.__get_posts_from_response(response)

    
    def request_reddit_api(self, path: str) -> Dict:
        requested_url = f'{DEFAULT_REDDIT_URL}{path}'
        response: dict = requests.get(requested_url, headers=self.__headers, params={'limit': '20'}).json()[1]
        
        if response.get('data') is None:
            raise Exception('data is none when reach the request_reddit_api function. response: {}'
                            .format(str(response)))
            
        return response

    def __get_posts_from_response(self, posts: requests.Response) -> Array[Post]:
        postsInstances: Array[Post] = []
        children = posts.get('data').get('children')
        for post in children:
            postsInstances.append(Post.post_from_dict(post))
            
        return postsInstances

redditApi = RedditApi()