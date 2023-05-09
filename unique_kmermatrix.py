c = 0
a = {}
b = ''
for i in open('K_18_f','r'):
    c += 1
    if c == 1:
        b += i
    else:
        spl = i.strip().split('\t')
        a [spl[0]] = 0

for i in open('K_18_s4','r'):
    spl = i.strip().split('\t')
    if a.has_key(spl[0]):continue
    b += i
open('chayi_1','w').write(b)

