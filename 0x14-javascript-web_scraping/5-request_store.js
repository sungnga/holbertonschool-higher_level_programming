#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filepath = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = body.body;
    fs.writeFile(filepath, content, 'utf-8', (err, data) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
