import {spring, useCurrentFrame, useVideoConfig} from 'remotion';
import Reply, { ReplyInterface } from '../components/PostElements/Reply';

interface ReplySequenceInterface{
	reply: ReplyInterface
}
export const ReplySequence = ({reply}: ReplySequenceInterface) => {
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
					<Reply
						content={reply.content}
						votesAmount={reply.votesAmount}
						author={reply.author}
						key={0}
					/>
				</div>
			</span>
		</div>
	);
};
