import random


def Generate(start_, len_, dict_):
    sentence = start_
    curr_len_ = 1
    word_ = start_
    while curr_len_ < len_:
        frequencies = list(dict_[word_].values())
        need = random.choice(frequencies)
        for j in dict_[word_].keys():
            if dict_[word_][j] == need:
                word_ = j
                break

        sentence += ' ' + word_
        curr_len_ += 1

    return sentence


while True:
    cmnd_ = input().split()
    if cmnd_[0] == 'exit':
        break
    elif cmnd_[0] == '--output':
        pass
    elif cmnd_[0] == '--model':
        pass
    elif cmnd_[0] == '--seed':
        pass
    elif cmnd_[0] == '--length':
        pass
    elif cmnd_[0] == '--help':
        print('print "exit" to finish')
