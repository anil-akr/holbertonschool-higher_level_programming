#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(Number).sort((a, b) => b - a);
  const uniqueNumbers = [...new Set(numbers)];
  
  if (uniqueNumbers.length <= 1) {
    console.log(0);
  } else {
    console.log(uniqueNumbers[1]);
  }
}
