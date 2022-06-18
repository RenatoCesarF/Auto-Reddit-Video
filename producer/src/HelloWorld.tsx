import {Sequence,  staticFile,  Audio, Img} from 'remotion';

import { PostInterface } from './components/PostElements/Post';
import {PostSequence} from './Sequences/PostSequence';
import { ReplySequence } from './Sequences/ReplySequence';

export const HelloWorld: React.FC<{
	post: PostInterface;
	lenght: number;
	path: string
}> = ({post, lenght, path}) => {

	let postAudioFile = null
	let replyAudioFile = null
	let background = staticFile('/WANEELA.gif')

	try {
		postAudioFile = staticFile('/audios/test.wav')
		replyAudioFile = staticFile('/audios/test.wav')
	} catch (error) {
		
	}

	return (
		<div style={{flex: 1, backgroundColor: "white"}}>
			<Img src={background}/>
			<div>
				{post.content != "" ?
					<>
						<Sequence from={0} durationInFrames={lenght}>		
							<PostSequence post={post} />
						</Sequence>
						<Sequence from={12} durationInFrames={lenght}>		
							{postAudioFile != null ? 
								<Audio key={34} src={postAudioFile}/> : <></>
							}
						</Sequence>
					</>
					:
					<></>
				}
			
			</div>
		</div>
	);
};



