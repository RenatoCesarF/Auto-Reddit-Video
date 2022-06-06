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
        postsResponse = self.__request_reddit_api(f'/r/{subreddit}/hot').json()
        postsData: Array[Post] = self.__get_posts_from_response(postsResponse)
        return postsData

    def __request_reddit_api(self, path: str) -> requests.Response:
        requested_url = f'{DEFAULT_REDDIT_URL}{path}'
        response = requests.get(requested_url, headers=self.__headers)
        return response

    def __get_posts_from_response(self, posts: requests.Response) -> Array[Post]:
        postsInstances: Array[Post] = []
        children = posts['data']['children']
        for post in children:
            postsInstances.append(self.__get_post_data_by_json(post))
            
        return postsInstances
            
    def __get_post_data_by_json(self, post: Dict)-> Post:
        data = post['data']
        if data == None:
            raise Exception("no data was found in post")
        
        post = Post(title=data['title'], 
                    subreddit=data['subreddit_name_prefixed'],
                    author=data['author'],
                    up_votes_amount=data['ups'],
                    content=data['selftext'],
                    url=data['url']
                )
        
        return post
