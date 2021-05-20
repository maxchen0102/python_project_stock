

from tqdm import tqdm
from time import sleep 

a=0 
for i in tqdm(range(100)):
    a+=1 
    sleep(0.01)
    
test=[]
test= [0] * 100

print(test)    
print(a)



def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros