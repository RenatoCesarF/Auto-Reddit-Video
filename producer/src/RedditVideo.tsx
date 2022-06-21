import {Sequence,  staticFile, Img} from 'remotion';
import { PostSequenceData, ReplySequenceData } from './classes/sequenceData';
import Post from './components/PostElements/Post';
import Reply from './components/PostElements/Reply';

import CompactedSequence from './Sequences/CompactedSequence';

export const RedditVideo: React.FC<{
	postSequenceData: PostSequenceData,
	replySequenceData: ReplySequenceData,
	totalLenght?: number
}> = ({postSequenceData, replySequenceData, totalLenght}) => {
	const secondSequenceStartFrame = postSequenceData.lenght
	const background = staticFile('/WANEELLA.gif')
	return (
		<div style={{flex: 1}}>

			{/* BACKGROUND */}
			<Sequence key={0} from={0} name="background" durationInFrames={totalLenght}>		
				<Img src={background}/>
			</Sequence>
			<CompactedSequence 
				audioPath={postSequenceData.path} 
				lenght={postSequenceData.lenght}
			>
				<Post 
					content={postSequenceData.post.content} 
					title={postSequenceData.post.title}
					author={postSequenceData.post.author}
					subreddit={postSequenceData.post.subreddit}
					votesAmount={postSequenceData.post.votesAmount}
				/>
			</CompactedSequence>

			<CompactedSequence 
				audioPath={replySequenceData.path} 
				lenght={replySequenceData.lenght}
				from={secondSequenceStartFrame}
			>
				<Reply 
					content={replySequenceData.reply.content} 
					author={replySequenceData.reply.author}
					votesAmount={replySequenceData.reply.votesAmount}
				/>
			</CompactedSequence>
		</div>
	);
};



