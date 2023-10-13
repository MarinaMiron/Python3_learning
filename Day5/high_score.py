student_scores = input("Input a list of student scores: ").split() 
#example: 78 65 89 86 55 91 64 89 , 150 142 185 120 171 184 149 199
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
high_score = 0
for score in student_scores:
  if score > high_score:
    high_score = score
print(f"The highest score in the class is: {high_score}")