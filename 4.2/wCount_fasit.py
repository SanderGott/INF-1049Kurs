import os
import matplotlib.pyplot as plt

FILTER = ".,:;!?()[]{}-"

def wordCount(fileName):
    with open(fileName, 'r') as f:
        text = f.read()
        words = text.split()

        result = {}
        for word in words:
            if word in FILTER:
                continue
            if word in result:
                result[word] += 1
            else:
                result[word] = 1



        return result

def mostCommonWords(wordCountDict):
    # 10 most common words. Return as list of tuples
    sortedWords = sorted(wordCountDict.items(), key=lambda x: x[1], reverse=True)
    return sortedWords[:10]



def plotLengthFrequency(wordCountDict):
    # plot the frequency of word lengths
    counts = {}
    words = list(wordCountDict.keys())
    for word in words:
        if len(word) in counts:
            counts[len(word)] += wordCountDict[word]
        else:
            counts[len(word)] = wordCountDict[word]
    
    plt.bar(counts.keys(), counts.values())
    plt.xlabel("Length of word")
    plt.ylabel("Frequency")
    plt.show()
    

    


fileName = os.path.join(os.path.dirname(__file__), "bee.txt")

result = wordCount(fileName)

sortedResult = mostCommonWords(result)

for i in sortedResult:
    print(f"{i[0]}: {i[1]}")

plotLengthFrequency(result)