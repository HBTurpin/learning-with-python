def cleaner(list1):
    for i in range(len(list1)):
        if list1[i] in ["a","the","and"]:
            list1[i] = "X"



pets = ["the", "dog", "and", "a", "cart"]
cleaner(pets)
print(pets)

movies = ["I", "watched", "a", "funny", "and", "good", "movie"]
cleaner(movies)
print(movies)
