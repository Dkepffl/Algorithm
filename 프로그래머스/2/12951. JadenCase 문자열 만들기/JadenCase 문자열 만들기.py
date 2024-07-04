def solution(s):
    list_s = s.split(' ')
    ans=[]
    for word in list_s:
        if word == '':
            ans.append('')
        else:
            ans.append(word[0].upper() + word[1:].lower())
    return ' '.join(ans)
