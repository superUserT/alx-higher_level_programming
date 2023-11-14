#!/usr/bin/node


class Rectangle {
    constructor (w, h) {
    if (w <= 0 || h <= 0) {
        return {};
    } else {
        this.width = w;
        this.height = h;
    }
}
print () {
    for (let counter = 0; counter < this.height; counter++) {
        console.log('X'.repeat(this.width));
    }
}
rotate () {
    [this.width, this.height] = [this.height, this.width];
}

double () {
    this.width *= 2;
    this.height *= 2;
}
}
module.exports = Rectangle;
