#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, (err, response) => {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + response.statusCode);
});
