import ReactMarkdown from "react-markdown"
import VoteBar from "./VoteBar"
import replyFooter from '../../../assets/reply-footer.png'
import redditUser from '../../../assets/reddit-user.png'
import { Img } from "remotion"

export interface ReplyInterface {
  author: string,
  votesAmount: number,
  content: string,
  authorImage: string,
}
const Reply = ({authorImage, author, content, votesAmount}: ReplyInterface) => {
  authorImage = authorImage == "" ? redditUser : authorImage
  return (
    <div className="post-body" style={{flexDirection: "column"}}>  
      <div style={{display: "flex", alignItems: "center"}}>
        <Img src={authorImage} className="author-img"/>
        <div className="reply-header-text-wrapper margin-around">
          <span>{author}</span>
          <span className="separation-dot"> • </span>
          <span style={{"color": "rgb(129, 131, 132)"}}>23 hr. ago</span>
        </div>
      </div>

      <main className="reply-body">
        <ReactMarkdown>{content}</ReactMarkdown>

        <footer style={{display: "flex"}}>
          <VoteBar amount={votesAmount} flexDirection="row" iconSize={60}/>
          <Img src={replyFooter} style={{width: "70%"}}/>
        </footer>
      </main>
    </div>
  )
}

export default Reply
