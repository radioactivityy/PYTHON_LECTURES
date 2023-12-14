#  Create a Python program that takes your age as input, stores it in a variable.
# and then prints out a message saying "You are [age] years old."

# Step 1: Take user input
age = input("Enter your age: ")

# Step 2: Convert the input to an integer

try:
    age_input = int(age)
# Step 3: Print out a message
# The f-string is used to format the output, and it allows us to include the value. 
    print(f"I am {age} years old.")
    
#This way, the program won't crash if the user 
# enters something that is not a valid integer.
except ValueError:
    print("Invalid input.")
