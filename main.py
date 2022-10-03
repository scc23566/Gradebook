last_semester_gradebook = [["Chemistry", 75], ["British Literature", 80]]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

gradebook[-1][-1] = 93 + 5
print(gradebook)

gradebook[2].remove(85)

gradebook[2].append("Pass")
#print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)