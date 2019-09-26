#!/usr/bin/node
// Write a script that concats 2 files

const fs = require('fs');

const fileA = fs.readFileSync(`./${process.argv[2]}`);
const fileB = fs.readFileSync(`./${process.argv[3]}`);
fs.appendFileSync(`./${process.argv[4]}`, fileA + fileB, 'utf-8');
