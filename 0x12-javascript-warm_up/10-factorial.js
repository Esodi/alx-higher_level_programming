#!/usr/bin/node

function fact (num) {
  let f = 1;

  if (Number.isNaN(num) || num === 1) {
    return f;
  } else {
    f *= num;
    num -= 1;
    if (num !== 1) {
      const f2 = fact(num);
      f *= f2;
    }
  }
  return f;
}

const num = process.argv[2];
const numInt = parseInt(num);
const result = fact(numInt);
console.log(result);
