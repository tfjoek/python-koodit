let numbers = [];
let input;

while (true) {
    input = prompt("Enter a number:");
    let num = Number(input);
    if (numbers.includes(num)) {
        console.log(`The number ${num} has already been entered. Stopping...`);
        break;
    }
    numbers.push(num);
}

numbers.sort((a, b) => a - b);
console.log("Numbers entered ascending order:");
console.log(numbers);
