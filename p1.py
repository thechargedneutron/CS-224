#This program calculates average TCP throughput from beni.txt file which was generated from the simulated pcap file
#command used for making beni.txt :  tshark -r tcp-example-1-0.pcap -T fields -e frame.time_epoch -e ip.src -e ip.dst -e tcp.len >> beni.txt
fin = open("beni.txt", "r")
srcip="10.1.1.1"
dstip="10.1.1.2"
str2=fin.readline()

str1=[]
str1 = str2.split()
tot=0
time1=float(str1[0])
time=0
while (str2!="") :
	str1 = str2.split()
	if (srcip==str1[1] and dstip==str1[2]):
		tot += int(str1[3])
	str2=fin.readline()
	time=float(str1[0])
print tot*8/(time-time1)
fin.close()
