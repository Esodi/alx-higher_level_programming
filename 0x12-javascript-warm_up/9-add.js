#!/usr/bin/node

function add (a, b) {
  const c = a + b;
  console.log(c);
}

const a = process.argv[2];
const b = process.argv[3];
const aInt = parseInt(a);
const bInt = parseInt(b);

add(aInt, bInt);
