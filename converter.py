
wires = []
hulls = []

def equalTuples(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

with open("D:\\FRC\\MiniPDU\\Wires.txt", 'r') as fob:
    for line in fob.readlines():
        line = line.strip()
        chunks = line.split(' ')
        chunks = [x.split('"') for x in chunks]
        #print(chunks)
        x1 = float(chunks[1][1])
        y1 = float(chunks[2][1])
        x2 = float(chunks[3][1])
        y2 = float(chunks[4][1])
        thisWire = ((x1, y1), (x2, y2))
        wires.append(thisWire)
        
#print(wires)
while True:
    if len(wires) == 0:
        break
        
    #Chose a wire
    thisHull = []
    startWire = wires.pop(0)
    startVertex = startWire[0]
    thisHull.append(startVertex)
    
    currentVertex = startWire[1]
    
    while True:
        thisHull.append(currentVertex)
        #make sure there's exactly one other wire with a vertex common with this one
        nextVertex = None
        nextWireIndex = None
        for i, wire in enumerate(wires):
            if equalTuples(wire[0], currentVertex):
                assert nextVertex is None
                nextVertex = wire[1]
                nextWireIndex = i
            elif equalTuples(wire[1], currentVertex):
                assert nextVertex is None
                nextVertex = wire[0]
                nextWireIndex = i
        wires.pop(nextWireIndex)
        if equalTuples(nextVertex, startVertex):
            print("Hull completed!")
            break
        currentVertex = nextVertex
    hulls.append(thisHull)
    
print(hulls)

with open("D:\\FRC\\MiniPDU\\foo.txt", 'w') as fob:
    for hull in hulls:
        fob.write('''<polygon width="0" layer="29">\n''')
        for vertex in hull:
            fob.write('''<vertex x="%f" y="%f"/>\n'''%(vertex[0], vertex[1]))
        fob.write('''</polygon>\n''')
    