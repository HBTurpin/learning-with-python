


def part_1():
    with open('F:\\Github\\learning-with-python\\challenges\\adventofcode.com\\2022\\day2-input.txt') as file:
        lines = [line.rstrip() for line in file]
    score = 0
    
    #A/X Rock
    #B/Y Paper
    #C/Z Scissors
    winning_logic = [["A","Y"],["B","Z"],["C","X"]]
    drawing_logic = [["A","X"],["B","Y"],["C","Z"]]
    scores = {"X" : 1, "Y" : 2 , "Z" : 3}
    for line in lines:
        comparison = line.split(" ")
        print(comparison)
        if comparison in winning_logic:
            score += 6 
        elif comparison in drawing_logic:
            score += 3
        score += scores[comparison[1]]
    print(score)
 
part_1()



def part_2():
    with open('F:\\Github\\learning-with-python\\challenges\\adventofcode.com\\2022\\day2-input.txt') as file:
        lines = [line.rstrip() for line in file]
    score = 0
    
    winning_logic = [["A","Y"],["B","Z"],["C","X"]]
    drawing_logic = [["A","X"],["B","Y"],["C","Z"]]

    replace_logic = {
        "Z" : {"A" : "Y", "B" : "Z", "C" : "X"}, #wIN
        "Y" : {"A" : "X", "B" : "Y", "C" : "Z"}, #DRAW
        "X" : {"A" : "Z", "B" : "X", "C" : "Y"} #LOSE
    }

    scores = {"X" : 1, "Y" : 2 , "Z" : 3}
    for line in lines:
        comparison = line.split(" ")
        # print("1st comparison", comparison)
        comparison_2 = [comparison[0], replace_logic[comparison[1]][comparison[0]]]
        # print("2nd comparison", comparison_2)
        if comparison_2 in winning_logic:
            score += 6 
        elif comparison_2 in drawing_logic:
            score += 3
        score += scores[comparison_2[1]]
    print(score)
 
part_2()