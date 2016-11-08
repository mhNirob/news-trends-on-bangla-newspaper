import re
inputfile = open("Data/stop words(final).txt","r",encoding="utf-8")
inputword = inputfile.read()
inputfile.close()
arrstr = inputword.split("\n")

stop_word = set()

for word in arrstr:
    if word not in stop_word:
        stop_word.add(word)

dont = 0;

outputfile = open("Separeted_word.txt","w",encoding="utf-8")

preLine = '<news date= "Fri Jan 01 00:00:00 BDT 2010">\n'

outputfile.write("</news>\n")
outputfile.write(preLine)

with open("Data/news paper data.txt","r",encoding="utf-8") as ins:
	for line in ins:
		#line.replace(","," ")
		#outputfile.write(line+'\n')
		if line=="</news>\n":
			dont=1
			continue
		elif dont==1:
			if line!=preLine:
				outputfile.write("</news>\n")
				outputfile.write(line+'\n')
				preLine=line
			
			dont=0
			continue
		elif line=="অ- অ অ+\n":
			continue
		else:
			dont=0
			#words = re.findall('\w+',line)
			line.replace(", "," ")
			line.replace("‌\n"," ")
			words = line.split(" ")
			for word in words:
				length = len(word)
				if length>1 and word[length-1]=='\n':
					word = word[:-1]
				if (word != ',' and word != '(' and word != ')' and word != '\'' and word != '\n' and (word not in stop_word)):
					outputfile.write(word+'\n')

					#outputfile.write(word+'\n')