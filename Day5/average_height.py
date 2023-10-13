#exaple: 
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
nr_students = 0
average_height = 0
for height in student_heights:
  total_height += height
  nr_students += 1
average_height = round(total_height/nr_students)
print(f"total height = {total_height}")
print(f"number of students = {nr_students}")
print(f"average height = {average_height}")