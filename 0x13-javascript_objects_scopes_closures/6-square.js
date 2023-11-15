#!/usr/bin/node

const SqaureParent = require('./5-square');

class Sqaure extends SqaureParent {
  charPrint (c = 'X') {
    const chr = c;
    let shape = '';

    /* chr ??= 'X'; */
    for (let row = 0; row < this.height; row++) {
      for (let col = 0; col < this.width; col++) {
        shape += chr;
      }
      console.log(shape);
      shape = '';
    }
  }
}
module.exports = Sqaure;
