#!/usr/bin/python

import os,re

#grep the lines with the information of species
cmd="grep '>' seqfas.fasta > spe.txt"
os.system(cmd)

tem=set()
with open("spe.txt","r") as file:
  lines=file.readlines()
for i in lines:
  species1=re.findall(r'\[(.*?)\]',i)
  for item in species1:
    tem.add(item)
print(len(tem))

