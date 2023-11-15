#!/usr/bin/node

exports.esrever = function (list) {
  let end = list.length - 1;
  let start = 0;
  let temp;

  while (end >= start) {
    temp = list[end];
    list[end] = list[start];
    list[start] = temp;
    end--;
    start++;
  }
  return list;
};
