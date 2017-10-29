#This program calculates the number of times cwnd dropped
fin = open("tcp-example.cwnd", "r")
str2=fin.readline()
str1=[]
str1 = str2.split()
str3=[]
str2=fin.readline()
str3 = str2.split()
		
n=0
while (str2!="") :
	str3 = str2.split()
	if (str3[1]<str1[1]):
		n+=1
	str2=fin.readline()
	str1=str3
print n
fin.close()