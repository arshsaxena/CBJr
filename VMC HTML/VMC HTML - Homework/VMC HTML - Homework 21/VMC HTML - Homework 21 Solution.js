let welcome = "Welcome! You will be asked some information. Please fill it.";
alert(welcome);
console.log(welcome);

name = prompt("What is your name?");
console.log("Name:", name);

age = prompt("What is your age?");
console.log("Age:", age);

agemsg = (`You are roughly ${age*365} days old.`);
alert(agemsg);
console.log(name, "is roughly", age*365, "days old.");

let welrect = "Now, you will be asked some values for finding area of a rectangle. Please fill them.";
alert(welrect);
console.log(welrect);

alert("Formula = Length x Breadth")
console.log("Formula = Length x Breadth")

lrect = prompt("What is the length of rectangle?");
console.log("Length =", lrect);

brect = prompt("What is the breadth of rectangle?");
console.log("Breadth =", brect);

arectmsg = (`Area of rectangle is ${lrect*brect} sq. units.`);
alert(arectmsg);
console.log("Area =", lrect*brect, "sq. units");

let weltri = "Now, you will be asked some values for finding area of a triangle. Please fill them.";
alert(weltri);
console.log(weltri);

alert("Formula = 1/2 x Length of base x Height")
console.log("Formula = 1/2 x Length of base x Height")

ltri = prompt("What is the length of base of triangle?");
console.log("Length of base =", ltri);

htri = prompt("What is the height of triangle?");
console.log("Height =", htri);

atrimsg = (`Area of triangle is ${0.5*ltri*htri} sq. units.`);
alert(atrimsg);
console.log("Area =", 0.5*ltri*htri, "sq. units");

thanks = "Thank you for filling the information and values asked."
console.log(thanks);