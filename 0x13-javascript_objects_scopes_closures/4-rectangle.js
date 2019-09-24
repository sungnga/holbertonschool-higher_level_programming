#!/usr/bin/node
// Write a class Rectangle that defines a rectangle with instance methods of
// print(), double(), and rotate()

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row = row + 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    let tmp = 0;
    tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }
}

module.exports = Rectangle;
