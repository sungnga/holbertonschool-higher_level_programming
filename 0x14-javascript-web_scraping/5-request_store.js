#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filepath = process.argv[3];

request({ url: url, json: true }, 'utf-8', (err, res) => {
  if (err) {
    console.log(err);
  } else {
    const content = res.body;
    fs.writeFile(filepath, content, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
