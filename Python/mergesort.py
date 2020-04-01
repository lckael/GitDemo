class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
       # if A==[]:
        #    return []
        #tmp=A[0]
        #left=[]
        #ight=[]
        #for i in range(1,len(A)):
         #   if A[i]<tmp:
          #      left+=[A[i]]
           # else:
            #    right+=[A[i]]
        #return self.sortIntegers2(left)+[tmp]+self.sortIntegers2(right)
        # Merge sort
        if len(A)>1:
            start=0
            end=len(A)-1
            mid=start+(end-start)//2+1
            left=A[:mid]
            right=A[mid:]
            self.sortIntegers2(left)
            self.sortIntegers2(right)
            i=0
            j=0
            k=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    A[k]=left[i]
                    i+=1
                else:
                    A[k]=right[j]
                    j+=1
                k+=1
            
            while i<len(left):
                A[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                A[k]=right[j]
                j+=1
                k+=1
a=Solution()
b=[3,2,1,4,5,6]
a.sortIntegers2(b)
        
            