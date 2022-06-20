import ReactMarkdown from 'react-markdown'

import PostHeader from "./PostHeader"
import VoteBar from "./VoteBar"
import postFooter from '../../../assets/post-footer.png'
import { Img } from 'remotion'

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
            <div style={{margin: "0px 35px 0 0"}}>
                <VoteBar amount={votesAmount}/>
            </div>
            <div>
                <PostHeader author={author} subreddit={subreddit}/>
                <h3>
                    {title}  
                </h3>
    
                <ReactMarkdown>{content}</ReactMarkdown> 
                <footer>
                    <Img src={postFooter} style={{width: "90%", maxWidth: "90%"}}/>
                </footer> 
            </div> 
        </div>
    )
}

export default Post