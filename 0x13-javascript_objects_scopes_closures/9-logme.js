#!/usr/bin/node

let argsCounter = 0;
exports.logMe = function (item) {
  argsCounter = typeof argsCounter !== 'undefined'
    ? argsCounter
    : 0;

  console.log(`${argsCounter}: ${item}`);
  argsCounter++;
};
