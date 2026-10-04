# 4.3: Manipulate Strings with Methods Exercises
# ----------------------------------------------
# Exercise 1;
# Write a program that converts the following strings to lowercase:
# "Animals", "Badger", "Honey Bee", "Honey Badger".
# Print each lowercase string on a separate line.
var0 = "Animals"
var1 = "Badger"
var2 = "Honey Bee"
var3 = "Honey Badger"
print("""This is Exercise 1.
The goal of this exericse is to convert the following strings to lowercase,
and print them on a separate line;
'Animals'
'Badger'
'Honey Bee'
'Honey Badger'
---
The following are the Variables and their values;
var0 = 'Animals'
var1 = 'Badger'
var2 = 'Honey Bee'
var3 = 'Honey Badger'
---

The following is the requested output of the exercise 1;""")
# Setting of method variables
var0E1 = var0.lower()
var1E1 = var1.lower()
var2E1 = var2.lower()
var3E1 = var3.lower()
print("Variable0 lowercase = " + var0E1)
print("Variable1 lowercase = " + var1E1)
print("Variable2 lowercase = " + var2E1)
print("Variable3 lowercase = " + var3E1)
# Note; I'm aware that I can modify the original variable utilizing the following code;
# var0 = var0.lower()
# But the exercise didn't explicitly state that I re-assign the variable with the new change
print('----------------------------------------------')
print('')
# Exercise 2;
# Repeat exercise 1, but convert each string to uppercase instead of lowercase.
# Setting of method variables
print("""This is Exercise 2.
The goal of this exericse is to convert the strings to uppercase instead of lowercase,
and print them on a separate line;""")
var0E2 = var0.upper()
var1E2 = var1.upper()
var2E2 = var2.upper()
var3E2 = var3.upper()
print("The following is the requested output of the exercise 2;")
print("Variable0 uppercase = " + var0E2)
print("Variable1 uppercase = " + var1E2)
print("Variable2 uppercase = " + var2E2)
print("Variable3 uppercase = " + var3E2)
print('----------------------------------------------')
print('')
# Exercise 3;
# Write a program that removes whitespace from the following strings,
# then print out the strings with the whitespace removed:
# Setting of exercise variables;
string1 = "    Filet Mignon"
string2 = "Brisket    "
string3 = "  Cheeseburger   "
print("""This is Exercise 3.
The goal of this exericse is to write a program that removes whitespace from the following strings,
then print out the strings with the whitespace removed:;""")
print("string1 = " + string1)
print("string2 = " + string2)
print("string3 = " + string3)
print('')
print("The following is the requested output of the exercise 2;")
stripString1 = string1.lstrip()
stripString2 = string2.rstrip()
stripString3 = string3.strip()
print("string1 = " + stripString1)
print("string2 = " + stripString2)
print("string3 = " + stripString3)
print('----------------------------------------------')
print('')
# Exercise 4;
# Write a program that prints out the result of .startswith("be") on each of the following strings:
# string1 = "Becomes"
# string2 = "becomes"
# string3 = "BEAR"
# string4 = "  bEautiful"
print("""This is Exercise 4.
Write a program that prints out the result of .startswith('be') on each of the following strings:
string1 = 'Becomes'
string2 = 'becomes'
string3 = 'BEAR'
string4 = '  bEautiful'""")
# Setting of variables
# Note: I am changing the variable names from 'stringx' to 'strEx4x'
strEx40 = "Becomes"
strEx41 = "becomes"
strEx42 = "BEAR"
strEx43 = " bEautiful"
print('')
print("Here is the output of the above variables;")
print("'Becomes' = ")
print(strEx40.startswith("be"))
print('')
print("'becomes' = ")
print(strEx41.startswith("be"))
print('')
print("'BEAR' = ")
print(strEx42.startswith("be"))
print('')
print("'  bEautiful' = ")
print(strEx43.startswith("be"))
print('----------------------------------------------')
print('')
# Exercise 5;
# Using the same four strings from exercise 4, write a program that uses string methods to alter each string so that .startswith("be") returns True for all of them.
# Note: Since the variables are already set in the previous exercise, I will not need to set them again here
# Note(cont.): But will need to set new variables to save changes
# Note(concl.): Due to 'strEX41' already being lowercase, I will not need to modify it
strEx40New = strEx40.lower()
strEx42New = strEx42.lower()
strEx43Chg = strEx43.lstrip()
strEx43New = strEx43Chg.lower()
print("""This is Exercise 5.
Using the same four strings from exercise 4,
write a program that uses string methods to alter each string so that .startswith("be") returns True for all of them.""")
print('')
print("Here is the output of the above variables;")
print("'Becomes' = ")
print(strEx40New.startswith("be"))
print('')
print("'becomes' = ")
print(strEx41.startswith("be"))
print('')
print("'BEAR' = ")
print(strEx42New.startswith("be"))
print('')
print("'  bEautiful' = ")
print(strEx43New.startswith("be"))
print('----------------------------------------------')
