#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const URL = 'https://swapi-api.alx-tools.com/api/films/';

request(URL + id, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
