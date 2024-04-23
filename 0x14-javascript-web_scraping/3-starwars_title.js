#!/usr/bin/node

const req = require('request');

const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(url, (err, resp, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const dict = JSON.parse(body);
  const theTitle = dict.title;
  console.log(theTitle);
});
