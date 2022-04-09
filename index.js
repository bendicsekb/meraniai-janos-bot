// source: https://www.youtube.com/watch?v=fD-GRCH_tks&t=470s&ab_channel=Domthedev

const {rwClient} = require('./twitterClient.js');
const {readWriteSync} = require('./readLineOfFile');


const tweet = async () => {
    try {
        await rwClient.v2.tweet(readWriteSync('generated_sentences.txt'));
    } catch (err) {
        console.error(err);
        
    }

}

async function run() {
    i = 0
    while(true){
        await new Promise(r => setTimeout(r, i * 1000 * 60 * 60));
        tweet();
        i = i + 1;
    }
}

run()