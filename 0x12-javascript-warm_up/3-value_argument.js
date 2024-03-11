#!/usr/bin/node

const someVar = process.argv;

if (someVar[2] === undefined) {
	console.log('No argument');
} else {
	console.log(someVar[2]);
}
