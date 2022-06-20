import {Sequence,  staticFile,  Audio, Img} from 'remotion';
import { PostSequenceData, ReplySequenceData } from './classes/sequenceData';

import {PostSequence} from './Sequences/PostSequence';
import { ReplySequence } from './Sequences/ReplySequence';

const AUDIO_DELAY_IN_FRAMES = 12

export const HelloWorld: React.FC<{
	postSequenceData: PostSequenceData,
	replySequenceData: ReplySequenceData,
	totalLenght?: number
}> = ({postSequenceData, replySequenceData, totalLenght}) => {

	let background = staticFile('/WANEELLA.gif')
	let	postAudioFile = staticFile(postSequenceData.path)
	let	replyAudioFile = staticFile(replySequenceData.path)

	return (
		<div style={{flex: 1}}>
			<Sequence key={0} from={0} name="background" durationInFrames={totalLenght}>		
				<Img src={background}/>
			</Sequence>
			{/* POST SEQUENCE WITH AUDIO */}
			<Sequence 
				key={1} 
				from={0} 
				name="Post"
				durationInFrames={postSequenceData.lenght}
			>		
				<PostSequence post={postSequenceData.post} />
			</Sequence>
			<Sequence 
				key={2} 
				from={AUDIO_DELAY_IN_FRAMES} 
				name="Post Audio"
				durationInFrames={postSequenceData.lenght + AUDIO_DELAY_IN_FRAMES}
			>		
				<Audio src={postAudioFile}/>
			</Sequence>
			
			{/* REPLY SEQUENCE WITH AUDIO */}

			<Sequence 
				key={3} 
				from={postSequenceData.lenght} 
				durationInFrames={replySequenceData.lenght}
				name="Reply"
			>		
				<ReplySequence reply={replySequenceData.reply} />
			</Sequence> 
			<Sequence 
				key={4} 
				from={postSequenceData.lenght + 5 + AUDIO_DELAY_IN_FRAMES} 
				name="Reply Audio"
				durationInFrames={replySequenceData.lenght + AUDIO_DELAY_IN_FRAMES}
			>		
				<Audio src={replyAudioFile}/>
			</Sequence>
		</div>
	);
};



