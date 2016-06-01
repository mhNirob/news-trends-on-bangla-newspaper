import re
inputfile = open("Data/stop words(final).txt","r",encoding="utf-8")
inputword = inputfile.read()
inputfile.close()
arrstr = inputword.split("\n")

outputfile = open("Frequency_keyword.txt","w",encoding="utf-8")


stop_word = set()

for word in arrstr:
    if word not in stop_word:
        stop_word.add(word)

dont = 0;

with open("Data/news paper data.txt","r",encoding="utf-8") as ins:
	for line in ins:
		#line.replace(","," ")
		#outputfile.write(line+'\n')
		if line=="</news>":
			dont=1
			continue
	
		elif dont==1:
			outputfile.write(line+'\n')
			dont=0
			continue
		else:
			dont=0
			#words = re.findall('\w+',line)
			line.replace(", "," ")
			line.replace("‌\n"," ")
			words = line.split(" ")
			for word in words:
				if (word != ',' and word != '(' and word != ')' and word != '\'' and word != '\n' and (word not in stop_word)):
					outputfile.write(word+'\n')






