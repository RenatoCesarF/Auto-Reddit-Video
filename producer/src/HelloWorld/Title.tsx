import {spring, useCurrentFrame, useVideoConfig} from 'remotion';
import Post from '../components/Post';

export const Title = () => {
	const videoConfig = useVideoConfig();
	const frame = useCurrentFrame();
	return (
		<h1
			style={{
				fontFamily: 'SF Pro Text, Helvetica, Arial',
				fontWeight: 'bold',
				fontSize: 100,
				textAlign: 'center',
				position: 'absolute',
				bottom: 160,
				width: '100%',
			}}
		>
			<span
				style={{
					marginLeft: 10,
					marginRight: 10,
					transform: `scale(${spring({
						fps: videoConfig.fps,
						frame: frame - 2 * 5,
						config: {
							damping: 100,
							stiffness: 200,
							mass: 0.5,
						},
					})})`,
					display: 'inline-block',
				}}
			>
					<Post
						body='Teste content'
						subreddit='renatinho'
						title='titulo teste'
						numVotes={20}						
						author='auto-reddit-videos'
						numComments={2}
						key={2}
					/>
				</span>
		
		</h1>
	);
};
