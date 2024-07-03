def solution(bridge_length, weight, truck_weights):
    on_bridge=[]
    out = []
    w=0
    t=0
    i=0
    
    while True:
        if len(on_bridge)==bridge_length:
            if on_bridge[0]!=0:
                out.append(on_bridge[0])
                w -=on_bridge[0]
            on_bridge.pop(0)
            
        front=truck_weights[i]
        
        if w+front > weight:
            on_bridge.append(0)
            t+=1
        else:
            on_bridge.append(front)
            w +=front
            t+=1
            if i+1 < len(truck_weights):
                i+=1  
        if len(out)==len(truck_weights):
            return t
        
        
            
