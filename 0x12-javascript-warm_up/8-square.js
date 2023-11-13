#!/usr/bin/node

const args = process.argv;
const size = Number(args[2]);
let square = '';

if (isNaN(size)) {
    console.log('Missing size');
} else {
    for (let i = 0; i < size; i++) {
	for (let j = 0; j < size; j++) {
	    square += 'x';
	}
	console.log(square);
	square = '';
    }
}
