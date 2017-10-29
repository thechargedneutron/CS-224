fin = open("tcp-example.tr", "r")
fout = open("p3.txt", "w")
str2=fin.readline()
str1=[]
str1 = str2.split()
n=0
t=0

while (str2!="") :
	str1 = str2.split()
	if str1[0] =='+':
		n+=1
	elif str1[0]=='-':
		n-=1
	else:
		str2=fin.readline()
		continue
	t=float(str1[1])
	fout.write(str(t) + "\t" + str(n) +"\n")
	str2=fin.readline()
fin.close()
fout.close()