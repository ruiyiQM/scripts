import numpy as np
import re
class Hole:
     def __init__(self, filename , number, dt ):
         read=open(filename,"r")
         self.occ =[]
         for line in read.readlines():
              if (re.search("occupancy",line)):
               data=line.split()
               if (len(data)<5):
                  self.occ.append(float(data[0][12:-2]))
         self.occ=np.asarray(self.occ).reshape(-1,number)
         self.pop= []
         self.number = number
         read=open(filename,"r")
         for line in read.readlines():
              if (re.search("population",line)):
                data=line.split()
                for i in range(1,len(data)-1):
                       self.pop.append(float(data[i]))
         self.pop = np.asarray(self.pop).reshape(-1,number,len(data)-2)
         self.length = self.occ.shape[0]
         self.time =np.arange(self.length)*dt
     def sort(self): 
         sort_length = self.pop.shape[2] 
         self.result =np.copy(self.occ[:,:sort_length])
         self.sorted_pop = np.copy(self.pop)  
         print (self.pop.shape)
         for i in range(100,self.length):
              list =[ l for l in range(0,sort_length)]
              
              for j in range(0,sort_length):
                     delta = 10
                     index = j 
                     for k in list:
                          diff = np.abs(np.sum(self.sorted_pop[i-100:i,:,j],axis=0)/100-self.pop[i,:,k])
                          if (np.sum(diff)<delta):
                                index = k
                                delta = np.sum(diff)
                     #print (list,index)
                     self.result[i,j]= self.occ[i,index]
                     list.pop(list.index(index))
                     self.sorted_pop[i,:,j]=self.pop[i,:,index]                      
