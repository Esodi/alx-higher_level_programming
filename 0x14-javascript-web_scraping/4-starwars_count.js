#!/usr/bin/node

const req = require('request');

const url = process.argv[2];
const target = 'https://swapi-api.alx-tools.com/api/people/18/';

req(url, (err, resp, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const dict = JSON.parse(body);
  const lst = dict.results;
  let count = 0;
  for (let elem = 0; elem < lst.length; elem++) {
    const personLst = lst[elem].characters;
    personLst.forEach(i => {
      if (i === target) {
        count += 1;
      }
    });
  }
  console.log(count);
});
