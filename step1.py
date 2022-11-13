#!/usr/local/bin/python

import os,re

#The 1st section of the step--count the sequence number
while 1:
  i="continue"

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
  print("The number of sequence is",seqnum)

#grep the lines with the information of species
  cmd1="grep '>' seqfas.fasta > spe.txt"
  os.system(cmd1)

#count the numbers of the species
  tem=set()
  with open("spe.txt","r") as file:
    lines=file.readlines()
  for i in lines:
    species1=re.findall(r'\[(.*?)\]',i)
    for item in species1:
      tem.add(item)
  count=len(tem)
  print("The number of species is",count)

#define a function to obtain user's ideas
  def answercount():
    global a
    a=("")
    usersp=input("Do you wanna continue?y/n")
    if usersp.upper()=='Y':
      print("Here we go, we will continue then")
      a="bye"
    elif usersp.upper()=='N':
      print("Great!Let us start again")
    else:
      print("Sorry, you typed wrong...please check again")
      answercount()

#Compare the sequence number with the limits
  if 20 < seqnum < 1000 and count>10 :
    print("Perfect!That is good for analyzing:)")
    i="bye"
  else:
    print("Sorry, it is not suitable for the next steps...")                       
    answercount()
    i=a
  if i=="bye":
    break

