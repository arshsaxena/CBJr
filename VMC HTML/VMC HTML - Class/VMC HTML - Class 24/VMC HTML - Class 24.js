let message = "Hi Arsh!";
// alert(message);

message = 214;
// alert(message);

// Data types
// Strings
let name = "Arsh! Arsh! Arsh!";
// alert(name);

console.log(message);
console.log(name);

let user = 'Arsh!';
console.log(user);

// alert(`Hi, ${name}`);
// alert(`Hello, ${user}`);
// alert(`Hello, ${2+14}`);
// alert("Hello, ${2+14");


// Numbers
let num = 10;
console.log(num);
num = 10.564;
console.log(num);

num = 14/2;
console.log(num);
num = 22/7;
console.log(num);
num = 10/7;
console.log(num);
num = -10/7;
console.log(num);

num = "Hi"/2;
console.log(num); // NaN = Not a Number

let val = 5;
console.log(val)

// BigInt (2^53-1)
let x = 543224272165453142142521354333312173n;

// Boolean

let isGreater = 4>5;
console.log(isGreater);
let isSmaller = 4<5;
console.log(isSmaller);

// Null
let age = null;

// Undefined
let y;

console.log("Type of name:", typeof name, "-", name);
console.log("Type of message: ", typeof message, "-", message);
console.log("Type of val:", typeof val, "-", val);
console.log("Type of num: ", typeof num, "-", num);
console.log("Type of age:", typeof age, "-", age);
console.log("Type of isGreater: ", typeof isGreater, "-", isGreater);
console.log("Type of y: ", typeof y, "-", y);

console.log("Type of name:", typeof(name), "-", name);

// Ways to interact with the browser
// alert(name);
age = prompt("How are you?");
console.log(age)

age = prompt("How are you?", 24);
console.log(age)

let isBoss = confirm("Are you the boss the company?");
alert(isBoss);
