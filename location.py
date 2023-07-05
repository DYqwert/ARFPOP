import sys

cvtxt=sys.argv[1]
KM=sys.argv[2]
outfile=sys.argv[3]

sortcv={}
a=0
b=0
for line in open(cvtxt,'r'):
    sortcv[int(line.split()[2])]=line.split()[0]
kmer={}
Tittle=''
a=0
for line in open(KM,'r'):
    if a==0:Tittle+=line;a+=1
    else:
        l=line.split('\t')[0]
        kmer[l]=line
#for j in sorted(list(sortcv.keys())):
x=0
for i,j in sortcv.items():
    if j in kmer:
        Tittle+=str(i)+"-"+kmer[j]
open(outfile,'w').write(Tittle)
