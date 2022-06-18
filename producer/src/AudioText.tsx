import { Sequence, staticFile } from "remotion";


export default function AudioTest() {


	const audioFile = staticFile('/audios/g2il7k.wv')
    return (
        <>			
        <Sequence from={0} durationInFrames={30}>		
            {/* <Audio src={} /> */}
        </Sequence>
        </>
    )
}