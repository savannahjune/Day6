"""
Program that opens a file on the command line and counts how many times 
each space seperated word occurs in that file.
"""
# from sys import argv
# script, filename = argv

# make each word a key, and how many times it occurs a value

def remove_punctuation(line):
    punctuation = "!\"#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
    line_no_punc = ""
    for letter in line:
        if letter not in punctuation:
            line_no_punc += letter
    return line_no_punc

def read_data_from_file(filename):
    dict_of_words = {}
    text = open(filename)
    for line in text:
        line = line.strip().lower()
        line = remove_punctuation(line)
        words = line.split() 
        for word in words:
            if word not in dict_of_words:
                dict_of_words[word] = 1
            else:
                dict_of_words[word] += 1
        # for word in dict_of_words:
        #     print word + " " + str(dict_of_words[word])  
    # print dict_of_words
    return dict_of_words

def sort_data(dictionary):
    # for key in sorted(dictionary.keys()):
    #     value = dictionary[key]
    #     print key, value
    # print dictionary
    opp_d = {}
    for key, value in dictionary.iteritems():
        if value not in opp_d:
            opp_d[value] = [key]
        else: 
            opp_d[value].append(key)
    # print opp_d
    opp_d_keys = opp_d.keys()
    opp_d_keys.reverse()
    # print opp_d_keys 
    for key in opp_d_keys:
        value = opp_d[key]
        print key, value

def main():
    dict_of_words = read_data_from_file('shorttext.txt')
    sort_data(dict_of_words)


if __name__ == '__main__':
    main()



