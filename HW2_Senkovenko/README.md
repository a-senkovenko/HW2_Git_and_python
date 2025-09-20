
# Калькулятор / Calculator

#### _**HomeWork №2.**_


## Описание

Калькулятор написан на языке Python, выполняет базовые арифметические операции. 

Функция  | Описание | Автор
----------------|------------|----------
main()| основной цикл программы, ввод/вывод, разбор выражения, обработка ошибок | Алексей Сенковенко (Тимлид)
addition(val1, val2) | сложение (val1 + val2)| Алиса Сенько
subtraction(val1, val2)| вычитание (val1  val2) | Аглая Цидулко 
division(val1, val2) | деление (val1 / val2)| Анастасия Колос
multiplication(val1, val2)| произведение (val1 * val2)| Елизавета Меньщикова

## Запуск и работа скрипта
Запуск скрипта прозводится из консоли. 

1. Клонировать репозиторий:
```
git clone <URL>
```
2. Перейти в папку проекта и запустить скрипт:
```
python3 calculator.py 
```
или
```
python calculator.py
```
в зависимости от вашей ОС.

### _Пример работы_
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
### _Обработка ошибок:_
* проверка, что введено ровно 3 элемента, разделенных пробелом - два числа и оператор:
```
Enter your expression: 
> 2 +
Value Error: Incorrect number of values, check your input: value1 operator value2
Enter your expression: 
> 2+3
Value Error: Incorrect number of values, check your input: value1 operator value2
```
* деление на ноль:
```
Enter your expression: 
> 3 / 0
Math Error: Cannot divide by zero
```
* корректность формата чисел и операторов:
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
* прочие неожиданные ошибки (Unexpected Error).

### _Завершение работы_
Для завершения работы калькулятора введите в поле для ввода `exit`:
```
Enter your expression: 
> exit
Program closed
```

## ✨✨Наша команда в работе✨✨

![alt text](imgs_Senkovenko/telegram-cloud-photo-size-2-5361908254491407803-y.jpg)

