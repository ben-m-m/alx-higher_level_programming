#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const complete = {};
  const tasks = JSON.parse(body);
  for (const i in tasks) {
    const task = tasks[i];
    if (task.complete === true) {
      if (complete[task.userId] === undefined) {
        complete[task.userId] = 1;
      } else {
        complete[task.userId]++;
      }
    }
  }
  console.log(complete);
});
