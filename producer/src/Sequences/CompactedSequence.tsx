import { Sequence, staticFile, Audio} from "remotion";
import Config from "../utils/configurationValue";
import Configuration from "../utils/configurationValue";
import { AnimatedSequence } from "./AnimatedSequence";


interface CompactedSequenceInterface{
    audioPath: string,
    lenght: number,
    from?: number,
    children: JSX.Element
}

export default function CompactedSequence({audioPath, lenght, children, from = 0}: CompactedSequenceInterface) {
	const sequenceAudio = staticFile(audioPath)

    return (
        <>
            <Sequence key={3} from={from} durationInFrames={lenght} name="Component">
                <AnimatedSequence>
                    {children}
                </AnimatedSequence>
            </Sequence><Sequence
                key={4} from={from}
                name="Audio" durationInFrames={lenght}
            >
                <Audio src={sequenceAudio} />
            </Sequence>
        </>
    )
}