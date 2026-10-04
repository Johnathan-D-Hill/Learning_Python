# 4.4 Exercises: Interact with User Input
# ---------------------------------------

# Exercise 1.
# Write a program that takes input from the user and displays that input back.
# ----
prompt = """This is Exercise #1;
What is today's date? """
exerResp1 = input(prompt)
print("You have entered: " + exerResp1)
print('')
# ----

# Exercise 2.
# Write a program that takes input from the user and displays the input in lowercase.
# ----
prompt = """This is Exercise #2;
Please enter today's date in all capital letters: """
exerResp2 = input(prompt)
exerResp2a = exerResp2.lower()
print("You have entered: " + exerResp2a)
print('')
# ----

# Exercise 3.
# Write a program that takes input from the user and displays the number of characters in the input.
# ----
prompt = """This is Exercise #3;
I will tell you the number of characters you enter,
Type what ever you like, user: """
exerResp3 = input(prompt)
print("The number of characters you've type are: ")
print(len(exerResp3))
# ----
