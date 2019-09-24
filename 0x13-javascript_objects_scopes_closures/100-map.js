#!/usr/bin/node
// Write a script that imports an array and computes a new array using map()

const list = require('./100-data').list;

const newList = list.map((value, index) => value * index);
console.log(list);
console.log(newList);
