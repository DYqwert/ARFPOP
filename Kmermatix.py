#!/home/ribozyme/bin/anaconda3/bin/python3
# encoding:utf-8

import sys, os,time

if __name__ == '__main__':
    cv_txt_directory = sys.argv[1]
  
    Out_filement = sys.argv[2]
    allkmer={'species':''}
    c=0
    t = time.time()
    for i in os.listdir(cv_txt_directory):
        if i[-7:]=='.cv.txt':
        #    c += 1
            allkmer['species'] += '\t' + i[:-7]
            for j in open(cv_txt_directory+i,'r').readlines()[1:]:
                q=j.strip().split()
                allkmer[q[0]] = ''
        ##if c == 8: break
#    print(allkmer)
    print( round(time.time()-t,2) )
    #exit()
    t = time.time()
    c=0
    for filement in os.listdir(cv_txt_directory):
        if filement[-7:] == '.cv.txt':
            c += 1
            tmp = {}
            for row in open(cv_txt_directory+filement, 'r').readlines()[1:]:
                #if row == 0:continue
                lst = row.strip().split()
                tmp[lst[0]] = lst[1]
            for oneKmer in list(allkmer.keys())[1:]:
                if oneKmer in tmp:  allkmer[oneKmer] += '\t' + tmp[oneKmer]
                else:  allkmer[oneKmer] += '\t' + str(0)
        #if c ==-8: break
    print( round(time.time()-t,2) )

    t = time.time()
    fh = open(Out_filement, 'w')
    tmp = []
    for i in allkmer.keys():
        if i!='species':
           tmp.append( int(i) )
    tmp.sort()
    fh.write('species'+allkmer['species']+'\n')
    for i in tmp:
        fh.write(str(i) + allkmer[str(i)] + '\n')
    print( round(time.time()-t,2) )

