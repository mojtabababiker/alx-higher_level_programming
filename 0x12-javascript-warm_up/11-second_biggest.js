#!/usr/bin/node

const args = process.argv;

let argc = args.length;
let firstMax;
let secondMax;
let num;

if (argc <= 3) {
    console.log('0');
} else { // 10 3 11 9 4
    firstMax = Number(args[2]);
    secondMax = -Infinity;
    for (let i = 3; i < argc; i++) {
	num = Number(args[i]);
	if (num > firstMax) {
	    secondMax = firstMax;
	    firstMax = num;
	} else if (num > secondMax) {
	    secondMax = num;
	}
    }
    console.log(secondMax);
}
