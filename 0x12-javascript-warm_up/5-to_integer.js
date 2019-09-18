#!/usr/bin/node
// A script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log(parseInt(arg));
}
