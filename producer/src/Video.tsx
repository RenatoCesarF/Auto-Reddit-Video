
import { useCallback, useEffect, useState } from 'react';
import {Composition, continueRender, delayRender} from 'remotion';
import { resolveProjectReferencePath } from 'typescript';
import { PostSequenceData, ReplySequenceData} from './classes/sequenceData';
import LoadingSequence from './components/LoadingSequence';
import { PostInterface } from './components/PostElements/Post';
import { ReplyInterface } from './components/PostElements/Reply';
import {HelloWorld} from './HelloWorld';																		

import { getRandomPost } from './utils/getRedditData';

const FPS = 30
const DEFAULT_POST: PostInterface = {
	content: "",
	title: '',
	author: '',
	subreddit: '',
	votesAmount: 0
}
const DEFAULT_REPLY: ReplyInterface = {
	author: '',
	votesAmount: 0,
	content: ''
}

export const RemotionVideo: React.FC = () => {
	const [ApiCallHandle] = useState(() => delayRender("== Feching data from API =="));	  
	const [totalLenght, setTotalLenght] = useState(200) 
	const [ready, setReady] = useState(false)
	const [postSequence, setPostSequence] = useState<PostSequenceData>({
		post: DEFAULT_POST, 
		lenght: 1,
		path: ""
	})
	const [replySequence, setReplySequence] = useState<ReplySequenceData>({
		reply: DEFAULT_REPLY,
		lenght: 1,
		path: ""
	})

    const fetchData = useCallback(async () => {
		if(ready){
			continueRender(ApiCallHandle);
			return
		}
		const response = await getRandomPost('askReddit')
		setPostSequence({
			lenght: Math.round(response.post.speech.lenght.toFixed() * FPS),
			path: response.post.speech.path,
			post: {
				content: response.post.content,
				title: response.post.title,
				author: response.post.author,
				subreddit: response.post.subreddit,
				votesAmount: response.post.upVotesAmount
			}
		})
		setReplySequence({
			lenght: Math.round(response.reply.speech.lenght.toFixed() * FPS),
			path: response.reply.speech.path,
			reply: {
				content: response.reply.content,
				author: response.reply.author,
				votesAmount: response.reply.upVotesAmount
			}
		})
		setTotalLenght(getVideoTotalLenght([
			response.post.speech.lenght,
			response.reply.speech.lenght,
			0.4, //audio delay
			0.33, //video delay
		]))
		// setTotalLenght(120)
		setReady(true)
		continueRender(ApiCallHandle);
    }, [ApiCallHandle]);
    
	useEffect(() => {
		fetchData();
	}, [fetchData]);
	
	return (
		<>
			<Composition
				id="HelloWorld"
				component={ready ? HelloWorld : LoadingSequence}
				durationInFrames={ready ? totalLenght : 100}
				fps={FPS}
				defaultProps={{
					postSequenceData: postSequence,
					replySequenceData: replySequence,
					totalLenght: totalLenght
				}}
				height={1920}
				width={1080}
			/>
		</>
	);
};

function getVideoTotalLenght(lengths: number[]){
	let totalLenght: number = 0
	lengths.forEach((val) =>{
		totalLenght += val
	})
	return Math.round(totalLenght * FPS)
}
