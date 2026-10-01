# String Indexing & String Slicing
# --------------------------------

# Variables
# ---------
flavor = "fig pie"
first_three_letters1 = flavor[0] + flavor[1] + flavor[2]
first_three_letters2 = flavor[-7] + flavor[-6] + flavor[-5]
firThrLetts = first_three_letters1 + " <<<Positive Indexing<<< | >>>Negative Indexing>>> " + first_three_letters2
slice1Pos = flavor[4] + flavor[1] + flavor[2]
slice2Neg = flavor[-3] + flavor[-6] + flavor[-5]
newSlice = slice1Pos + " <<<Positive Indexing<<< | >>>Negative Indexing>>> " + slice2Neg
newSlice2 = flavor[-3:-1] + flavor[-5] + " <<<Negative Slicing<<< | >>>Positive Slicing>>> " + flavor[4] + flavor[1:3]
print("""The following are the set Variables of this program;
    Variable0 = 'flavor'
    Variable1 = 'first_three_letters1'
    Variable2 = 'first_three_letters2'
    Variable3 = 'firThrLetts'
    Variable4 = 'slice1Pos'
    Variable5 = 'slice2Neg'
    Variable6 = 'newSlice'
    Variable7 = 'newSlice2'
    """)

# Testing of output
# -----------------
# flavor[0:3]
#   Output = 'fig'
# flavor[-7:-5]
#   Output = 'fi'
# flavor[-7:-4]
#   Output = 'fig'
# flavor[-7:-0]
#   Output = ''
# flavor[-7:0]
#   Output = ''
# flavor[-7:]
#   Output = 'fig pie'
# flavor[-7:1]
#   Output = 'f'
# flavor[-3:-2]
#   Output = 'p'
# flavor[-3:-1]
#   Output = 'pi'
# flavor[-5]
#   Output = 'g'
# flavor[-3:-1] + flavor[-5]
#   Output = 'pig'

# Outputs (from the above Variables and Values)
# --------------------------------------------
print("These are the Outputs")
print("Part 1 of 2")
print("Variable value for 'flavor' = " + flavor)
print("Variable value for 'first_three_letters1' = " + first_three_letters1)
print("Variable value for 'first_three_letters2' = " + first_three_letters2)
print("Variable value for 'slice1Pos' = " + slice1Pos)
print("Variable value for 'slice2Neg' = " + slice2Neg)
print(" ")
print("Part 2 of 2")
print("First test for Indexing = " + firThrLetts)
print("Second test for Indexing = " + newSlice)
print("Final test of Slicing = " + newSlice2)
