
newEngland = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]

def problem2_3(ne):
    
    for i in range(len(ne)):
        ct = 0
        print(ne[i],end=" ")
        print("has",end=" ")
        for x in ne[i]: 
            if x !='~': 
                ct = ct + 1
        print(ct,"letters.")
    