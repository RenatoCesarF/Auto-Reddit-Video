import { Sequence } from "remotion";


export default function LoadingSequence(){

    return(
        <Sequence key={2} from={0} durationInFrames={5*30 * 60} name="Loading">		
            <div className='center'>
                <h1>Loading...</h1>
            </div> 
        </Sequence>

    )
}