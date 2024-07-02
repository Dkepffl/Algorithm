def solution(array, commands):
    ans=[]
    for i,j,k in commands:
        temp=array[i-1:j]
        temp=sorted(temp)
        ans.append(temp[k-1])
    return ans