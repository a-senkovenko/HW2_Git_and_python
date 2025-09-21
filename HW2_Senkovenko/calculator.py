def subtraction(val1, val2):
    return val1 -  val2

def addition(val1, val2):
    return val1 + val2

def multiplication(val1, val2):
    return val1 * val2

def division(val1, val2):
    if val2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return val1 / val2


operators = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}

def main():
    print("Hello! \nType exit to finish calculations")

    while True:
        check = input("Enter your expression: \n")
        
        if "exit" in check:
            print("Program closed")
            break

        try:
            line = check.split()    
            
            if len(line) != 3:
                raise ValueError("Incorrect number of values, check your input: value1 operator value2")
                
            val1 = float(line[0])
            oper = line[1]
            val2 = float(line[2])

            if oper not in operators:
                raise KeyError (f"Used unknown operator, supported operators are: {tuple(operators.keys())}")

            result = operators[oper](val1, val2)

            print(f"Result: {result}")

        except ValueError as valerr:
            print(f"Value Error: {valerr}")
        except KeyError as keyerr:
            print(f"Key Error: {keyerr}")
        except ZeroDivisionError as zeroerr:
            print(f"Math Error: {zeroerr}")
        except Exception as exc:
            print(f"Unexpected Error: {exc}")

if __name__ == "__main__":
    main()
