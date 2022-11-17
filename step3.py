#!/usr/bin/python

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

#making the file into a one-line fasta format
name=[]
fasta=[]
atcg=[]
with open ("seqfas.fasta","r") as f:
  line=f.readlines()
for i in line:
  if i[0]==">":
    i1=i.replace("\n","")
    name.append(i1)
    fastem="".join(atcg)
    fasta.append(str(fastem))
    atcg=[]
  else:
    line=i.replace("\n","")
    atcg.append(line)
fastem="".join(atcg)
fasta.append(str(fastem))
fasta.pop(0)
ID=[]
for i in name:
  id1=i.split(" ")
  id2=id1[0].replace(">","")
  ID.append(id2)
with open("IDlist.txt","w")as aid:
  for line in ID:
    aid.write(line+'\n')
with open("fastafile.fasta","w")as file:
  for i in range(0,len(name)):
    fa=name[i]+"?"+fasta[i]
    file.write(fa+'\n')
#tell the users about the next steps
print("We will do the next analyzing then\nYou can determine which parameter(Length of sequence,ID and species\nIf the sequence number is too big, we will choose 450 as the limitation number\nOtherwise,we will choose all the sequences you have searched")
#ask the users to choose the length of sequence
while 1:
  n="hi"
  def answer():
    global b
    global length
    global length1
    b=("")
    choice=input("Do you wanna to select the number of sequence you are interested in?y/n")
    if choice.upper()=="Y":
      length=input("Perfect, the sequence length is...(enter a number)")
      if length.isdigit():
        print("Thank you, we got it!")
        length1=length
        b="bye"
      else:
        print("Sorry, the length should be some numbers......")
        length=input("Please enter the sequence length again...")
        length1=length
        b="bye"
    elif choice.upper()=="N":
      print("OK,so we will help you make the decision")
      length=seqnum1[7:-8]
      if len(length)<450:
        length1=length
      else:
        length1=450
      b="bye"
    else:
      print("Sorry, you typed wrong...please check again")
      answer()
  answer()
  command1="head -n"+length1+" fastafile.fasta > ana1.txt"
  os.system(command1)
  n=b
  if n=="bye":
    break
#ask the users to choose the accessiion ID
while 1:
  h="hi"
  def answer1():
    global c
    global IDuser
    global IDuserlist
    c=("")
    IDuserlist=[]
    choice1=input("Do you wanna to select the accession ID?y/n")
    if choice1.upper()=="Y":
      while 1:
        end="Y"
        def id():
          global option
          IDuser=input("Cool,the ID is...(enter the accession ID from NCBI)")
          if IDuser in ID:
            IDuserlist.append(IDuser)
            command2="grep -w "+IDuser+" fastafile.fasta >> ana3.txt"
            os.system(command2)
            option=input("Do you wanna choose another ID?y/n").upper()[0]
          else:
            print("Sorry, you may typed something wrong, please enter again...")
            id()
        id()
        end=option
        if end=="N":
          break
      c="bye"
    elif choice1.upper()=="N":
      print("That is fine, we can ignore it...")
      command3="cp ana1.txt ana2.txt"
      os.system(command3)
      c="bye"
    else:
      print("Sorry,you typed wrong...please check it again")
      answer1()
  answer1()
  h=c
  if h=="bye":
    break
print(IDuserlist)

