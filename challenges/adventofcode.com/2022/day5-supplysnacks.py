import math
import re

def part_1():
    with open('F:\\Github\\learning-with-python\\challenges\\adventofcode.com\\2022\\day5-input.txt') as file:
        lines = [line.rstrip() for line in file]
        lines_box = lines[0:8]
        lines_command = lines[10:]

    boxes = [[] for _ in range(0,9)]
    for line_box in lines_box:
        split = line_box.replace("    ","[ ]").replace("[","").replace("]","")
        split = re.split(r' ', split)
        for column, box in enumerate(split):
            if box != "":
                boxes[column].insert(0, box)
    
    for line_command in lines_command:
        params = re.split(' from | to ', line_command[5:])
        for move in range(int(params[0])):
            box_to_move = boxes[int(params[1])-1].pop()
            boxes[int(params[2])-1].append(box_to_move)

    output = ""
    for column in boxes:
        output += column[-1]
        
    print(boxes, output)
         




def part_2():
    with open('F:\\Github\\learning-with-python\\challenges\\adventofcode.com\\2022\\day5-input.txt') as file:
        lines = [line.rstrip() for line in file]
        lines_box = lines[0:8]
        lines_command = lines[10:]

    boxes = [[] for _ in range(0,9)]
    for line_box in lines_box:
        split = line_box.replace("    ","[ ]").replace("[","").replace("]","")
        split = re.split(r' ', split)
        for column, box in enumerate(split):
            if box != "":
                boxes[column].insert(0, box)
    
    for line_command in lines_command:
        params = re.split(' from | to ', line_command[5:])
        boxes_to_move = boxes[int(params[1])-1][-int(params[0]):]
        print(boxes_to_move)
        for move in range(int(params[0])):
            boxes[int(params[1])-1].pop()
        boxes[int(params[2])-1].extend(boxes_to_move)

    output = ""
    for column in boxes:
        output += column[-1]
        
    print(boxes, output)
         
part_2()
