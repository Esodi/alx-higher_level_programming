#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(w)) {
      return (null);
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let r = '';
    for (let i = 0; i < this.width; i++) {
      r += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(r);
    }
  }
}

module.exports = Rectangle;
