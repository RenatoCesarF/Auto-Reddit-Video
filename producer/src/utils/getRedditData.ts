import axios from "axios";


export default function getPostByInfo(subreddit: string, id: string, postFixInfo: string){
}

export function getRandomPost(subreddit: string){
  axios.get(`http://127.0.0.1:5000/get_post_data?subreddit=${subreddit}`)
    .then(res => {
      console.log(`statusCode: ${res.status}`);
      console.log(res);
  })
  .catch(error => {
    console.error(error);
  });
  //return data
}
