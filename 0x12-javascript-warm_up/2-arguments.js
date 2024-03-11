#!/usr/bin/node

const someVar = process.argv;

if ((someVar.length - 2) < 1)
{
	console.log('No argument');
}
else if ((someVar.length - 2) === 1)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
