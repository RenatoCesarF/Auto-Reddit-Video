const util = require('node:util');
const exec = util.promisify(require('node:child_process').exec);

run_command = "npm run build"

async function generateVideo() {
    const { stdout, stderr } = await exec(run_command);
    console.log(stdout);
    console.error('stderr:', stderr);
}

generateVideo();

