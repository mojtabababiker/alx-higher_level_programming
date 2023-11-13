#!/usr/bin/node

const args = process.argv;
const num = Number(args[2]);

function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

if (isNaN(num)) {
  console.log('1');
} else {
  console.log(factorial(num));
}
