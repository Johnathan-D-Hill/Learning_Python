# 4.6 Review Exercises
# --------------------
# Exercise 1;
# Create a string containing an integer,
# then convert that string into an actual integer object using int().
# Test that your new object is a number by multiplying it by another number,
# and displaying the result.
# --------------------
print("""This first program will take a number you enter,
then multiple that number by 2.""")
userNum0 = input("Please enter a number: ")
userNumInt0 = int(userNum0)
userNumMul0 = userNumInt0 * 2
print("Your input number was: " + userNum0)
print("The multiplication of that number by 2 results in: " + str(userNumMul0))
print("This is the end of program 1.")
#
print("")
# --------------------
# Exercise 2;
# Create a string containing an floating-point number,
# then convert that string into an actual floating-point number object using float().
# Test that your new object is a number by multiplying it by another number,
# and displaying the result.
# --------------------
print("""This second program will take a number you enter,
then multiple that number by 2.""")
userNum1 = input("Please enter a decimal number: ")
userNumInt1 = float(userNum1)
userNumMul1 = userNumInt1 * 2
print("Your input number was: " + userNum1)
print("The multiplication of that number by 2 results in: " + str(userNumMul1))
print("This is the end of program 2.")
#
print("")
# --------------------
# Exercise 3;
# Create a string object and an integer object,
# then display them side by side,
# utilizing a single print function call utilizing str()
# --------------------
print("""This third program will ask you to;
a.) input a number
b.) then display that number as a string object
c.) and then display that number as a integer object.""")
userNum2 = input("Please enter a number: ")
userNumInt2 = int(userNum2)
userNumStr0 = str(userNum2)
print("The number you've entered is; " + "String Object: " + str(userNumStr0) + " Integer Object: " + str(userNumInt2))
print("This is the end of program 3.")
#
print("")
# --------------------
# Exercise 4;
# Write a program using input() function twice;
# Each input() function should request a number from the user
# Then multiply the numbers together
# Finally, display the results
# Note: If the user enters 'x' and 'y' then your program should print the following;
# "The product of x and y is z.0."
# --------------------
print("""This fourth program will ask you to;
a.) input two whole numbers
b.) multiply those two whole numbers
c.) display the results to you.""")
userNum3 = input("Please enter the first number: ")
userNum4 = input("Please enter the second number: ")
userNumInt3 = float(userNum3)
userNumInt4 = float(userNum4)
numTot0 = userNumInt3 * userNumInt4
print("The product of " + str(userNum3) + " and " + str(userNum4) + " is: " + str(numTot0))
print("This is the end of the 4th program.")
