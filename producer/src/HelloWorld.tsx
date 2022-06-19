import {Sequence,  staticFile,  Audio, Img} from 'remotion';

import { PostInterface } from './components/PostElements/Post';
import {PostSequence} from './Sequences/PostSequence';
import { ReplySequence } from './Sequences/ReplySequence';

export const HelloWorld: React.FC<{
	post: PostInterface;
	lenght: number;
	path: string
}> = ({post, lenght, path}) => {


	let background = staticFile('/WANEELLA.gif')
	let	postAudioFile = null
	
	try{
		postAudioFile = staticFile('/audios/test.wav')
	}
	catch(e){

	}
	
	return (
		<div style={{flex: 1}}>
			<div>
				<Sequence key={0} from={0} durationInFrames={lenght}>		
					<Img src={background}/>
				</Sequence>
				
				<Sequence key={1} from={0} durationInFrames={lenght}>		
					<PostSequence post={post} />
				</Sequence>
				<Sequence key={2} from={10} durationInFrames={lenght}>		
					{postAudioFile != null ? 
						<Audio  src={postAudioFile}/> : <></>
					}
				</Sequence>
		
			</div>
		</div>
	);
};



