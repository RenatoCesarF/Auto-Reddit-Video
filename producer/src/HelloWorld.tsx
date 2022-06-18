import { useCallback, useEffect, useState } from 'react';
import {continueRender, interpolate, Sequence, useCurrentFrame, useVideoConfig} from 'remotion';
import { PostInterface } from './components/PostElements/Post';
import {PostSequence} from './Sequences/PostSequence';
import { ReplySequence } from './Sequences/ReplySequence';

export const HelloWorld: React.FC<{
	titleText: string;
	titleColor: string;
}> = () => {
	const frame = useCurrentFrame();
	const videoConfig = useVideoConfig();
	const [lenght, setLenght] = useState(0);
	const audioPath = '';

	const videoPost: PostInterface = {
		content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
		title: 'A test Post for sure',
		author: 'RenatoCesarF',
		subreddit: 'r/AskReddit',
		votesAmount: 100
	}


	const fetchTts = useCallback(async () => {
		// await the get from api
		const audioPath = '../../../audios/v993sh.mp3'

		//set post info as receved

	}, []);

	useEffect(() => {
		fetchTts();
	}, [fetchTts]);
	
	return (
		<div style={{flex: 1, backgroundColor: "white"}}>
			<div>
				<Sequence from={0} durationInFrames={lenght * videoConfig.fps}>
					<PostSequence post={videoPost}  speachPath={audioPath}/>
				</Sequence>
				<Sequence from={100} durationInFrames={200}>
					<ReplySequence reply={videoPost}/>
				</Sequence>
			</div>
		</div>
	);
};
