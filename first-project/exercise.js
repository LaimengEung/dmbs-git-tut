// Number Range
const prompt = require('prompt-sync')();
const user_num = prompt("Please input the number: ");
if (user_num > 0) {
    console.log(user_num, "is Positive!");
} else if (user_num < 0) {
    console.log(user_num, "is Negative!");
} else {
    console.log(user_num, "is 0!");
}