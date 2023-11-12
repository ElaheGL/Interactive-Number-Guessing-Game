import random
start = 1
end = 99
hads = random.randint(start,end)
print(hads)
javab = input(str())
while(javab != 'd'):
    if( javab == 'k'):
        hads1 = random.randint(start,hads)
        hads = hads1
        print(hads1)
    elif(javab =='b'):
        hads2 =random.randint(hads,end)
        hads = hads2
        print(hads2)
    javab = input(str())
    
   
        

    
   
  
    

    

    
  
    
    