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
    with open(link_to_file, 'wb') as file:
        pickle.dump(def_dict, file)


def make_dict(lowercase=False, file_name='input.txt'):
    with open(file_name) as file:
        def_dict = defaultdict(defaultdict)  # dict() -> dict() -> frequency
        last_word = ''

        for line in file:
            words = line.split()
            corrected_words = []
            for word in words:
                corrected_words.append(check_word(word, lowercase))

            for i in range(len(corrected_words) - 1):
                if i == 0:
                    if corrected_words[0] in def_dict[last_word]:
                        def_dict[last_word][corrected_words[0]] += 1
                    else:
                        def_dict[last_word][corrected_words[0]] = 1

                if corrected_words[i + 1] in def_dict[corrected_words[i]]:
                    def_dict[corrected_words[i]][corrected_words[i + 1]] += 1
                else:
                    def_dict[corrected_words[i]][corrected_words[i + 1]] = 1

                last_word = corrected_words[len(corrected_words) - 1]

        del def_dict['']
        return def_dict


lower = False

parser = argparse.ArgumentParser()
parser.add_argument('--input-dir', required=True, dest='link_to_load', help='path to file to load')
parser.add_argument('--model', required=True, dest='link_to_save', help='path to file to save')
parser.add_argument('--lc', help='reduction to lowercase')

args = parser.parse_args()
if args.lc:
    lower = True

write(make_dict(lower, args.link_to_load), args.link_to_save)
