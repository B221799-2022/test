#!/usr/bin/python

#find the sequences' number
import linecache
path='/localdisk/home/s2280668/ICA2/test/seq.txt'
line_number=5
def getnum(path,line_number):
	return linecache.getline(path,line_number).strip()
seqnum1=getnum(path,line_number)
seqnum=int(seqnum1[7:10])
print(seqnum)

#Compare the sequence number with the limits
while True:
	if seqnum > 1000 or seqnum == 0:
		print("It is not suitable for analyzing, bye")
		break
	else:
		print("Great! You chose amazing sequence!")
		break

