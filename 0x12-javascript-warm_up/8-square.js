#!/usr/bin/node

const someVar = process.argv[2];
const toInt = parseInt(someVar);

if (Number.isNaN(toInt)) {
  console.log('Missing size');
} else {
  let cat = '';
  for (let i = 0; i < toInt; i++) {
    cat += 'X';
  }
  for (let j = 0; j < toInt; j++) {
    console.log(cat);
  }
}
