#!/usr/bin/node

const args = process.argv;
const myNumber = Number(args[2]);
let msg = 'Not a number';

msg = myNumber ? 'My number: ' + myNumber : msg;
console.log(msg);
