def longest_repetition(list):
    if list==[]:
        return None
    else:
        pre=[]
        j=0
        H=[]
        M=[]
        k=1
        while j<len(list):   
            if list[j]==pre:
                k=k+1
                pre=list[j]
            else:
                H.append(list[j-1])
                M.append(k)
                k=1
                pre=list[j]     
            j=j+1
        H.append(list[j-1])
        M.append(k)
        H.pop(0)
        M.pop(0)
        
        i=0
        while i<len(M):
            if M[i]==max(M):
                return H[i]
            i=i+1

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])

print longest_repetition([1,2,3,4,5])

print longest_repetition([])
