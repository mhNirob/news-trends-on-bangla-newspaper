inputfile = open("Data/Grouped/Bangla/banglabhasa.txt","r",encoding="utf-8")
inputword = inputfile.read()
inputfile.close()
arrstr = inputword.split("\n")

keyword = set()

for word in arrstr:
    if word not in keyword:
        keyword.add(word)



preLine = '<news date= "Fri Jan 01 00:00:00 BDT 2010">\n'

x = 1
y = 0

outputfile = open("Graph/banglabhasa_x_y.txt","w",encoding="utf-8")
outputfiledate = open("Data/Grouped/Bangla/Banglabhasa_x_y_date.txt","w",encoding="utf-8")


with open("Data/Separeted_word.txt","r",encoding="utf-8") as ins:
	for line in ins:
		#line.replace(","," ")
		#outputfile.write(line+'\n')
		if line=="</news>\n":
			dont=1
			continue
		elif dont==1:
			if line!=preLine:
				#outputfile.write(line)
				outputfiledate.write(preLine)
				outputfile.write(str(y))
				outputfile.write('\n')
				outputfiledate.write(str(y))
				outputfiledate.write('\n')
				x = x+1
				y=0
				preLine=line
			
			dont=0
			continue
		else:
			dont=0
			word = line
			length = len(word)
			if length>1 and word[length-1]=='\n':
				word = word[:-1]
			if (word in keyword):
				y = y + 1
