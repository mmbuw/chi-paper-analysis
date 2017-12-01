# convert list of words to matrix

ofh = open("words.tsv", "w")

allWords = set()

fileWords = dict()
for line in open("words.txt"):
    fs = line.rstrip("\n").split()
    if len(fs)==1:
        continue
    words = fs[1].split(",")
    fileId = fs[0].split('.')[0]
    allWords.update(words)
    fileWords[fileId] = words

wordToIndex = dict([(word, idx) for idx, word in enumerate(allWords)])

for fileId, words in fileWords.iteritems():
    vec = [0] * len(allWords)
    for w in words:
        idx = wordToIndex[w]
        vec[idx] = 1
    ofh.write("%s\t%s\n" % (fileId,"\t".join([str(x) for x in vec])))

print "Columns/Words: %d" % len(allWords) 
print "Documents/Lines: %d" % len(fileWords) 
