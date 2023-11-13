#!/usr/bin/node

const args = process.argv;
const x = Number(args[2]);

if (x !== 0 && !x) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < x; i++) {
	console.log('C is fun');
    }
}
