from __future__ import division
import pandas as pd
import time
import math
import multiprocessing
import itertools
import os
import sys
import numpy as np
import pandas as pd
#Create a directory if not exist at present workplace
def crtdir(work_station, filename):
    if not os.path.exists(work_station + '/' + filename):
        cmd = 'mkdir ' + work_station + '/' + filename
        os.system(cmd)
#Calculate the euclidean distance between two species' Kmer frequency vector
def euclidean_distance(pairsSpecies):
    sp1, sp2 = pairsSpecies[0], pairsSpecies[1]
    dict1, dict2, index = {}, {},set()
    kmer_number1 = list(data.loc[sp1])
    kmer_number2 = list(data.loc[sp2])

    for i in range(0,len(kmers)):
        index.add(kmers[i])
        dict1[kmers[i]] = int(kmer_number1[i])
        dict2[kmers[i]] = int(kmer_number2[i])
       # common_sets = index1&index2
       # different_sets = (index1|index2)-common_sets
    
    mintotal=min(sum(dict1.values()),sum(dict2.values()))
    dist = 0
    for i in index:
        #if min(dict1[i],dict2[i])==0:continue
        dist += min(dict1[i],dict2[i])
    dd= (-1 / k) * math.log((dist)/mintotal)
   # for i in different_sets:
    #    if i in dict1:
     #       dist += dict1[i]**2
      #  else:
       #     dist += dict2[i]**2
    return dd

if __name__ == '__main__':

    help = "python3 distance_matrix.py csvfile CPU.NUM distance-type (EUC)\n\
       cvtxt.directory\t-str\tThe path of cv.txt of species stored\tother suffix files must nonexistent\n\
       CPU.NUM\t-num\tThe number of CPU be used\n\
       distance-type\t-str\tEuclidean distance or Cosine disimilarity\n"
    ##使用文件格式为kmerMatrix.py合并之后的
    if len(sys.argv) < 4:
            exit(help)

    now = time.time()
    inputfile, coreNum, k = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    py1=np.loadtxt(inputfile,delimiter=',',dtype=str)
    pad1=pd.DataFrame(py1)
    pad1.columns=pad1.iloc[0]
    data=pad1.drop([0])
    data.set_index(["species"],inplace=True)
    #data = pd.read_csv(inputfile,index_col=0)
    kmers = list(data.columns.values)
   # print(kmers)
    #k=sys.argv[4]
    specieslist = []
    for i in data.index:
        specieslist.append(i)
    biospecies = list(itertools.combinations(specieslist,2))
   # print(specieslist)
     
    rst = []
    p = multiprocessing.Pool(coreNum)
    rst = p.map(euclidean_distance, biospecies)
    p.close()
    p.join()
    rst = list(rst)[::-1]
 #Output a triangle distance matrix of species
    output = \
    '#mega\n!Title megadist.meg' + ';\n' \
    + '!Format DataType=distance DataFormat=LowerLeft NTaxa=' \
    + str(len(specieslist))+';\n'+'\n'
    for i in specieslist[::-1]:
        output += '#'+i+'\n'
        output += '\n'
        count = 0
    for i in range(1,len(specieslist)+1):
        for j in rst[count:count+i]:
            output += str("%.18f"%j)+'\t'
            count += 1
            output += '\n'
    crtdir('./', 'MEG')
    namelist = inputfile.split('/')
    crtdir('MEG/', namelist[-1])
    open('MEG/'+namelist[-1]+'/'+namelist[-1]+'eucdist.meg', 'w').write(output)
    print(time.time()-now)

