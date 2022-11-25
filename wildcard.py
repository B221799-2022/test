#!/usr/bin/env python3
import os,PIL

#make the stats of all the sequences user selected
cmd='pepstats final.fasta stat.pepstats'
os.system(cmd)
print("We have made a file contains all the detailed information of the sequences\nYou can see it in the folder")

#ask the users to choose the window size for pepwindowall
print("We will show you the Kyte-Doolittle hydropathy plot for the alignment then")
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
      if int(size)!=0:
        cmdd="pepwindowall cluster.txt -window "+size+" -graph png"
        os.system(cmdd)
        print("Ok,the file is created")
        from PIL import Image
        img=Image.open("pepwindowall.1.png")
        img.show()
        idea=input("Do you want to change the window size?y/n").upper()[0]
      else:
        print("Sorry, the size should bigger than 0")
        winsize()
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

#tell user that is the end of the programme
print("That is all for the programme\nThanks for using\nBye!")
