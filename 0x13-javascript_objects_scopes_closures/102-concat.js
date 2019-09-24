#!/usr/bin/node
// Write a script that concats 2 files

const fs = require('fs');

const a = process.argv[2];
const b = process.argv[3];
const c = process.argv[4];

const fileA = fs.readFileSync(a);
const fileB = fs.readFileSync(b);
const fileC = fileA + fileB;
