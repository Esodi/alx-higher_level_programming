#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return (null);
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let res = '';
    for (let i = 0; i < this.width; i++) {
      res += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(res);
    }
  }

  rotate () {
    const rot = this.width;
    this.width = this.height;
    this.height = rot;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
