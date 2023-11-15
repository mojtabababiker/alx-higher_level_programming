#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numOfAcc = 0;

  for (const element of list) {
    if (element === searchElement) {
      numOfAcc++;
    }
  }
  return numOfAcc;
};
