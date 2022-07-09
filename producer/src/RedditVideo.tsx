import { Sequence, staticFile, Img, AbsoluteFill, useVideoConfig } from 'remotion';
import { Gif } from "@remotion/gif";
import { PostSequenceData, ReplySequenceData } from './classes/sequenceData';
import Post from './components/PostElements/Post';
import Reply from './components/PostElements/Reply';
import CompactedSequence from './Sequences/CompactedSequence';


export const RedditVideo: React.FC<{
	postSequenceData: PostSequenceData,
	replySequenceData: ReplySequenceData,
	backgroundPath: string
	totalLenght?: number,
}> = ({ postSequenceData, replySequenceData, totalLenght, backgroundPath }) => {

	const secondSequenceStartFrame = postSequenceData.lenght + 5

	const background = staticFile(backgroundPath)
	const { width, height } = useVideoConfig();


	return (
		<div style={{ flex: 1 }}>

			{/* BACKGROUND */}
			<Sequence key={0} from={0} name="background" durationInFrames={totalLenght}>
				<Gif
					src={background}//"https://media.giphy.com/media/3o72F7YT6s0EMFI0Za/giphy.gif"
					width={width}
					height={height}
					fit="cover"
				/>
			</Sequence>
			<CompactedSequence
				audioPath={postSequenceData.path}
				lenght={postSequenceData.lenght}>
				<Post
					content={postSequenceData.post.content}
					title={postSequenceData.post.title}
					author={postSequenceData.post.author}
					subreddit={postSequenceData.post.subreddit}
					votesAmount={postSequenceData.post.votesAmount}
					subredditImage={postSequenceData.post.subredditImage} />
			</CompactedSequence>

			<CompactedSequence
				audioPath={replySequenceData.path}
				lenght={replySequenceData.lenght}
				from={secondSequenceStartFrame}>
				<Reply
					content={replySequenceData.reply.content}
					author={replySequenceData.reply.author}
					votesAmount={replySequenceData.reply.votesAmount}
					authorImage={replySequenceData.reply.authorImage} />
			</CompactedSequence>
		</div>
	);
};



