import { Img } from "remotion"
import redditUser from '../../../assets/reddit-user.png'
interface PostHeaderInterface {
    author: string,
    subreddit: string,
    subredditImage: string,
}
const PostHeader = ({ author, subreddit, subredditImage }: PostHeaderInterface) => {
    return (
        <div className="header-text-wrapper margin-around">
            <Img src={subredditImage} className="subreddit-img" />
            <span>{subreddit}</span>
            <span className="separation-dot"> • </span>
            <span style={{ "color": "rgb(129, 131, 132)" }}>Posted by u/{author}</span>
        </div>
    )
}


export default PostHeader