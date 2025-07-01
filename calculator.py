# let's make a scientific calculator
# lessons learnt: don depend on recursion instead use while loop and break / continue

def user_inputs():
  while True: 
    try: 
      num1 = float(input("enter num1: "))
      num2 = float(input("enter num2: "))
      print("operators are + - / *")
      operator = input("operator: ")
      return num1, num2, operator

    except:
      print("invalid input numbers.. try again")


def validify_inputs(num1,num2,operator):
  if operator not in ['+','-','*','/']:
    return False
  else:
    return True

def calculate(num1,num2,operator): 
  if operator == "+":
    return num1 + num2
  elif operator == "-": 
    return num1 - num2
  elif operator == "*": 
    return num1 * num2
  elif operator == "/": 
    try:
      sum = num1 / num2
      return sum
    except:
      print("Error: Dividing by zero!")

def main():
    while True:
        num1, num2, operator = user_inputs()
        validity = validify_inputs(num1, num2, operator)

        while not validity:
            print("Incorrect inputs.. try again")
            num1, num2, operator = user_inputs()
            validity = validify_inputs(num1, num2, operator)

        result = calculate(num1, num2, operator)
        if result != None:
          print(f"{num1} {operator} {num2} = {result}")

        while True:
            try_again = input("Would you like to try again? (Yes / No): ").strip().lower()
            if try_again in ['yes', 'y']:
                break  
            elif try_again in ['no', 'n']:
                print("Thanks for using our calculator.")
                return  
            else:
                print("Please enter 'Yes' or 'No'.")


if __name__ == "__main__":
    main()