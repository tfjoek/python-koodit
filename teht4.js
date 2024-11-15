let numbers = [];
let input;
while (true) {
    input = prompt("Enter a number (0 to stop):");
    let num = Number(input);
    if (num === 0) break;
    
    numbers.push(num);
}

numbers.sort((a, b) => b - a);
console.log("Numbers descending order:");
console.log(numbers);
