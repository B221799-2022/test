#!/usr/bin/python

import os

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
with open("fastafile.fasta","w")as file:
  for i in range(0,len(name)):
    fa=name[i]+"?"+fasta[i]
    file.write(fa+'\n')

#tell the users about the next steps
print("We will do the next analyzing then\nYou can determine which parameter(Length of sequence,ID and Species) to select\nAlso, you can just leave the sequences for us, we will choose 450 as the limitation length of sequence")
print("Again, if you are not interested in choosing it, we will make all the sequences you have found to make the next processing procedures")
while 1:
  n="hi"
  def answer():
    global b
    b=("")
    choice=input("Do you wanna to select the number of sequence you are interested in?y/n")
    if choice.upper()=="Y":
      length=input("Perfect, the sequence length is...(enter a number)")
      if length.isdigit():
        length=int(length)
        print("Thank you, we got it!")
        b="bye"
      else:
        print("Sorry, the length should be some numbers......")
        length=input("Please enter the sequence length again...")
        b="bye"
    elif choice.upper()=="N":
      print("OK,so we will help you make the decision")
      b="bye"
    else:
      print("Sorry, you typed wrong...please check again")
      answer()
  answer()
  n=b
  if n=="bye":
    break

while 1:
  h="hi"
  def answer1():
    global c
    c=("")
    choice1=input("Do you wanna to select the accession ID?y/n")
    if choice1.upper()=="Y":
      ID=input("Cool, the ID is...(enter the accession ID from NCBI)")
      c="bye"
    elif choice1.upper()=="N":
      print("That is fine, we will help you...")
      c="bye"
    else:
      print("Sorry,you typed wrong...please check it again")
      answer1()
  answer1()
  h=c
  if h=="bye":
    break

while 1:
  j="hi"
  def answer2():
    global d
    d=("")
    choice2=input("Last but not least, do you wanna to select the species?y/n")
    if choice2.upper()=="Y":
      species=input("Great,the species is...(enter the scientific name of the species)")
      d="bye"
    elif choice2.upper()=="N":
      print("Alright, we can help you definitely...")
      d="bye"
    else:
      print("Sorry, you typed wrong...please check it again")
      answer2()
  answer2()
  j=d
  if j=="bye":
    break
