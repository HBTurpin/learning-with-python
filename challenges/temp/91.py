def parser(email):
    for i in range(len(email)):
        name = email[:email.find("@")]
        domain = email[email.find("@") + 1:]
        return [name, domain]


# main program
data = input("Enter and email address: ")  # ask for the address
result = parser(data)
print("The username is:", result[0], "and the domain is:", result[1])
