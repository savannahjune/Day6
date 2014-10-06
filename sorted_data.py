def main():
    sorted_scores = {}
    scores = open('scores.txt')
    for line in scores:
        line = line.rstrip()
        line = line. split(':')
        sorted_scores[line[0]] = line[1]
        sorted_scores_keys = sorted(sorted_scores.keys())
    for key in sorted_scores_keys:
        value = sorted_scores[key]
        print "Restaurant %s is rated at %s" % (key, value)  

if __name__ == '__main__':
    main()