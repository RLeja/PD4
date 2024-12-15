def printmasivs(masivs):
    for elements in masivs:
        print(elements)

def oprintmasivs(masivs):
    for i in range(len(masivs)-1, 0, -1):
        print(masivs[i])
        
def geoprintmasivs(masivs):
    if(len(masivs)<=0): return 
    prev = masivs[0]
    print(prev)
    for i in range(1,len(masivs)):
        prev+=masivs[i]
        print(prev)
