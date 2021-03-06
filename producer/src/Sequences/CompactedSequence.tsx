import { Sequence, staticFile, Audio } from "remotion";
import { AnimatedSequence } from "./AnimatedSequence";
import Config from "../utils/configurationValue"
interface CompactedSequenceInterface {
    audioPath: string,
    lenght: number,
    from?: number,
    children: JSX.Element
}

export default function CompactedSequence({ audioPath, lenght, children, from = 0 }: CompactedSequenceInterface) {
    return (
        <>
            <Sequence key={3} from={from} durationInFrames={lenght} name="Component">
                <AnimatedSequence duration={lenght}>
                    {children}
                </AnimatedSequence>
            </Sequence><Sequence
                key={4} from={from}
                name="Audio" durationInFrames={lenght}
            >
                <Audio src={audioPath} />
            </Sequence>
        </>
    )
}