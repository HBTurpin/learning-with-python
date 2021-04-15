midterm = int(input("Enter your score for the midterm (out of 20):"))
assignment1 = int(input("Enter your score for the assignment 1 (out of 15):"))
assignment2 = int(input("Enter your score for the assignment 2 (out of 15):"))
course = int(input("Enter your score for the course (out of 100):"))


exam = course - assignment1 - assignment2 - midterm

if exam <= 50:
  print("You will need to get "+str(exam)+" out of 50 on the final")
else:
  print("Your desired grade is not possible")