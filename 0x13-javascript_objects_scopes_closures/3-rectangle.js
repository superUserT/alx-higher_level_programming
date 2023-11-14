#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0) {
            return {};
        }
        this.weight = w;
        this.height = h;
    }
    print() {
        for (let counter = 0; counter < this.height; counter++) {
            console.log("X".repeat(this.width));
        }
    }
}

module.exports = Rectangle;