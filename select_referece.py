import sys

#out=open(sys.argv[1],'r').readlines()[0]
out=''
a=0
for line in open(sys.argv[1],'r'):
    line1=line.strip().split('\t')
    if a==0:out+=line;a+=1
    else:
        if line1[int(sys.argv[2])]!='0':
            suml=0
            for i in line1[1:]:
                suml+=int(i)
            #if suml<267:
            out+=line
open(sys.argv[3],'w').write(out)

