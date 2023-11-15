#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Sqaure extends Rectangle {
  constructor (size) {
    if (size > 0) {
      super(size, size);
    }
  }
}
module.exports = Sqaure;
