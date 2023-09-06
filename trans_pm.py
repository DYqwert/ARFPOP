#!/home/ribozyme/bin/anaconda3/bin/python3 
# encoding:utf-8
# ./kmer_makemp.py   输入文件(filter之后的文件)   输出文件              ——>会产生     输出文件.map  和   输出文件.ped  这两个文件
import sys
import math
import re
if __name__=='__main__':
    infile=sys.argv[1]
    outfile=sys.argv[2]
    output=''
    m=1
    i=open(infile,'r').readlines()[1:]
    for x in i:
        #ref|NC_001133|_2133_A 
        l=x.split('\t')[0]#        chrom=l[0]+'_'+l[1]
        loc=l.split('-')[0]
        output+='1 '+l+' 0 '+loc+'\n'
    open(outfile+'.map','w').write(output)
    a=0
    pedfile={}
    for line in open(infile,'r'):
        l=line.strip().split()
        if a==0:
            spec=l[1:]
            a+=1
            for i in spec:
                pedfile[i]=[]
        else:
            for i,j in enumerate(l[1:]):
                pedfile[spec[i]].append(j)
    ped=''
    for ID,kmer in pedfile.items():
        ped+=' '.join([ID,ID,'0','0','0','0']+kmer)+'\n'
    open(outfile+'.ped',,'w').write(ped)
            

