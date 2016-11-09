import matplotlib as plt
import matplotlib.pyplot as plt


inputfile = open('Female_x_y.txt','r')

inputword = inputfile.read()
inputfile.close()
ys = inputword.split("\n")

keyword = set()

x = 1

for y in ys:
	try:
		int(y)
	except ValueError:
		continue 
	plt.plot(x,int(y),'ro')
	x += 7


plt.axis([0,1000,0,500])

plt.show()