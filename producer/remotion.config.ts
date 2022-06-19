import {Config} from 'remotion';

const MINUTES = 10
Config.Rendering.setImageFormat('jpeg');
Config.Output.setOverwriteOutput(true);
Config.Puppeteer.setTimeoutInMilliseconds(MINUTES * 60 * 1000 );