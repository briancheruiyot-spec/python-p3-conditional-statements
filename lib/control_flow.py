#!/usr/bin/env python3

def admin_login(username, password):
    correct_username = "admin"
    correct_password = "12345"
    
    # Case-insensitive comparison for username
    if username.lower() == correct_username and password == correct_password:
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    # Adjusted conditions based on the tests
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature < 65:
        return "It's a little chilly out there!"
    elif 65 <= temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"


def fizzbuzz(num):
    if num == 0:
        return "FizzBuzz"  # or return None if you prefer to indicate no result

    results = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(i)
    
    return results[-1]  # Return the last value (as per the test cases)


def calculator(operation, num1, num2):
    # Perform basic arithmetic operations
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        print("Invalid operation!")
        return None
