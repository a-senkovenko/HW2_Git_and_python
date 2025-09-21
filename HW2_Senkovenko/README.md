# Калькулятор / Calculator

#### _**HomeWork №2.**_


## Description

The calculator is written in Python and performs basic arithmetic operations.

Function  | Description | Contributor
----------------|------------|----------
main()| program loop, input/output, error handling | Alexey Senkovenko (lead)
addition(val1, val2) | val1 + val2 | Alisa Senko
subtraction(val1, val2)| val1 - val2 | Aglaya Tsidulko 
division(val1, val2) | val1 / val2 | Anastasiia Kolos
multiplication(val1, val2)| val1 * val2 | Elizaveta Menshikova

README.md - main text by Alisa Senko, en-translation by Alexey Senkovenko.

## How to run the script
The script is launched from the console. 

1. Clone the repository:
```
git clone <URL>
```
2. Go to the project folder and run the script:
```
python3 calculator.py 
```
or
```
python calculator.py
```
depending on your OS.

### _Example_
```
> python calculator.py
Hello! 
Type exit to finish calculations
Enter your expression:
> 3 * 15
Result: 45.0
Enter your expression:
> 3 / 0
Math Error: Cannot divide by zero
Enter your expression:
> 3 + 15.4
Result: 18.4
Enter your expression: 
> 3.0 + 3.9
Result: 6.9
```
### _Error handling:_
* Input-check that exactly 3 elements are given, separated by a space - two numbers and an operator:
```
Enter your expression: 
> 2 +
Value Error: Incorrect number of values, check your input: value1 operator value2
Enter your expression: 
> 2+3
Value Error: Incorrect number of values, check your input: value1 operator value2
```
* Division by zero:
```
Enter your expression: 
> 3 / 0
Math Error: Cannot divide by zero
```
* Check for the correct input format:
```
Enter your expression: 
> 3,5 + 3,5
Value Error: could not convert string to float: '3,5'
Enter your expression: 
> 4.0 ++ 5
Key Error: "Used unknown operator, supported operators are: ('+', '-', '*', '/')"
Enter your expression: 
> - - 3
Value Error: could not convert string to float: '-'
```
* Unexpected Error

### _How to end the calculations_
To finish your work, type `exit` in the input field :
```
Enter your expression: 
> exit
Program closed
```

## ✨✨Our team!✨✨

![alt text](imgs_Senkovenko/telegram-cloud-photo-size-2-5361908254491407803-y.jpg)
