# convert text to tap sep file in format <document> listOfWords

import glob, re
from os.path import *
from collections import Counter, defaultdict

pattern = re.compile('[\W_]+')

# read the BNC top words
commonWords = set()
for line in open("lemma.al"):
    #5 2186369 a det
    word = line.split()[2]
    commonWords.add(word)
    
# read the whole text into RAM
texts = dict()
wordCounts = defaultdict(int)
inAll = set()
#print "Reading files..."
for fname in glob.glob("raw-text/*.txt"):
    textId = basename(fname)
    words = open(fname).read().split()
    words = [w for w in words if not w.startswith("doi") and not w.startswith("http") and not w.startswith("www") and not "@" in w and not "," in w and not "." in w]
    words = [pattern.sub('', w) for w in words] # remove unprintable chars
    words = [w.lower() for w in words if len(w)>5 and not w[0].isdigit()] # remove short words and numbers

    goodWords = set(words)-commonWords
    # keep only words that appear twice
    #wordCounts = Counter(words)
    #goodWords = [word for word,count in wordCounts.most_common() if count > 1]

    # for each word count in how many texts it appears
    for word in goodWords:
        wordCounts[word] += 1
    texts[textId] = goodWords

# output
minOcc = 5
maxOcc = 800
for textId, wordVec in texts.iteritems():
    words = [w for w in wordVec if maxOcc > wordCounts[w] > minOcc]
    print textId, ",".join(words)

