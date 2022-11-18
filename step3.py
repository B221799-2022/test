#!/usr/bin/python

import os,re,PIL

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
  with open("species.txt","w")as species:
    for i in tem:
      species.write(i+'\n')
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
        print("Sorry, the length should be some numbers and more than 1......")
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
  command1="head -n"+length1+" fastafile.fasta > ana1.fasta"
  os.system(command1)
  n=b
  if n=="bye":
    break
#ask the users to choose the accession ID
while 1:
  h="hi"
  command11="cp ana1.fasta ana2.fasta"
  os.system(command11)
  def answer1():
    global c
    global IDuser
    global IDuserlist
    global option
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
            command2="grep -w "+IDuser+" fastafile.fasta >> ana2.fasta"
            os.system(command2)
            option=input("Do you wanna choose another ID?y/n").upper()[0]
          else:
            print("Sorry, you may typed something wrong, please enter again...")
            id()
        id()
        end=option
        if end=="N":
          break
        elif end=="Y":
          continue
        else:
          print("Sorry,you should type y/n,,please type again...")
          option=input("Do you wanna choose ID again?y/n").upper()[0]
          if option=="Y":
            continue
          else:
            break
      c="bye"
    elif choice1.upper()=="N":
      print("That is fine, we can ignore it...")
      c="bye"
    else:
      print("Sorry,you typed wrong...please check it again")
      answer1()
  answer1()
  h=c
  if h=="bye":
    break
if IDuserlist!=[]:
  print("Okay,file has been created\nYou have chosen the accessions as below:")
  for i in IDuserlist:
    print(i)
  print("We are going to the next step then")
else:
  print("We are going to the next step then")
#ask the users to choose the species they are interested in
while 1:
  g="hi"
  command22="cp ana2.fasta ana3.fasta"
  os.system(command22)
  def answer2():
    global p
    global suser
    global suserlist
    global option1
    p=("")
    suserlist=[]
    choice2=input("Do you wanna to choose the species?y/n")
    if choice2.upper()=="Y":
      while 1:
        end1="Y"
        def species():
          global option1
          suser=input("Cool,the species is...(enter the full species name from NCBI)")
          if suser in tem:
            suserlist.append(suser)
            command3="grep -w "+"\'"+suser+"\'"+" fastafile.fasta >> ana3.fasta"
            os.system(command3)
            option1=input("Do you wanna choose another species?y/n").upper()[0]
          else:
            print("Sorry, you may typed something wrong, please enter again...")
            species()
        species()
        end1=option1
        if end1=="N":
          break
        elif end1=="Y":
          continue
        else:
          print("Sorry,something is wrong,please type again...")
          option1=input("Do you wanna choose again?y/n").upper()[0]
          if option1=="Y":
            continue
          else:
            break
      p="bye"
    elif choice2.upper()=="N":
      print("That is fine, we can ignore it...")
      p="bye"
    else:
      print("Sorry,you typed wrong...please check it again")
      answer2()
  answer2()
  g=p
  if g=="bye":
    break
print("Okay, the species you have chosen are as below:")
for i in suserlist:
  print(i)
#change the template ana.fastas into a normal fasta file(delete the '?')
final1=[]
final2=[]
with open("ana3.fasta","r")as f:
  lines=f.readlines()
  for i in lines:
    i1=i.split("?")
    final1.append(i1[0])
    final2.append(i1[-1])
final=[]
with open("final.fasta","w")as file:
  for i in range(0,len(final1)):
    final=final1[i]+'\n'+final2[i]
    file.write(final)
#cluster the sequences the user chose
cmdc="clustalo -i final.fasta -o cluster.txt -v --force"
os.system(cmdc)
#use infoalign to display the basic information about the multiple sequence alignment
cmdi="infoalign cluster.txt infoalign.txt -nousa"
os.system(cmdi)
print("You can read the identity or other information from the text file created")
#use plotcon to make the graph and obtain the data
while 1:
  global size
  global idea
  global gr
  global go
  gr=0
  def winsize():
    global idea
    global size
    go="Y"
    size=input("It is up to you to choose the window size\nWhat is it(enter a number)")
    if size.isdigit():
      cmdd="plotcon cluster.txt -winsize "+size+" -graph png"
      os.system(cmdd)
      print("Ok,the file is created")
      from PIL import Image
      img=Image.open("plotcon.1.png")
      img.show()
      idea=input("Do you want to change the window size?y/n").upper()[0]
    else:
      print("Sorry,you typed wrong,please enter a number")
      winsize()
  winsize()
  go=idea
  if go=="Y":
    continue
  elif go=="N":
    break
  else:
    print("You typed wrong...")
    idea=input("Please enter it again").upper()[0]
    if idea=="Y":
      continue
    else:
      break
  gr=1
  if gr==1:
    break
#export the data of plotcon
cmdd1="plotcon cluster.txt -winsize "+size+" -graph data"
os.system(cmdd1)
cmdd2="grep -v '##' plotcon1.dat > plotcon.txt"
os.system(cmdd2)
cmdd3="grep -w 'Ymax' plotcon1.dat"
os.system(cmdd3)
print("The line shows above means\nX means the number of residue,so Xmax means how many residues do we have\nY means the number of similarity")
with open("plotcon.txt","r")as f:
  lines=f.readlines()
  sum=0
  l=0
  li=[]
  for i in lines:
    i1=i.split("\t")[1]
    li.append(i1)
  for a in li:
    a1=float(a)
    l=l+1
    sum=sum+a1
    avg=sum/l
    avg=('%.4f' % avg)
print("The average of the similarity is "+str(avg))
