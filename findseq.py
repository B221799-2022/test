#!/usr/local/bin/python

import os, subprocess

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
cmd1='esearch -db protein -query "txid' + str(taxo) + '[organism] AND ' + protein + '[protein]" | efetch -format fasta > seqfas.fasta'

os.system(cmd)
os.system(cmd1)
