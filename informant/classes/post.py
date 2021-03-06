from __future__ import annotations
from ctypes import Array
from typing import Dict
from requests import Response

from utils.clean_text import clean_text
from utils.log import log
from classes.redditArticle import RedditArticle

class Post(RedditArticle):
    title: str
    markdown_title: str
    url_posfix: str
    subreddit_img: str
    replies: Array[RedditArticle]
    
    def __init__(self, title: str, author: str, content: str, 
                 subreddit: str, url: str, id: str, up_votes_amount: int = 0):
        super().__init__(author=author, content=content, id=id, subreddit=subreddit,
                         up_votes_amount=up_votes_amount, url=url)
        self.markdown_title = title
        self.title = clean_text(title)
        
        if url is not None:
            urlSplited = url.split('/')
            self.url_posfix = urlSplited[-2]
        self.replies = []

    @staticmethod
    def create_from_dict(post: Dict)-> Post:
        data = post.get('data')
        if data == None:
            log.error(f"No data was found in Post {post}")
            raise Exception("no data was found in post: {}".format(post))
    
        post = Post(title=data.get('title'), 
                    subreddit=data.get('subreddit_name_prefixed'),
                    author=data.get('author'),
                    up_votes_amount=data.get('ups'),
                    content=data.get('selftext'),
                    url=data.get('url'),
                    id= data.get('id')
                )
        
        return post

    def set_replies_by_dict(self, replies: Dict):
        for rep in replies:
            data = rep.get('data')
            reply = RedditArticle.create_article_from_dict(data)
            if reply is None:
                continue
            self.replies.append(reply)
    
    @staticmethod
    def create_posts_from_response(posts_response: Response) -> Array[Post]:
        postsInstances: Array[Post] = []
        children = posts_response.get('data').get('children')
        
        for post in children:
            postsInstances.append(Post.create_from_dict(post))
            
        return postsInstances
               
    def to_json(self) -> Dict:
        dictObject = {
            'id': self.id, 
            'title': self.markdown_title, 
            'author': self.author, 
            'content': self.markdown_content,
            'subreddit': self.subreddit,
            'upVotesAmount': self.up_votes_amount,
            'url': self.url,
            "subredditImage": self.subreddit_img
        }
        return dictObject;    

    def __str__(self) -> str:
        return self.__get_self_representation_in_string()
                
    def __repr__(self) -> str:
        return self.__get_self_representation_in_string()
            
    def __get_self_representation_in_string(self) -> str:
        return (
            f"ID: {self.id}\n"
            f"title: {self.title}\n"
            f"author: {self.author}\n"
            f"subreddit: {self.subreddit}\n"
            f"url: {self.url}\n"
            f"up votes: {self.up_votes_amount}\n"
            f"content: {self.content}\n"
        )
            
