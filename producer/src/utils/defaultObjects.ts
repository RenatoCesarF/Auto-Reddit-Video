import { PostSequenceData, ReplySequenceData } from "../classes/sequenceData"
import { PostInterface } from "../components/PostElements/Post"
import { ReplyInterface } from "../components/PostElements/Reply"

export  const DEFAULT_POST: PostInterface = {
	content: "",
	title: '',
	author: '',
	subreddit: '',
	votesAmount: 0,
	subredditImage: ""
}
export const DEFAULT_REPLY: ReplyInterface = {
	author: '',
	votesAmount: 0,
	content: '',
	authorImage: ""
}

export const DEFAULT_REPLY_SEQUENCE:ReplySequenceData = {
    lenght: 0,
    path: "",
    reply: DEFAULT_REPLY
}
export const DEFAULT_POST_SEQUENCE:PostSequenceData = {
    lenght: 0,
    path: "",
    post: DEFAULT_POST
}