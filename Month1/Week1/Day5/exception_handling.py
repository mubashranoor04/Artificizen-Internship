#6. Write a try/except block that gracefully handles at least three different
# exception types (ValueError, ZeroDivisionError, FileNotFoundError)
try:
    number = int(input("Enter a number: "))
    answer = 100 / number

    with open("example.txt", "r") as file:
        print(file.read())

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

except FileNotFoundError:
    print("The file was not found.")

else:
    print("Program executed successfully.")

finally:
    print("Execution completed.")