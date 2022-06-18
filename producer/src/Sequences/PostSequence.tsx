import {spring, useCurrentFrame, useVideoConfig, 	Audio, Img, staticFile,} from 'remotion';
import Loading from '../components/Loading';
import Post, { PostInterface } from '../components/PostElements/Post';

interface PostSequenceInterface{
	post: PostInterface,
}
export const PostSequence = ({post}: PostSequenceInterface) => {
	const videoConfig = useVideoConfig();
	const frame = useCurrentFrame();

	return (
		<div
			style={{
				position: 'absolute',
				top: "15%",
				width: '100%',
			}}
		>
			<span
				style={{
					marginLeft: 10,
					marginRight: 10,
					display: 'inline-block',
					transform: `scale(${spring({
						fps: videoConfig.fps,
						frame: frame -  5,
						config: {
							damping: 100,
							stiffness: 100,
							mass: 0.5,
						},
					})})`,
				}}
			>
				<div className="big-zoom">
					<Post
						key={1}
						content={post.content}
						subreddit={post.subreddit}
						title={post.title}
						votesAmount={post.votesAmount}
						author={post.author} 
					/>
				</div>
			</span>
		</div>
	);
};
