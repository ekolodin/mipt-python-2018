from collections import defaultdict
import argparse
import pickle


def check_word(word, lowercase=False):
    for letter in word:
        if not letter.isalpha():
            word = word.replace(letter, '')

    if lowercase:
        word = word.lower()
    return word


def write(def_dict, link_to_file):
    temp_dict = defaultdict(dict)
    for i in def_dict:
        temp_dict[i] = dict(def_dict[i])
    with open(link_to_file, 'wb') as file:
        pickle.dump(temp_dict, file)


def make_dict(lowercase, stdin, file_name='input.txt'):
    full_text = []
    if not stdin:
        with open(file_name) as file:
            for line in file:
                words = line.split()
                for word in words:
                    full_text.append(check_word(word, lowercase))
    else:
        full_text = input().split()

    def_dict = defaultdict(lambda: defaultdict(int))  # defaultdict() -> defaultdict() -> frequency
    for i in range(len(full_text) - 1):
        def_dict[full_text[i]][full_text[i + 1]] += 1

    return def_dict


lower = False

parser = argparse.ArgumentParser()
parser.add_argument('--input-dir', dest='link_to_load', help='path to file to load')
parser.add_argument('--model', required=True, dest='link_to_save', help='path to file to save')
parser.add_argument('--lc', help='reduction to lowercase')

args = parser.parse_args()
if args.lc:
    lower = True

if args.link_to_load:
    write(make_dict(lower, False, args.link_to_load), args.link_to_save)
else:
    write(make_dict(lower, True), args.link_to_save)
