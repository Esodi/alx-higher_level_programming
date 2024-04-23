#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req (url, (err, resp, body) => {
	if (err) {
		console.error(err);
		return;
	}
	const data = JSON.parse(body);
	const ilst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
	const olst = {};
	let count = 0;
	ilst.forEach(i => {
		data.forEach(j => {
			if (j.userId === i) {
				if (j.completed === true) {
					count += 1;
				}
			}
		});
		olst[i] = count;
		count = 0;
	});
	console.log(olst);
});
