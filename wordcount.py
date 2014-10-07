"""
Program that opens a file on the command line and counts how many times 
each space seperated word occurs in that file.
"""
from sys import argv
scrip, filename = argv

# make each word a key, and how many times it occurs a value
def main():
    dict_of_words = {}
    text = open(filename)
    for line in text:
        line = line.strip()
        words = line.split(' ') 
        for word in words:
            if word not in dict_of_words:
                 dict_of_words[word] = 1
            else:
                dict_of_words[word] += 1
    for word in dict_of_words:
        print word + " " + str(dict_of_words[word])  

if __name__ == '__main__':
    main()