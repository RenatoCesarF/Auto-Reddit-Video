

interface PostHeaderInterface{
    author: string,
    subreddit: string,
}
const PostHeader = ({author, subreddit}: PostHeaderInterface) => {

    return (
        <div className="post-header-wrapper">
            <div className="header-text-wrapper margin-around">
                <img src="https://via.placeholder.com/20" className="subreddit-img"/>
                <span>{subreddit}</span>
                <span className="separation-dot"> • </span>
                <span style={{"color": "rgb(129, 131, 132)"}}>Posted by u/{author}</span>
            </div>
        </div>
    )
}


export default PostHeader