#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  for (let i = 0; i < json.results.length; i++) {
    for (let j = 0; j < json.results[i].characters.length; j++) {
      if (json.results[i].characters[j].includes('/18/')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
