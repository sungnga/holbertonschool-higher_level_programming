#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments

const argLen = process.argv.length;
if (argLen < 4) {
  console.log(0);
} else {
  const list = process.argv.slice(2);
  const secondMax = list.sort(function (a, b) { return b - a; })[1];
  console.log(secondMax);
}
