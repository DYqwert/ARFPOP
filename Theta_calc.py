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
    
    #mintotal=min(sum(dict1.values()),sum(dict2.values()))
    dist = 0
    for i in index:
        #if min(dict1[i],dict2[i])==0:continue
        dist += abs(dict1[i]-dict2[i])
    dd=dist/float(sum(dict1.values())+sum(dict2.values()))
    #dd=dist/len(index)/k
   # for i in different_sets:
    #    if i in dict1:
     #       dist += dict1[i]**2
      #  else:
       #     dist += dict2[i]**2
    return dd

if __name__ == '__main__':

    now = time.time()
    inputfile, coreNum, k = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
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
    print(rst)
 #Output a triangle distance matrix of species
    Output=str(sum(rst)/float(len(rst))/k)
    print(Output)
    open(inputfile+'_theta','w').write(Output)
    print(time.time()-now)

