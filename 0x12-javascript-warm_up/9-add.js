#!/usr/bin/node

function add(a, b) {
    return a + b;
}

if (process.argv[2] && process.argv[3]) {
    const num1 = parseInt(process.argv[2]);
    const num2 = parseInt(process.argv[3]);

    if (!isNaN(num1) && !isNaN(num2)) {
        const result = add(num1, num2);
        console.log(result);
    }
}
if (process.argv.length <= 3) {
    console.log("NaN")
}