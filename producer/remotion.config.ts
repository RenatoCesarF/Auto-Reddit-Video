import {Config} from 'remotion';

const MINUTES = 1
Config.Rendering.setImageFormat('png');
Config.Output.setOverwriteOutput(true);
Config.Puppeteer.setTimeoutInMilliseconds(MINUTES * 60 * 1000);