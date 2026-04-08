# Python Variables Practice: 30 Tasks
# Instructions: Complete each task by writing the code below the comment.

# --- Level 1: The Basics (Naming & Assignment) ---

# 1. Create a variable named 'city' and assign it the name of your hometown.



city = "Winchester hills"
print("question 1:", city)
# 2. Create a variable 'age' and set it to your age.
age = 35
print("question 2:",age)
# 3. Assign the value 100 to a variable called 'score'.
score = 100
print("question 3:",score)
# 4. Create a variable 'is_sunny' and set it to True.
is_sunny = True
print("question 4: is_sunny",is_sunny)
# 5. Reassign the 'score' variable from task 3 to a new value: 150.
score = 150
print("question 5:",score)
# 6. Create two variables, 'x' and 'y', and assign them both the value 5 on a single line.
x = y = 5
print("question 6: the value of x:",x)
print("question 6.1: the value of y:",y)
# 7. Rename the illegal variable '2_cool' to something valid.
cool_2 = "too cool"
print("question 7:",cool_2)
# 8. Create a variable using snake_case (e.g., user_favorite_color).
User_fullname = "Lehlogonolo"
print("question 8:", User_fullname)
# 9. Swap the values of two variables, a = 10 and b = 20, so a is 20 and b is 10.
a = 10
b = 20
swap = a,b = b,a
print("question 9:", swap)
# 10. Create a variable 'pi' and assign it the value 3.14159.
pi = 3.14159
print("question 10:",pi)

# --- Level 2: Data Types & Conversion ---

# 11. Use the type() function to check the data type of 'age'.
print("question 11:",type(age))
# 12. Create a string 'price_str = "19.99"' and convert it to a float.
price = "19.99"
convert = float(price)
print("question 12;",type(convert))
# 13. Convert the float 9.99 into an integer. 
L=9.99
conversion = int(L)
print("question 13:", conversion)
# 14. Create a variable 'greeting' that combines a string and your 'city' variable.
greeting = (city)
print("question 14:",greeting)
# 15. Use an f-string to print: "I am [age] years old and live in [city]."
print("question 15:", f"I am {age} years old and live in {city}.")
# 16. Create a variable with a long string and use len() to find its length.
full_names = "Lehlogonolo Sylvester Raphiri"
print("question 16:",len(full_names))
# 17. Use input() to store a name in a variable called 'user_name'.
user_name = input('what is your user_name?')
print("question 17: Hi",User_fullname)
# 18. Ask a user for their birth year, convert to int, and calculate their current age.
birth_year = int(input("whats is your birth-year?"))
current_age = (2026 - birth_year)
print("question 18: you are" , current_age)
# 19. Create a boolean variable that checks if 10 is greater than 5.
N = 10>5
print("question 19:", N)
# 20. Create a variable 'nothing' and assign it the value None.
nothing = "none"
print("question 20:", nothing)

# --- Level 3: Basic Math with Variables ---

# 21. Create 'length = 10' and 'width = 5'. Calculate 'area' in a new variable.
# 22. Create 'count = 0'. Increment it by 1 using the += operator.
# 23. Calculate the remainder of 10 / 3 using the modulo operator (%).
# 24. Create 'base = 2' and 'exponent = 3'. Calculate 2 to the power of 3.
# 25. Find the average of three variables: test1, test2, and test3.
# 26. Create 'price = 50'. Calculate a 10% discount and store the final price.
# 27. Convert a 'fahrenheit' variable to 'celsius' using: (F - 32) * 5/9.
# 28. Create 'seconds = 3660'. Convert this into minutes and remaining seconds.
# 29. Use a variable to store the result of 10 // 3 (floor division).
# 30. Create a 'wallet' variable with 100. Subtract three 'purchase' variables from it.