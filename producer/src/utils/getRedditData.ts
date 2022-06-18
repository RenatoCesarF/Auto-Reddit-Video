import axios from "axios";


const DEFAULT_URL = "https://7f34-170-254-139-207.sa.ngrok.io"
export async function getRandomPost(subreddit: string){
  let response = await axios.get(`${DEFAULT_URL}/get_post_data?subreddit=${subreddit}`)

  if(response.status != 200){
    throw new Error(response.status + response.data);
  }
  return response.data
}
