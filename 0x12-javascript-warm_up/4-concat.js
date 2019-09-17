#!/usr/bin/node
// A script that prints two arguments passed to it, in the following format: “ is ”

process.argv.slice(2);
console.log(process.argv[2] + ' is ' + process.argv[3]);
