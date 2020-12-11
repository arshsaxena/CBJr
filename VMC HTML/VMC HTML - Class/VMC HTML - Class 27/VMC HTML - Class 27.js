// alert("Connected!");

// Conditions
var age = 16;

if (age > 18 && age < 60){
    console.log("Approved");
}
else if (age > 60){
    console.log("Age is more than the required age.");
}
else if (age > 80 && age < 100){
    console.log("Age is much more than the required age.");
}
else{
    console.log("Age is less than the required age.");
}

console.log(1);
console.log(1);
console.log(1);
console.log(1);
console.log(1);
console.log(1);
console.log(1);
console.log(1);
console.log(1);
console.log(1);

// While loop
var count = 0; // initializing condition
while (count < 10){
    console.log("Arsh");
    count++; // same as count = count + 1;
}

count = 0;
while (count < 10){
    console.log("While loop: " + count);
    count++;
}

count = 10;
while (count > 0){
    console.log(count);
    count--;
}

// For loop
for (var count = 0; count < 10; count++){
    console.log("For loop: " + count)
}

count = 10;
for (;count > 0;){
    console.log(count);
    count--;
}

// Same as last code above
// for (var count = 10; count > 0; count--){
//     console.log("For loop: " + count)
// }