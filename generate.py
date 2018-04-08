import random
import argparse
import pickle
from collections import defaultdict


def read(path_to_file):
    with open(path_to_file, 'rb') as f:
        def_dict = pickle.load(f)
        return def_dict


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


parser = argparse.ArgumentParser()
parser.add_argument('--output', dest='link_to_save', help='path to file to save')
parser.add_argument('--model', required=True, dest='link_to_load', help='path to load to save')
parser.add_argument('--seed', required=True, dest='first_word', help='the word from which we start')
parser.add_argument('--length', required=True, dest='length', help='length of the sentence', type=int)
args = parser.parse_args()

answer = generate(args.first_word, args.length, read(args.link_to_load))
if args.link_to_save:
    with open(args.link_to_save) as file:
        file.write(answer)
else:
    print(answer)
