#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let shape = '';
    for (let row = 0; row < this.height; row++) {
      for (let col = 0; col < this.width; col++) {
        shape += 'X';
      }
      console.log(shape);
      shape = '';
    }
  }

  rotate () {
    let temp;
    if (this.width > 0 && this.height > 0) {
      temp = this.width;
      this.width = this.height;
      this.height = temp;
    }
  }

  double () {
    if (this.width > 0 && this.width > 0) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
