unstructured = open("UnstructuredEmotionRankings.txt", "r")
structured = open("EmotionRankings.txt", "w+")

currentWord = ""

for line in unstructured:
    thisLine = line.split()
    print(thisLine)
    thisWord = thisLine[0]
    if (thisWord == currentWord):
        structured.write("," + thisLine[2])
    else:
        currentWord = thisWord
        structured.write("\n" + thisWord + "," + thisLine[2])

unstructured.close()
structured.close()
