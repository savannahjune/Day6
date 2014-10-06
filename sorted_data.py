def main():
    sortedscores = {}
    scores = open('scores.txt')
    for line in scores:
        line = line.rstrip()
        line = line. split(':')
        sortedscores[line[0]] = line[1]
    print sortedscores

if __name__ == '__main__':
    main()