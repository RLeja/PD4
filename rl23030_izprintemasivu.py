def printmasivs(masivs):
    for elements in masivs:
        print(elements)

def geoprintmasivs(masivs):
    if(len(masivs)<=0): return 
    prev = masivs[0]
    print(prev)
    for i in range(1,len(masivs)):
        prev+=masivs[i]
        print(prev)