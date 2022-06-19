import axios from "axios";


const DEFAULT_URL = "http://127.0.0.1:5000"
export async function getRandomPost(subreddit: string){
  let response = await axios.get(`${DEFAULT_URL}/get_post_data?subreddit=${subreddit}`)

  if(response.status != 200){
    throw new Error(response.status + response.data);
  }
  return response.data
}
