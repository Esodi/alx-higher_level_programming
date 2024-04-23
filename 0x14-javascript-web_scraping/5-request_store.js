#!/usr/bin/node

const req = require('request');
const fs = require('fs');

const url = process.argv[2];
const path = process.argv[3];

req(url, (err, resp, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const content = body;
  fs.writeFile(path, content, (error) => {
    if (err) {
      console.error(error);
    }
  });
});
