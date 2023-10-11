username_expected = 'Hugo'
password_expected = 'abc123*'

### Functions

# Example 1:
def validation(username, password):
    while True:
        try:
            input_username = input("Enter your username: ")

            if input_username == username:
                while True:
                    input_password = input("Enter your password: ")

                    if input_password == password:
                        print("Logging in...")
                        break  # Exit the password validation loop if login is successful
                    else:
                        print("Invalid password. Please try again.")
                break  # Exit the username validation loop if login is successful
            else:
                print("Invalid username. Please try again.")
        except Exception as e:
            print(f"A problem occurred: {e}")

validation(username_expected, password_expected)


print("")

# Example 2
num1 = 2
num2 = 4
num3 = 10

def sum_calc(a, b, c):
    return a + b * c

result = sum_calc(num1, num2, num3)
print(result)


# Example 3
# Function to calculate the factorial of a number
# 5! (read as "cinco fatorial") is equal to 5 x 4 x 3 x 2 x 1, which is 120.
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Get user input for the number
number = int(input("Enter a number to calculate its factorial: "))

# Call the function to calculate the factorial
factorial = calculate_factorial(number)

# Display the result
print(f"The factorial of {number} is {factorial}")

