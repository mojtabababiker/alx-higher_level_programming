#!/usr/bin/node

function add(a, b) {
    return a + b;
}

const args = process.argv;
let num1 = Number(args[2]);
let num2 = Number(args[3]);
console.log(add(num1, num2));
