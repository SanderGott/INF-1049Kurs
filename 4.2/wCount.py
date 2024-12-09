import os

FILTER = ".,:;!?()[]{}-"

def wordCount(fileName):
    """
    Returner et dict med ordet som key og alle forekomster av ordet som value. 
    Mange ord består bare av , : - osv... Bruk FILTER variabelen for å filtrere ut disse.
    """
    pass


def mostCommonWords(wordCountDict):
    """
    Returner en liste med de 10 mest brukte ordene. 
    Hvert element i listen skal være et tuple med ordet og antall forekomster. 
    Sortert etter antall forekomster, der det mest brukte ordet er først.
    """
    pass

def plotLengthFrequency(wordCountDict):
    """
    Finn antall forekomster av hver ordlengde og plot det som en bar chart. 
    """

fileName = os.path.join(os.path.dirname(__file__), "bee.txt")

result = wordCount(fileName)

commonWords = mostCommonWords(result)

for i in commonWords:
    print(f"{i[0]}: {i[1]}")

plotLengthFrequency(result)