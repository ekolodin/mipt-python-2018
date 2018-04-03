import random


def generate(start, length, def_dict):
    sentence = start
    curr_len = 1
    word = start
    while curr_len < length:
        frequencies = list(def_dict[word].values())
        need = random.choice(frequencies)
        for j in def_dict[word].keys():
            if def_dict[word][j] == need:
                word = j
                break

        sentence += ' ' + word
        curr_len += 1

    return sentence


output_file = ''
link_to_save = ''
while True:
    cmnd = input().split()
    if cmnd[0] == 'exit':
        break
    elif cmnd[0] == '--output':
        output_file = cmnd[1]
    elif cmnd[0] == '--model':
        link_to_save = cmnd[1]
    elif cmnd[0] == '--seed':
        start = cmnd[1]
    elif cmnd[0] == '--length':
        length = int(cmnd[1])
    elif cmnd[0] == '--help':
        print('print "exit" to finish')
