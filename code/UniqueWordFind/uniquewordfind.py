import json

inputfile = open("Bangla Corpus (word list).txt", "r", encoding="utf-8")
inputstr = inputfile.read()
inputfile.close()
arrstr = inputstr.split("\n")

print("Total Words:", len(arrstr))
wordmap = json.dumps({'id': 1})
wordmap = json.loads(wordmap)

print(wordmap)

uniquewords = 0

for word in arrstr:
    try:
        val = wordmap[word]+1
    except KeyError:
        val = 1
        uniquewords += 1
    except TypeError:
        val = 1
        uniquewords += 1
    wordmap[word] = val

print("Unique Words:", uniquewords)

"""outputfile = open("word list.txt", "w", encoding="utf-8")
for stri in arrstr:
    strlen = len(stri)
    dp = []
    for i in range(strlen+1):
        dp.append(0)
    dp[0] = 1
    for i in range(strlen):
        for j in range(i+1, strlen):
            now = stri[i:j+1]
            try:
                val = wordmap[now]
                dp[j+1] += dp[i]
            except KeyError:
                val = 1

    if dp[strlen] > 1:
        outputfile.write(stri)
        outputfile.write('\n')
outputfile.close()"""

outputfile = open("word list2.txt", "w", encoding="utf-8")
outputfile1 = open("word list5.txt", "w", encoding="utf-8")
total = 0
for stri in arrstr:
    strlen = len(stri)
    outputfile1.write(stri)
    outputfile1.write('\n')
    for i in range(1,strlen-2):
        try:
            val = wordmap[stri[0:i+1]]
            val = wordmap[stri[i+1:strlen]]
            outputfile.write(stri)
            outputfile.write(' ')
            outputfile.write(stri[0:i+1])
            outputfile.write(' ')
            outputfile.write(stri[i+1:strlen])
            outputfile.write('\n')
            total += 1
            break
        except KeyError:
            val = 1

outputfile.close()
outputfile1.close()

print("Total Words:", total)
