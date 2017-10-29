#this program calculates waiting time for each packet and stores it in p4.txt
fin = open("tcp-example.tr", "r")
fout = open("p4.txt", "w")
str2=fin.readline()
str1=[]
str1 = str2.split()
m=[]
t=0

while (str2!="") :
	str1 = str2.split()
	t=float(str1[1])
	if str1[0] =='+':
		m.append(float(str1[1]))
	elif str1[0]=='-':
		w=m[0];
		del m[0]
		fout.write(str(t) + "\t" + str(t-w) +"\n")
		
	str2=fin.readline()
fin.close()
fout.close()
