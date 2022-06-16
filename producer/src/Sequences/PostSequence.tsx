import {spring, useCurrentFrame, useVideoConfig} from 'remotion';
import Post, { PostInterface } from '../components/PostElements/Post';

interface PostSequenceInterface{
	post: PostInterface
}
export const PostSequence = ({post}: PostSequenceInterface) => {
	const videoConfig = useVideoConfig();
	const frame = useCurrentFrame();
	return (
		<div
			style={{
				fontSize: 100,
				position: 'absolute',
				bottom: 600,
				width: '100%',
			}}
		>
			<span
				style={{
					marginLeft: 10,
					marginRight: 10,
					transform: `scale(${spring({
						fps: videoConfig.fps,
						frame: frame -  5,
						config: {
							damping: 100,
							stiffness: 100,
							mass: 0.5,
						},
					})})`,
					display: 'inline-block',
				}}
			>
				<div className="big-zoom">
					<Post
						content={post.content}
						subreddit={post.subreddit}
						title={post.title}
						votesAmount={post.votesAmount}
						author={post.author}
						key={0}
					/>
				</div>
			</span>
		</div>
	);
};
