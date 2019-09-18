#!/usr/bin/node
// A script that prints x times “C is fun”

const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i <= arg - 1; i++) {
    console.log('C is fun');
  }
}
