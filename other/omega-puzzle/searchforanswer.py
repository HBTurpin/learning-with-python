connections = {
    "long" : ["potion", "loiter", "girl", "?"],
    "girl" : ["long", "loiter", "ridge" , "?"],
    "ridge" : ["girl", "loiter", "integral", "grid", "?"],
    "grid" : ["?", "?", "integral", "ridge"],
    "loiter" : ["long", "girl", "ridge", "integral", "titan", "potion"],
    "integral" : ["grid", "ridge", "loiter", "titan", "pinata", "eclipse", "?", "?"],
    "eclipse" : ["integral", "?", "?", "?", "?", "spare", "pinata"],
    "titan" : ["potion", "rotate", "pinata", "integral", "loiter"],
    "potion" : ["long", "loiter", "titan", "rotate", "prop", "?"],
    "prop" : ["potion", "rotate", "?", "?"],
    "rotate" : ["prop", "?", "?", "pinata", "titan", "potion"],
    "pinata" : ["rotate","?", "spare", "eclipse", "integral", "titan"],
    "spare" : ["eclipse", "?", "?", "?", "pinata"],
}

options = {
    "long" : [],
    "girl" : [],
    "ridge" : [],
    "grid" : [],
    "loiter" : [],
    "integral" : [],
    "eclipse" : [],
    "titan" : [],
    "potion" : [],
    "prop" : [],
    "rotate" : [],
    "pinata" : [],
    "spare" : [],
}


def generate_initial_options():
    for word in connections:
        for connection_index, connection in enumerate(connections[word]):
            letters = ""
            for letter in connection:
                if connection == "?":
                    letters = word
                    break
                elif letter in word:
                    letters += letter
            options[word].insert(connection_index,letters)
    print(options)
            
confirmed = options
generate_initial_options()

def generate_connections(word):
    #list of lists....


    potential_options = []
    #for start_connection_index, start_connection in enumerate(options[word]):
    start_connection_index = 0
    #Will need to reorder list/loop through differently if selecting different start point

    for start_letter_index, start_letter in enumerate(options[word][start_connection_index]):
        print(f"starting with connection_index: {start_connection_index}, letter: {start_letter}, letter_index: {start_letter_index}")
        potential_option = []
        for option_index, option in enumerate(options[word]):
            potential_option.insert(option_index,[connections[word][option_index], option])
            
        for connection_index, connection in enumerate(connections[word]):

            print(potential_option[connection_index][1][start_letter_index])
            letter = potential_option[connection_index][1][start_letter_index]
            potential_option[connection_index][1] = letter
            #print(f"The letter for {connection} is {letter}")
            #Remove the letter from other connections, shouldn't be able to have this twice
            start_letter_index = 0
            for letter_option_index, letter_option in enumerate(potential_option):
                #print(f"Removing {letter} from {potential_option[connection_index]}")
                if letter_option_index != connection_index:
                    potential_option[letter_option_index][1] = potential_option[letter_option_index][1].replace(letter, "", 1)
        if potential_option not in potential_options:
            potential_options.append(potential_option)



    
    print(f"_____________POTENTIAL OPTIONS FOR '{word}':_____________")
    for po in potential_options:
        print(po)

generate_connections("integral")

