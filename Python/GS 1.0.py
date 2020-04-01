def uniqueSubstrings(inputString,substringLength):
    length=len(inputString)
    n=length-substringLength+1
    count={}
    for i in range(n):
        count[inputString[i:i+substringLength]]=i
    return sorted(count.keys())
    
def subsum(arr,k):
    count={}
    s=0
    for i in arr:
        if i in count.keys():
            count[i]+=1
        else:
            count[i]=1
    for r in count:
        if k-r in count and k-r!=r:
            s+=count[k-r]*count[r]/2
        elif k-r in count and k-r==r:
            s+=count[r]*(count[r]-1)/2
    return s
            
 
            
        

    
    
        
    
        
        
    

        