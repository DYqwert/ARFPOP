import sys
c = 0
b = ''
minC=sys.argv[1]
N=int(sys.argv[2])
for i in open(sys.argv[1],'r'):
    c += 1
    if c == 1:
        b += i
    else:
        d = []
        spl = i.strip().split('\t')
        for k in spl[1:]:
            if int(k) < minC :
                d.append(k)
        if len(d) != N :continue
        #if sum(list(map(int,spl[1:]))) == 8 :continue
        #if sum(list(map(int,spl[1:]))) == 0 :continue
        b += spl[0] + '\t' + '\t'.join(d) + '\n'
open(sys.argv[2],'w').write(b)

