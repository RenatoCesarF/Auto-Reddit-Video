import {Sequence,  staticFile,  Audio, Img} from 'remotion';
import { PostSequenceData, ReplySequenceData } from './classes/sequenceData';

import {PostSequence} from './Sequences/PostSequence';
import { ReplySequence } from './Sequences/ReplySequence';

const AUDIO_DELAY = 12
const VIDEO_DELAY = 10

export const HelloWorld: React.FC<{
	postSequenceData: PostSequenceData,
	replySequenceData: ReplySequenceData,
	totalLenght?: number
}> = ({postSequenceData, replySequenceData, totalLenght}) => {

	const replyStartFrame = postSequenceData.lenght + VIDEO_DELAY + AUDIO_DELAY
	const postCompleteLenght = postSequenceData.lenght + VIDEO_DELAY + AUDIO_DELAY


	const background = staticFile('/WANEELLA.gif')
	const postAudioFile = staticFile(postSequenceData.path)
	const replyAudioFile = staticFile(replySequenceData.path)

	return (
		<div style={{flex: 1}}>

			{/* BACKGROUND */}
			<Sequence key={0} from={0} name="background" durationInFrames={totalLenght}>		
				<Img src={background}/>
			</Sequence>
			{/* POST SEQUENCE WITH AUDIO */}
			<Sequence 
				key={1} 
				from={0} 
				name="Post"
				durationInFrames={postCompleteLenght}
			>		
				<PostSequence post={postSequenceData.post} />
			</Sequence>
			<Sequence 
				key={2} 
				from={0 + AUDIO_DELAY} 
				name="Post Audio"
				durationInFrames={postSequenceData.lenght + AUDIO_DELAY}
			>		
				<Audio src={postAudioFile}/>
			</Sequence>
			

			{/* REPLY SEQUENCE WITH AUDIO */}
			<Sequence 
				key={3} 
				from={replyStartFrame} 
				durationInFrames={replySequenceData.lenght}
				name="Reply"
			>		
				<ReplySequence reply={replySequenceData.reply} />
			</Sequence> 
			<Sequence 
				key={4} 
				from={replyStartFrame + AUDIO_DELAY} 
				name="Reply Audio"
				durationInFrames={replySequenceData.lenght + AUDIO_DELAY}
			>		
				<Audio src={replyAudioFile}/>
			</Sequence>
		</div>
	);
};



