#!/usr/bin/env python
""" Converts PDB files to CRD files. NOT Python3 compatible """
__author__ = "Rohan Pandit"

import sys
import os

def main():
	#Example Usage: python2.7 pdb2crd.py Met-Enk.pdb 180
	name = sys.argv[1]
	numAtoms = int(sys.argv[2])

	f = open(name, 'r')
	modelnum = 0

	out=open(name[:-4] + '.crd', 'w')

	for l in f:
		if 'END MODEL' in l:
			modelnum+=1
			out.write('\n')
		elif len(l)>33:
			out.write(l[33:56])


def splitFile(inFileName, numAtoms):
	infile = open(inFileName, 'r')
	outfile = open(inFileName+"_1", 'w')

	modelNum=1
	count=1
	for line in infile:
		if count > numAtoms:
			modelNum += 1
			count = 1
			outfile = open(inFileName+"_"+str(modelNum),'w')
		
		if count == numAtoms: # to take care of ending with newline problem
			line = line[:-2]
		
		outfile.write(line)
		count+=1

if __name__=="__main__":
	main()