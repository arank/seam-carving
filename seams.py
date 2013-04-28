import heapq


# test heap from standard pyhton lib for comaprison tests
class TestHeap :
    def __init__(self):
        self.h = []

    def add (self, edge) :
        heapq.heappush(self.h, edge)

    def get_top (self) :
        return (heapq.heappop(self.h))

# calculates the lowest seam starting at a given pixel with Dijkstra's
#helper methods may be added later

# min heap that stores edges for djikstras algorithm, given constant time
# lookup and log insert
class Heap :

    def __init__(self):

        self.list = []

    # gets childeren of the given heap branch
    def get_children(self, p) :
        if p*2+1 > (len(self.list)-1) :
            return []
        elif p*2+1 == (len(self.list)-1) :
            return [p*2+1]
        else :
            return [p*2+1, p*2+2]

    # swaps two elements in heap tree
    def switch(self, p1, p2) :
        t = self.list[p1]
        self.list[p1] = self.list[p2]
        self.list[p2] = t

    # bubbles up an element
    def b_up(self, p) :
        if p == 0 :
            return
        elif p%2 == 0 :
            par = (p-2)/2
        else :
            par = (p-1)/2
        if self.list[par] > self.list[p] :
            self.switch(par,p)
            self.b_up(par)
    #  pushes down an element
    def b_down(self, p) :
        c = self.get_children(p)
        if len(c) == 1 :
            if self.list[p] > self.list[c[0]] :
                self.switch(p,c[0])
        elif len(c) == 2 :
            if self.list[p] > self.list[c[0]] or self.list[p] > self.list[c[1]] :
                if self.list[c[0]] < self.list[c[1]] :
                    self.switch(p,c[0])
                    self.b_down(c[0])
                else :
                    self.switch(p,c[1])
                    self.b_down(c[1])
    # inserts element into heap
    def add (self, edge) :
        self.list.append(edge)
        self.b_up (len(self.list)-1)
    # removes and returns the top edge from the heap
    def get_top (self) :
        val = self.list[0]
        self.list[0] = self.list.pop()
        self.b_down(0)
        return val
# encapulates data that helps build the pixle array into a graph of valid directed paths
# with edge weights corresponding to energies of pixles
class Edge :
    def __init__(self, source, sink, weight):

        self.source = source
        self.sink = sink
        self.weight = weight
    # comapre function for use in heap comparisons
    def __cmp__(self,other):
        return (self.weight - other.weight)
    
    def __str__(self):

        return "[%s]" % str(self.weight)

# djikstras algorithm
def seam_dijk (image) :
    heap = TestHeap ()
    path =[]
    dic = {}
    prev ={}

    # extracts and returns final path from the path array
    def get_path(node) :
        path.append(prev[node])
        if prev[node] is None:
            # print [str(p) for p in path if len(path) > 900]
            return
        else :
            get_path(prev[node].pos)

    for pix in image.top_horz_row(): 
        heap.add(Edge(None, pix, pix.energy))
        dic[pix.pos]=pix.energy
        prev[pix.pos]=None

    # while (len(dic.keys())<(image.width*image.height)) :
    while True : 
        edge = heap.get_top()

        #nighbors
        neighbors = []
            
        if (edge.sink.pos[1] == (image.height-1)) :
            path.append(edge.sink)
            get_path(edge.sink.pos)
            return path
        else :
            neighbors.append(image.pixels[ (edge.sink.pos[0], (edge.sink.pos[1]+1)) ])
            if edge.sink.pos[0] == (image.width-1) :
                 neighbors.append(image.pixels[ ((edge.sink.pos[0]-1), (edge.sink.pos[1]+1)) ])

            elif edge.sink.pos[0] == 0 :
                 neighbors.append(image.pixels[ ((edge.sink.pos[0]+1), (edge.sink.pos[1]+1)) ])

            else :
                neighbors.append(image.pixels[ ((edge.sink.pos[0]-1), (edge.sink.pos[1]+1)) ])
                neighbors.append(image.pixels[ ((edge.sink.pos[0]+1), (edge.sink.pos[1]+1)) ])
        
        for n in neighbors:
            cost = (edge.weight+n.energy)
            if n.pos in dic:
                if (dic[n.pos] < cost):
                    continue
                else :
                    dic[n.pos] = cost
                    prev[n.pos] = edge.sink
                    heap.add(Edge(edge, n, cost))
            else :
                dic[n.pos] = cost
                prev[n.pos] = edge.sink
                heap.add(Edge(edge, n, cost))
            




# calculates the lowest seam starting at a given pixel with dynamic programming
#helper methods may be added later
def seam_dyn (image) :
    seam=[]

    #height = 128

    #answer to the previous subproblem
    #make 2d
    ans = [0]*(image.width)

    #array storing the paths
    paths = [[0 for x in range(image.height)] for y in range(image.width)]

    # gets the minimum index in a list of numbers given with an offset built in and defined by j
    def min_index (j, a):
        return j+(a.index(min(a)))
   
    for i in range(0, image.height) :
        ind = min_index(0, [ans[0], ans[1]])
        paths[0][i]= ind
        ans[0]=ans[ind]+image.pixels[(0,i)].energy

        for j in range(1, image.width-1) :
            ind = min_index(j, [ans[j-1],ans[j],ans[j+1]])
            paths[j][i]=ind-1
            ans[j]=ans[ind-1]+image.pixels[(j,i)].energy
        
        ind=min_index(image.width-1, [ans[image.width-2],ans[image.width-1]])
        paths[image.width-1][i]=ind-1    
        ans[image.width-1] = ans[ind-1]+image.pixels[(image.width-1,i)].energy

    ind = min_index(0, ans)

    for i in range(image.height-1,-1,-1):
        seam.append((ind,i))
        ind = paths[ind][i]

    return seam





