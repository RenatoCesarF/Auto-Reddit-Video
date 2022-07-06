
import { useCallback, useEffect, useState } from 'react';
import { Composition, continueRender, delayRender } from 'remotion';
import { PostSequenceData, ReplySequenceData } from './classes/sequenceData';
import LoadingSequence from './components/LoadingSequence';
import { RedditVideo } from './RedditVideo';
import Config from './utils/configurationValue';
import { DEFAULT_POST_SEQUENCE, DEFAULT_REPLY_SEQUENCE } from './utils/defaultObjects';

import { getRandomPost } from './utils/getRedditData';

export const RemotionVideo: React.FC<{ backgroundPath?: string }> = ({ backgroundPath }) => {
	const [ApiCallHandle] = useState(() => delayRender("== Feching data from API =="));
	const [totalLenght, setTotalLenght] = useState(100)
	const [ready, setReady] = useState(false)
	const [postSequence, setPostSequence] = useState<PostSequenceData>(DEFAULT_POST_SEQUENCE)
	const [replySequence, setReplySequence] = useState<ReplySequenceData>(DEFAULT_REPLY_SEQUENCE)

	const fetchData = useCallback(async () => {
		const response = await getRandomPost('askReddit')
		setPostSequence({
			lenght: calculateSequenceLenght(response.post.speech.lenght),
			path: response.post.speech.path,
			post: {
				content: response.post.content,
				title: response.post.title,
				author: response.post.author,
				subreddit: response.post.subreddit,
				subredditImage: response.post.subredditImage,
				votesAmount: response.post.upVotesAmount
			}
		})
		setReplySequence({
			lenght: calculateSequenceLenght(response.reply.speech.lenght),
			path: response.reply.speech.path,
			reply: {
				content: response.reply.content,
				author: response.reply.author,
				votesAmount: response.reply.upVotesAmount,
				authorImage: response.reply.authorImage,
			}
		})
		setTotalLenght(getVideoTotalLenght([
			response.post.speech.lenght,
			response.reply.speech.lenght,
			0.37
		]))
		setReady(true)
		continueRender(ApiCallHandle);
	}, [ApiCallHandle]);

	useEffect(() => {
		fetchData();
	}, [fetchData]);

	return (
		<Composition
			id="RedditVideo"
			component={ready ? RedditVideo : LoadingSequence}
			durationInFrames={ready ? totalLenght : 5}
			fps={Config.FPS}
			defaultProps={{
				postSequenceData: postSequence,
				replySequenceData: replySequence,
				totalLenght: totalLenght,
				backgroundPath: backgroundPath ? backgroundPath : '/backgrounds/pizza.gif'
			}}
			height={1920}
			width={1080}
		/>

	);
};

const calculateSequenceLenght = (lenght: any) => {
	return Math.round((lenght.toFixed()) * Config.FPS) + 10
}
const getVideoTotalLenght = (lengths: number[]) => {
	let totalLenght: number = 0
	lengths.forEach((val) => {
		totalLenght += val
	})
	return Math.round(totalLenght * Config.FPS)
}
