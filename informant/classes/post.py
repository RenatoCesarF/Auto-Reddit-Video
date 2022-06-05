from typing import Dict
import json

class Post:
    title: str
    author: str
    content: str
    subreddit: str
    url: str
    up_votes_amount: int
    
    def __init__(self, title: str, author: str, content: str, 
                 subreddit: str, up_votes_amount: int = 0, url: str = ""):
        self.title = title
        self.author = author
        self.content = content
        self.subreddit = subreddit
        self.up_votes_amount = up_votes_amount
        self.url = url
        
    def toJson(self) -> Dict:
        dictObject = {
            'title': self.title, 
            'author': self.author, 
            'content': self.content,
            'subreddit': self.subreddit,
            'upVotesAmount': self.up_votes_amount,
            'url': self.url  
        }
        return json.dumps(dictObject);

        
    def get_self_representation_in_string(self) -> str:
        return (
            f"title: {self.title}\n"
            f"author: {self.author}\n"
            f"subreddit: {self.subreddit}\n"
            f"url: {self.url}\n"
            f"up votes: {self.up_votes_amount}\n"
            f"content: {self.content}\n"
        )
            
    def __str__(self) -> str:
        return self.get_self_representation_in_string()
      
                
    def __repr__(self) -> str:
        return self.get_self_representation_in_string()
            
 