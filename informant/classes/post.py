from __future__ import annotations
from ctypes import Array
from typing import Dict

from classes.redditArticle import RedditArticle

class Post(RedditArticle):
    title: str
    url_posfix: str
    replies: Array[RedditArticle]
    
    def __init__(self, title: str, author: str, content: str, 
                 subreddit: str, url: str, id: str, up_votes_amount: int = 0):
        super().__init__(author=author, content=content, id=id, subreddit=subreddit,
                         up_votes_amount=up_votes_amount, url=url)
        self.title = title
        
        if url is not None:
            urlSplited = url.split('/')
            self.url_posfix = urlSplited[-2]
        self.replies = []

    @staticmethod
    def create_from_dict(post: Dict)-> Post:
        data = post.get('data')
        if data == None:
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

    def set_replies(self, replies: Array[Dict]):
        for rep in replies:
            data = rep['data']
            reply = self.create_article_from_dict(data)
            if reply is None:
                continue
            self.replies.append(reply)
            
           
    def toJson(self) -> Dict:
        dictObject = {
            'id': self.id, 
            'title': self.title, 
            'author': self.author, 
            'content': self.content,
            'subreddit': self.subreddit,
            'upVotesAmount': self.up_votes_amount,
            'url': self.url  
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
            
