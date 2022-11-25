#!/usr/local/bin/python
import os
import pandas as pd

#write a function to choose 2 lines once
from typing import List, Iterable
def read(fp: str, n: int) -> Iterable[List[str]]:
  i=0
  lines=[]
  with open(fp) as f:
    for line in f:
      i=i+1
      lines.append(line.strip())
      if i >=n:
        yield lines
        i=0
        lines.clear()
  if i >0:
    yield lines

#use the function above
fp="final.fasta"
lines_gen=read(fp,2)

#use the variable 'hebing' to make the sequence as a normal fasta file
hebing=[]

#analyze one sequence per time, then choose the data
for lines in lines_gen:
  hebing=lines[0]+'\n'+lines[1]
  file=open("motif.fa","w")
  file.write(hebing)
  file.close()
  cmd="patmatmotifs motif.fa motif.txt -rformat2 gff"
  os.system(cmd)
  cmd1="grep -v '#' motif.txt > motif1.txt"
  os.system(cmd1)
  with open("motif1.txt","r")as f1:
    line=f1.readlines()
    f2=open("motiffinal.txt","a")
    for i in line:
      f2.write(i)
    f2.close
    
df=pd.read_table("motiffinal.txt",header=None)
df.columns=["ID","Source","Type","Start","End","Score","Strand","Phase","Attributes"]
df.drop("Source",inplace=True,axis=1)
print("The dataframe created by using patmatmotifs is showed as below:")
df["Motif"]=df['Attributes'].str.split(" ",expand=True)[1]
df.drop("Attributes",inplace=True,axis=1)
print(df)

count=df["Motif"].value_counts()
print("The number of each motif is showed as below:")
print(count)
