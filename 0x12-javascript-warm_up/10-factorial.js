#!/usr/bin/node
// A script that computes and prints a factorial

const num = parseInt(process.argv[2]);
if (num === undefined || isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}

function factorial (x) {
  if (x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
