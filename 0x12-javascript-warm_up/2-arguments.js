#!/usr/bin/node
// A script that prints a message depending of the number of arguments passed

'use strict';

// var myArgs = process.argv.slice(2);
for (let j = 1; j < process.argv.length; j++) {
  if (j < 2) {
    console.log('No argument');
  } else if (j === 2) {
    console.log('Argument found');
  } else {
    console.log('Arguments found');
  }
}
