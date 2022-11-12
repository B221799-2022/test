#!/usr/local/bin/python

import os

while 1:
  i=0

#ask the user to input the taxon ID and the protein family
  protein=input('Enter the specific protein family please:')
  taxo=input('Enter the taxonID please:')

#make sure the input taxonID is an integer
  if taxo.isdigit():
    taxo=int(taxo)
  else:
    print('Sorry,the taxonID should be some numbers...')
    taxo=input('Enter the taxonID(some digits) please:')

#using esearch to find the sequences
  cmd='esearch -db protein -query "txid' + str(taxo) + '[organism] AND ' + protein+ '[protein]" > seq.txt'
  os.system(cmd)
#find the sequences' number
  import linecache
  path='/localdisk/home/s2280668/ICA2/test/seq.txt'
  line_number=5
  def getnum(path,line_number):
    return linecache.getline(path,line_number).strip()
  seqnum1=getnum(path,line_number)
  seqnum=int(seqnum1[7:-8])
  print(seqnum)

#Compare the sequence number with the limits
  if seqnum > 20 and seqnum < 1000:
    print("Perfect!That is good for analyzing:)")
    i=1
  else:
    print("Sorry, it is not suitable for analyzing...")                       
    user=input("Do you wanna continue?y/n")
    if user.upper()[0]=="Y":
      print("Ok,we will continue")
      i=1
    else:
      print("Great!Let us start again")
  if i==1:
    break


