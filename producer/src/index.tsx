import { registerRoot } from 'remotion';
import { RemotionVideo } from './Video';
import './styles/globals.css'
import getRandomBackground from './utils/getRandomBackground';

RemotionVideo.defaultProps = { backgroundPath: getRandomBackground() }
registerRoot(RemotionVideo);
