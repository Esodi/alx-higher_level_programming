#!/usr/bin/node

const someVar = process.argv[2];
const toInt = parseInt(someVar);

if (Number.isNaN(toInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${toInt}`);
}
