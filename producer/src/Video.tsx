import {Composition} from 'remotion';
import {HelloWorld} from './HelloWorld';
import {Title} from './HelloWorld/Title';

export const RemotionVideo: React.FC = () => {
	return (
		<>
			<Composition
				id="HelloWorld"
				component={HelloWorld}
				durationInFrames={150}
				fps={30}
				height={1920}
				width={1080}
				defaultProps={{
					titleText: 'Welcome to Remotion',
					titleColor: 'black',
				}}
			/>

			<Composition
				id="Title"
				component={Title}
				durationInFrames={100}
				fps={30}
				height={1920}
				width={1080}
				defaultProps={{
					titleText: 'Welcome to Remotion',
					titleColor: 'black',
				}}
			/>

		</>
	);
};
