# You are given a 2d matrix which consist of the following symbols ".", "#", "", where "." represent free cell, "#" represent a obstacle, "" denotes shape. Your task is to find out the minimum obstacle to remove from the matrix so that the shapes falls down to the bottom.

# Test Case:

# [["*", "*", "*", "*"],
# ["#", "*", ".", "*"],
# [".", ".", "#", "."],
# [".", "#", ".", "#"] ]

# Output = 4

# Simulation:

# Initial matrix:

# [["*", "*", "*", "*"],
# ["#", "*", ".", "*"],
# [".", ".", "#", "."],
# [".", "#", ".", "#"] ]

# After removing matrix[1][0]

# [[".", ".", ".", "."],
# ["*", "*", "*", "*"],
# [".", "*", "#", "*"],
# [".", "#", ".", "#"] ]

# After removing matrix[2][2], matrix[3][1], matrix[3][3], we get

# [[".", ".", ".", "."],
# [".", ".", ".", "."],
# ["*", "*", "*", "*"],
# [".", "*", ".", "*"] ]

# which will give us the output 4