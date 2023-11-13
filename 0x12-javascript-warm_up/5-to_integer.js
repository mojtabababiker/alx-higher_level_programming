#!/usr/bin/node

const args = process.argv;
let msg = 'Not a number';
let myNumber = Number(args[2]);

msg = myNumber ? 'My number: ' + myNumber : msg
console.log(msg);
