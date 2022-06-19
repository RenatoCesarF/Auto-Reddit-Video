
import { useCallback, useEffect, useState } from 'react';
import {Composition, continueRender, delayRender} from 'remotion';
import SequenceData from './classes/sequenceData';
import {HelloWorld} from './HelloWorld';																		

import { getRandomPost } from './utils/getRedditData';

const FPS = 30
const DEFAULT_POST = {
	content: "",
	title: '',
	author: '',
	subreddit: '',
	votesAmount: 0
}

export const RemotionVideo: React.FC = () => {
	const [ApiCallHandle] = useState(() => delayRender("== Feching data from API =="));	   
	const [postSequence, setPostSequence] = useState<SequenceData>({
		post: DEFAULT_POST, 
		lenght: 1,
		path: ""
	})

    const fetchData = useCallback(async () => {
		const response = await getRandomPost('gamedev')
		setPostSequence({
			lenght: Math.round(response.speach.lenght.toFixed() * FPS),
			path: response.speach.path,
			post: {
				content: response.post.content,
				title: response.post.content,
				author: response.post.author,
				subreddit: response.post.subreddit,
				votesAmount: response.post.upVotesAmount
			}
		})
		
		continueRender(ApiCallHandle);
    }, [ApiCallHandle]);
    
	useEffect(() => {
		fetchData();
	}, [fetchData]);
	
	return (
		<>
			<Composition
				id="HelloWorld"
				component={HelloWorld}
				durationInFrames={postSequence.lenght}
				fps={FPS}
				defaultProps={{
					lenght: postSequence.lenght, 
					path: postSequence.path,
					post: postSequence.post
				}}
				height={1920}
				width={1080}
			/>
		</>
	);
};
