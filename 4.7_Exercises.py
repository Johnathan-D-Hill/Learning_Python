# 4.7 - Streamline Your Prints Exercises
# --------------------------------------
#
# Exercise 1
# ---------------------------------------------------------------------------
# A.) Create a float object named 'weight'
# B.) Assign the value of '0.2' to the float object named 'weight'
# C.) Create a string object named 'animal'
# D.) Assign the value of 'newt' to the string object named 'animal'
# E.) Finally, print these objects using the following string concatenation;
# ->>> '0.2 kg is the weight of the newt.'
# ---------------------------------------------------------------------------
weight = float(0.2)
weightStr = str(weight)
animal = str("newt")
print("""# A.) Create a float object named 'weight'
# B.) Assign the value of '0.2' to the float object named 'weight'
# C.) Create a string object named 'animal'
# D.) Assign the value of 'newt' to the string object named 'animal'
# E.) Finally, print these objects using the following string concatenation;
# ->>> '0.2 kg is the weight of the newt.'
Next will be the displayed output;
""")
print(weightStr + " kg is the weight of the " + animal)
print("This is the end of exercise 1")
print("")
#
# Exercise 2
# ---------------------------------------------------------------------------
# Display the same string using .format() and empty{} placeholders.
# ---------------------------------------------------------------------------
weight = float(0.2)
animal = str("newt")
print("""This 2nd program requests the following;
Display the same string using .format() and empty{} placeholders.
""")
print("{} kg is the weight of the {}".format(weight, animal))
print("This is the end of exercise 2")
print("")
#
# Exercise 3
# ---------------------------------------------------------------------------
# Display the same string using an f-string
# ---------------------------------------------------------------------------
weight = float(0.2)
animal = str("newt")
print("""This 3rd program requests the following;
Display the same string using an f-string.
""")
print(f"{weight} kg is the weight of the {animal}")
print("This is the end of exercise 3")
print("")
