
from sys import maxsize


letters_dictionary = {}
def generateLettersRank():
    global letters_dictionary
    with open('other\\5letterwords.txt') as file:
        words = [line.rstrip() for line in file]
    for word in words:
        for letter in word:
            if letter in letters_dictionary:
                letters_dictionary[letter][0] += 1
            else:
                letters_dictionary[letter] = [1, 0, 0]
    
    #rank letters
    letters_dictionary = dict(sorted(letters_dictionary.items(), key=lambda item: item[1][0]))
    rank = 0
    max_rank = 0
    for letter in letters_dictionary:
        letters_dictionary[letter][1] = rank
        if rank == 25:
            max_rank = letters_dictionary[letter][0]
        rank += 1

    for letter in letters_dictionary:
        letters_dictionary[letter][2] = letters_dictionary[letter][0]/max_rank
        
    print(letters_dictionary)

generateLettersRank()

def getLetterRank(letter):
    return letters_dictionary[letter][2]

def getLetterCount(letter, word):
    count = 0
    for l in word:
        if l == letter:
            count += 1
    return count

def getWordRank(word):
    points = 0
    for letter in word:
        points += getLetterRank(letter)/max(1,(getLetterCount(letter, word)*1.2)+1)
    return points

words_dictionary = {}
def generateWordRanks():
    global words_dictionary
    with open('other\\5letterwords.txt') as r:
        words = [line.rstrip() for line in r]

    for word in words:
        words_dictionary[word] = getWordRank(word)
    words_dictionary = dict(sorted(words_dictionary.items(), key=lambda item: item[1], reverse=True))

    print(words_dictionary)

    with open("other\\5letterwords_ranked.txt", 'w') as w:
        for word, rank in words_dictionary.items():
            w.write(word+", "+str(rank)+"\n")
        w.close()


generateWordRanks()