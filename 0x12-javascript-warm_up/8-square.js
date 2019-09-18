#!/usr/bin/node
// A script that prints a square

const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  let row = 'X';
  for (let i = 0; i < arg - 1; i++) {
    row += 'X';
  }
  for (let j = 0; j < arg; j++) {
    console.log(row);
  }
}
