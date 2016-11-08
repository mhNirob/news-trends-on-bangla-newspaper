from operator import itemgetter
with open("Data/Frequency(root).txt","w",encoding="utf-8") as outputfile:

	#print (outputfile)

	keyword = {}


	with open("Data/Separeted_word(root).txt","r",encoding="utf-8") as ins:
		for line in ins:
			if line=="</news>\n":
				#sorted(keyword.values())
				#sorted(keyword.items(), key=lambda x:x[1])
				#print (keyword)
				d_view = [ (v,k) for k,v in keyword.items() ]
				d_view.sort(reverse=True)
				for v,k in d_view:
					#if keyword[word] > 10:
						#print (word+"		"+str(keyword[word]))
						#tword = word.replace("\n","")
						#outputfile.write(word+str(keyword[word])+"\n\n");
					if v>=10:
						outputfile.write(k+str(v)+"\n\n");

				keyword = {}
				outputfile.write(line)
				dont = 1
				continue
			elif dont==1:
				outputfile.write(line)
				dont = 0
				continue
			elif line in keyword:
				keyword[line] += 1
			else:
				keyword[line] = 1

outputfile.close()
				