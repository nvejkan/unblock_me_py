from ast import literal_eval
fin = open('test30.log')
board_list = []
count = 1
for i in fin:
    if count > 1:
        board_list.append(literal_eval(i))
    else:
        pass
    count = count + 1
