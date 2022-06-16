import React from 'react'
import ReactMarkdown from 'react-markdown'
// import ReactDom from 'react-dom'

import PostHeader from "./PostHeader"
import VoteBar from "./VoteBar"


export interface PostInterface{
    content: string,
    title: string,
    author: string,
    subreddit: string,
    votesAmount: number,
}
const Post = ({content, title, author, subreddit, votesAmount}: PostInterface) =>{
    return (
        <div className="post-body"> 
            <div style={{margin: "15px 35px 0 0"}}>
                <VoteBar  amount={votesAmount} />
            </div>
            <body>
                <PostHeader author={author} subreddit={subreddit}/>
                <h3>{title}</h3>
                <ReactMarkdown>{content}</ReactMarkdown>
            </body>
        </div>
    )
}

export default Post