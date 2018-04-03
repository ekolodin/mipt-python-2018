def check_word(word, lowercase=False):
    for letter in word:
        if not letter.isalpha():
            word = word.replace(letter, '')

    if lowercase:
        word = word.lower()
    return word


def write(def_dict):
    for dict_next in def_dict:
        print(dict_next, len(def_dict[dict_next]), sep='\n')  # the key word and size of sub_dictionary
        for word in def_dict[dict_next]:
            print(word, def_dict[dict_next][word])  # second word in collocation and its frequency


def read(path_to_file='input.txt'):
    with open(path_to_file) as path:
        file = path.read().split('\n')
        def_dict = defaultdict(defaultdict)

        i = 0
        while i < len(file):
            i += 1
            temp_dict = defaultdict(int)
            for j in range(int(file[i])):
                temp_dict[file[i + j + 1].split()[0]] = int(file[i + j + 1].split()[1])

            def_dict[file[i - 1]] = temp_dict
            i += (int(file[i]) + 1)

        return def_dict


def make_dict(file_name='input.txt'):
    with open(file_name) as file:
        def_dict = defaultdict(defaultdict)  # dict() -> dict() -> frequency
        last_word = ''

        for line in file:
            words = line.split()
            corrected_words = []
            for word in words:
                corrected_words.append(check_word(word))

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


link_to_load = ''
link_to_save = ''
lowercase = False
while True:
    cmnd = input().split()
    if cmnd[0] == 'exit':
        break
    elif cmnd[0] == '--input-dir':
        link = cmnd[1]
    elif cmnd[0] == '--model':
        link_to_save = cmnd[1]
    elif cmnd[0] == '--lc':
        lowercase = True
    elif cmnd[0] == '--help':
        print('print "exit" to finish')
