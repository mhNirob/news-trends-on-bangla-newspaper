import json

inputfile = open("Data/stop words 1.txt","r",encoding="utf-8")
inputword = inputfile.read()
inputfile.close()
arrstr1 = inputword.split("\n")

inputfile = open("Data/stop words 3.txt","r",encoding="utf-8")
inputword = inputfile.read()
inputfile.close()
arrstr2 = inputword.split("\n")

json_data=open('Data/stop words 2.json').read()
data=json.loads(json_data)

with open('Data/data.txt','w') as f:
	json.dump(data, f, ensure_ascii=False)

inputfile = open("Data/data.txt","r",encoding="utf-8")
inputword = inputfile.read()
inputfile.close()
arrstr3 = inputword.split('", "')


arrstr = arrstr1+arrstr2+arrstr3




outputfile = open("Data/stop words.txt","w",encoding="utf-8")

unique = set()

var = 0

for word in arrstr:
    if word not in unique:
        outputfile.write(word+"\n")
        unique.add(word)
        var = var + 1

print (var)

