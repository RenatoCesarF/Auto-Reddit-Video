import { PostInterface } from "../components/PostElements/Post";
import { ReplyInterface } from "../components/PostElements/Reply";

export type PostSequenceData = {
    lenght: number;
    path: string;
    post: PostInterface;
}

export type ReplySequenceData = {
    lenght: number;
    path: string;
    reply:  ReplyInterface;
}

