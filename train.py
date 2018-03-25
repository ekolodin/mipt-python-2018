def IsLetter(letter_):
    return 'a' <= letter_ <= 'z' or 'A' <= letter_ <= 'Z'


def CheckWord(word_, lowercase = False):
    for letter_ in word_:
        if not IsLetter(letter_):
            word_ = word_.replace(letter_, '')

    if lowercase:
        word_ = word_.lower()
    return word_


def Write(dict_):
    for dict_next_ in dict_:
        print(dict_next_, len(dict_[dict_next_]), sep='\n')  # the key word and size of sub_dictionary
        for word_ in dict_[dict_next_]:
            print(word_, dict_[dict_next_][word_])  # second word in collocation and its frequency


def Read(link_to_file_='input.txt'):
    file_ = open(link_to_file_).read().split('\n')  # need try block !!!
    dict_ = dict()

    i = 0
    while i < len(file_):
        i += 1
        temp_dict_ = dict()
        for j in range(int(file_[i])):
            temp_dict_[file_[i + j + 1].split()[0]] = file_[i + j + 1].split()[1]

        dict_[file_[i - 1]] = temp_dict_
        i += (int(file_[i]) + 1)

    return dict_


def MakeDict(link_to_file_='input.txt'):
    file_ = open(link_to_file_)  # need try block !!!
    dict_ = dict()  # dict() -> dict() -> frequency

    last_word_ = ''

    for line_ in file_:
        words_ = line_.split()
        corrected_words_ = []
        for word_ in words_:
            corrected_words_.append(CheckWord(word_))

        for i in range(len(corrected_words_) - 1):
            if i == 0:
                if last_word_ in dict_:
                    if corrected_words_[0] in dict_[last_word_]:
                        dict_[last_word_][corrected_words_[0]] += 1
                    else:
                        dict_[last_word_][corrected_words_[0]] = 1
                else:
                    dict_[last_word_] = dict()
                    dict_[last_word_][corrected_words_[0]] = 1

            if corrected_words_[i] in dict_:
                if corrected_words_[i + 1] in dict_[corrected_words_[i]]:
                    dict_[corrected_words_[i]][corrected_words_[i + 1]] += 1
                else:
                    dict_[corrected_words_[i]][corrected_words_[i + 1]] = 1
            else:
                dict_[corrected_words_[i]] = dict()
                dict_[corrected_words_[i]][corrected_words_[i + 1]] = 1

            last_word_ = corrected_words_[len(corrected_words_) - 1]

    del dict_['']
    return dict_


link_to_load_ = ''
link_to_save_ = ''
lowercase = False
while True:
    cmnd_ = input().split()
    if cmnd_[0] == 'exit':
        break
    elif cmnd_[0] == '--input-dir':
        link = cmnd_[1]
    elif cmnd_[0] == '--model':
        link_to_save = cmnd_[1]
    elif cmnd_[0] == '--lc':
        lowercase = True
    elif cmnd_[0] == '--help':
        print('print "exit" to finish')
