def solution(arr):
    ans=[]
    for i in range(len(arr)):
        if i==0:
            ans.append(arr[i])
        elif arr[i-1]==arr[i]:
            continue
        else:
            ans.append(arr[i])
    return ans