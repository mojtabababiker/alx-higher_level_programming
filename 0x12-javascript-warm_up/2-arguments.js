#!/usr/bin/node

const args = process.argv;
const argsNum = args.length;

if (argsNum === 2) {
  console.log('No argument');
} else if (argsNum === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
