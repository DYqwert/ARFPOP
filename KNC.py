#! /home/ribozyme/bin/anaconda3.newest/bin/python3
# -*- coding:utf-8 -*-
import sys
import re
import os
import time
import multiprocessing
from Bio import SeqIO
def reverse_complement(s):
    basecomplement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    letters = list(s)
    letters = [basecomplement[base] for base in letters]
    return(''.join(letters)[::-1])

def str2int(Kmer):
    nucleotide = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    Kmer_list = list(Kmer)
    location = len(Kmer)-1
    Kmer_value = 0
    for i in Kmer_list:
        Kmer_value += nucleotide[i]*4**location
        location -= 1
    return(Kmer_value)

def realname(kmer):
    rname=min([str2int(kmer),str2int(reverse_complement(kmer))])
    return(rname)

def seq_count(seq,k):
    base=['A','C','G','T']
    allkmer={}
    for i,j in enumerate(list(seq)[:-k+1]):
        j=j.upper()
        kmer=seq[i:i+k].upper()
        if j not in base:continue
        if 'N' in kmer:continue
        if 'R' in kmer:continue
        if 'Y' in kmer:continue
        if 'S' in kmer:continue
        if 'M' in kmer:continue
        if 'K' in kmer:continue
        if 'W' in kmer:continue
        if 'H' in kmer:continue
        if 'D' in kmer:continue
        if 'V' in kmer:continue
        if '-' in kmer:continue
        kmername=realname(kmer)
        loc=i
        
        if kmername in allkmer:
            allkmer[kmername][0]+=1
            allkmer[kmername][1].append(i)
        else:
            allkmer[kmername]=[1,[i]]
    return(allkmer)

def readseq(fa):
    faseq={}
    for seq_record in SeqIO.parse(fa, "fasta"):
        faseq[seq_record.name] = str(seq_record.seq)    
    return(faseq)


if __name__ == '__main__':
    tt=time.time()
    fa=sys.argv[1]
    k=int(sys.argv[2])
    faseq=readseq(fa)
    SEQ=''
    print(time.time()-tt)
    for contig,seq in faseq.items():
        SEQ+=seq
    allkmer=seq_count(SEQ,k)
    print(time.time()-tt)
    out=''
    for i,j in allkmer.items():
        out+=str(i)+'\t'+str(j[0])+'\t'+' '.join(list(map(str,j[1])))+'\n'
    open(sys.argv[3]+'cv.txt','w').write(out)
