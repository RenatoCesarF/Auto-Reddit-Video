
import { useCallback, useEffect, useState } from 'react';
import {Composition, continueRender, delayRender} from 'remotion';
import AudioTest from './AudioText';
import {HelloWorld} from './HelloWorld';
import { getRandomPost } from './utils/getRedditData';

const FPS = 30

export const RemotionVideo: React.FC = () => {
	const [handle] = useState(() => delayRender());	   
	const [path, setPath] = useState('')
	const [lenght, setLenght] = useState(1)
	// const [reply, setReply] = useState()
	const [post, setPost] = useState({
		content: "",
		title: '',
		author: '',
		subreddit: '',
		votesAmount: 0
	})

    const fetchData = useCallback(async () => {
        const response = await getRandomPost('gamedev')
		setPath(response.speach.path)
		setLenght(Math.round(response.speach.lenght.toFixed() * FPS))
		setPost({
			content: response.post.content,
			title: response.post.content,
			author: response.post.author,
			subreddit: response.post.subreddit,
			votesAmount: response.post.upVotesAmount
		})
        continueRender(handle);
    }, [handle]);
    
	useEffect(() => {
		fetchData();
	}, [fetchData]);

	return (
		<>
			<Composition
				id="HelloWorld"
				component={HelloWorld}
				durationInFrames={lenght}
				fps={FPS}
				defaultProps={{lenght,path,post}}
				height={1920}
				width={1080}
			/>
		</>
	);
};
