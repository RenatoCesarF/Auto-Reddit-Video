
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';


interface AnimatedSequenceInterface {
	children: JSX.Element,
	duration: number
}


export const AnimatedSequence = ({ children, duration }: AnimatedSequenceInterface) => {
	const videoConfig = useVideoConfig();
	const frame = useCurrentFrame();

	const animation = calculateSprintAnimation(duration, frame, videoConfig.fps)

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
					transform: `scale(${animation})`,
				}}
			>
				<div className="big-zoom">
					{children}
				</div>
			</span>
		</div>
	);
};

const calculateSprintAnimation = (duration: number, frame: number, actualFps: any) => {
	let startAnimation = duration > 30 ? 30 : 15
	let endAnimation = duration - 30 ?? duration - 20

	if (startAnimation == endAnimation)
		startAnimation -= 1

	const interpolation = interpolate(
		frame,
		[0, startAnimation, endAnimation, duration],
		// v--v---v----------------------v
		[0, 20, 80, 0]
	);

	const springAnimation = spring({
		fps: actualFps,
		frame: interpolation,
		config: {
			damping: 100,
			stiffness: 100,
			mass: 0.5,
		},
	})
	return springAnimation
}