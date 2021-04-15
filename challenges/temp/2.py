

attempts = 0

while attempts < 3:
  password = input("Enter the password:")
  attempts+=1
  if password == "test123":
    print("Password accepted, you are in")
    print("Welcome to our system")
    break
  else:
    if attempts >= 3:
      print("You are out of tries - locked out")
      break
    else:
      print("Incorrect password, you have", str(3 - attempts), "left")




