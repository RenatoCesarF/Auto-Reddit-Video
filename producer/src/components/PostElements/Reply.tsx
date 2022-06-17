import ReactMarkdown from "react-markdown"
import VoteBar from "./VoteBar"
import replyFooter from '../../../assets/reply-footer.png'

export interface ReplyInterface {
  author: string,
  votesAmount: number,
  content: string,
}
const Reply = ({author, content, votesAmount}: ReplyInterface) => {
  return (
    <div className="post-body" style={{flexDirection: "column"}}>  
      <div style={{display: "flex", alignItems: "center"}}>
        <img src="https://via.placeholder.com/100" className="author-img"/>
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
          <img src={replyFooter} style={{width: "70%"}}/>
        </footer>
      </main>
    </div>

    
  )
}

export default Reply

/*
    // <div className="post-body"> 
    //   <div style={{display: "flex", alignItems: "center"}}>
    //     <img src="https://via.placeholder.com/100" className="author-img"/>
    //     <div className="reply-header-text-wrapper margin-around">
    //       <span>{author}</span>
    //       <span className="separation-dot"> • </span>
    //       <span style={{"color": "rgb(129, 131, 132)"}}>23 hr. ago</span>
    //     </div>
    //   </div>

    //   <main style={{marginLeft: "90px"}}>
    //     <ReactMarkdown>{content}</ReactMarkdown>

    //     <footer style={{display: "flex"}}>
    //       <VoteBar amount={votesAmount} flexDirection="row" iconSize={60}/>
    //       <img src={replyFooter} style={{width: "70%"}}/>
    //     </footer>
    //   </main>
    // </div>

*/