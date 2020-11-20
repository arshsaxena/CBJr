// Comparisons (>, <, ==, !=, >=, and <=)

let a = 2;
let b = 3;
console.log("a =", a)
console.log("b =", b)

console.log("a > b:", a > b); // Greater than (>)
console.log("a < b:", a < b); // Less than (<)
console.log("a == b:", a == b); // Equals to (==)

b = 14; // Assignment (=)

console.log("a >= b:", a >= b); // Greater than equals to (>=)
console.log("a <= b:", a <= b); // Less than equals to (>=)

console.log("2 != 14:", 2 != 14); // Not equals to (!=)
console.log("14 != 14:", 14 != 14);

// Strings are checked in dictonary order (lexicographically)
console.log("Arsh > Unknown:", "Arsh" > "Unnkown"); 
console.log("Arsh > Ankit:", "Arsh" > "Ankit"); 
console.log("A > H:", "A" > "H");
console.log("Bee > Be:", "Bee" > "Be");

// Comparing a string and a number
// When values are of different data type then first both values are converted into same data type and then comapred
console.log("2 > 1:", "2" > 1);

console.log("true == 1:", true == 1); // True
console.log("true == 1:", false == 1); // False

let xNumber = 0;
console.log("Boolean type of xNumber:", Boolean(xNumber));
let xstring = "0";
console.log("Boolean type of xstring:", Boolean(xstring));
console.log("xNumber == xstring:", xNumber == xstring);

console.log("0 == false", 0 == false)// Simple equality (==)
console.log("0 === false", 0 === false)// Strict equality (===)
