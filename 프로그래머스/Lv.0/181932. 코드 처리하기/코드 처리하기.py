def solution(code):
    mode = 0
    ret=[]
    for idx in range(0,len(code)):
        if mode==0:
            if code[idx] == "1":
                mode = 1
            else:
                if idx%2==0:
                    ret.append(code[idx])
        elif mode==1:
            if code[idx] == "1":
                mode = 0
            else:
                if idx%2==1:
                    ret.append(code[idx])
    ret = ''.join(ret)
    return "EMPTY" if ret =='' else ret