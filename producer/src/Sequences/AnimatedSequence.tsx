
import {spring, useCurrentFrame, useVideoConfig} from 'remotion';


interface AnimatedSequenceInterface{
	children: JSX.Element,
}
export const AnimatedSequence = ({children}: AnimatedSequenceInterface) => {
	const videoConfig = useVideoConfig();
	const frame = useCurrentFrame();

	return (
		<div
			style={{
				position: 'absolute',
				top: 0,
				bottom: 0,
				marginBottom: "50%",
				marginTop: "50%",
				width: '100%',
				height: '100%'
			}}
		>
			<span
				style={{
					marginLeft: 10,
					marginRight: 10,
					display: 'inline-block',
					transform: `scale(${spring({
						fps: videoConfig.fps,
						frame: frame -  4,
						config: {
							damping: 100,
							stiffness: 100,
							mass: 0.5,
						},
					})})`,
				}}
			>
				<div className="big-zoom">
					{children}
				</div>
			</span>
		</div>
	);
};
