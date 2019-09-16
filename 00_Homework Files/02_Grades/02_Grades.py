# Author: Nate K
# Date of Creation: 09/16/2019
# Date of Last Edit: 09/16/2019
# If-Statement Grading Homework
# SOURCES: 

# On my honor, I have neither given nor received unauthorized aid.
# Signed: NK 09/16/2019
# *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*

grade_UR = float(input("\n\n\n\n\n\nPlease input your grade (0-5):\n"))

if grade_UR > 5 or grade_UR < 0:
	print("\n\nERROR: Expected input between 0-5, please restart the program.")
elif grade_UR >= 4.85 and grade_UR <= 5:
	print("\n\nGRADE RECEIVED: A+")
elif grade_UR >= 4.65 and grade_UR < 4.85:
	print("\n\nGRADE RECEIVED: A")
elif grade_UR >= 4.5 and grade_UR < 4.65:
	print("\n\nGRADE RECEIVED: A-")
elif grade_UR >= 4.2 and grade_UR < 4.5:
	print("\n\nGRADE RECEIVED: B+")
elif grade_UR >= 3.85 and grade_UR < 4.2:
	print("\n\nGRADE RECEIVED: B")
elif grade_UR >= 3.5 and grade_UR < 3.85:
	print("\n\nGRADE RECEIVED: B-")
elif grade_UR >= 3.2 and grade_UR < 3.5:
	print("\n\nGRADE RECEIVED: C+")
elif grade_UR >= 2.85 and grade_UR < 3.2:
	print("\n\nGRADE RECEIVED: C")
elif grade_UR >= 2.5 and grade_UR < 2.85:
	print("\n\nGRADE RECEIVED: C-")
elif grade_UR >= 2 and grade_UR < 2.5:
	print("\n\nGRADE RECEIVED: D+")
elif grade_UR >= 1.5 and grade_UR < 2:
	print("\n\nGRADE RECEIVED: D")
elif grade_UR >= 1 and grade_UR < 1.5:
	print("\n\nGRADE RECEIVED: D-")
elif grade_UR >= 0 and grade_UR < 1:
	print("\n\nGRADE RECEIVED: F")