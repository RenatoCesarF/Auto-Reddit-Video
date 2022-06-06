from __future__ import annotations
from ctypes import Array
from tkinter import E
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
        
        urlSplited = url.split('/')
        self.url_posfix = urlSplited[-2]
        self.replies = []

    def to_speach(self, path: str):
        #mach title and content mp3 audio, save and return the path
        pass

    @staticmethod
    def post_from_dict(post: Dict)-> Post:
        data = post['data']
        if data == None:
            raise Exception("no data was found in post")
        
        post = Post(title=data['title'], 
                    subreddit=data['subreddit_name_prefixed'],
                    author=data['author'],
                    up_votes_amount=data['ups'],
                    content=data['selftext'],
                    url=data['url'],
                    id= data['id']
                )
        
        return post

    def set_replies(self, replies: Array[Dict]):
        for rep in replies:
            data = rep['data']
            self.replies.append(
                RedditArticle.create_article_from_dict(data)
            )
            
           
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
            

    def __str__(self) -> str:
        return self.__get_self_representation_in_string()
      
                
    def __repr__(self) -> str:
        return self.__get_self_representation_in_string()
            
 