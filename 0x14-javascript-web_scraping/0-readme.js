#!/usr/bin/node

const fs = require('fs');

const par = process.argv[2];

fs.readFile(par, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
