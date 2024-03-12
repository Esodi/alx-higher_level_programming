#!/usr/bin/node

const Square = require('./5-square.js');

class Square1 extends Square {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c = 'X') {
    let res = '';
    for (let i = 0; i < this.size; i++) {
      res += c;
    }
    for (let j = 0; j < this.size; j++) {
      console.log(res);
    }
  }
}

module.exports = Square1;
