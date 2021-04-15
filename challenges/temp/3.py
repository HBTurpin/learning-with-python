

q1 = input("Do you practice programming weekly?")
q2 = input("Do you attend the Peer Assisted Study Sessions (PASS) weekly?")

if q1 == "yes" and q2 == "yes":
  print("We predict you will pass the course.")
elif q1 == "yes" or q2 == "yes":
  print("We predict you may pass the course.")
else:
  print("We predict you may have difficulty in this course.")



total_score = 0
number_of_scores = 0
while True:
  score = int(input("Enter a score for a free-throw:"))
  if score == -1:
    average_score = total_score/number_of_scores
    print("You scored an average of",average_score,"in all your free throws")
    break
  elif score >= 0:
    total_score += score
    number_of_scores += 1



