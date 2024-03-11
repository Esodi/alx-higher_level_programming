#!/usr/bin/node

const someVar = process.argv[2];
const toInt = parseInt(someVar);

if (Number.isNaN(toInt)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < toInt) {
    console.log('C is fun');
    i++;
  }
}
