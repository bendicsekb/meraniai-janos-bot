// source: https://www.youtube.com/watch?v=fD-GRCH_tks&t=470s&ab_channel=Domthedev

const {TwitterApi} = require('twitter-api-v2');

const twitterClient = new TwitterApi({
    appKey: '',
    appSecret: '',
    accessToken: '',
    accessSecret: ''    
});

const rwClient = twitterClient.readWrite

module.exports = {
    rwClient: rwClient
}