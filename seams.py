import heapq

class Seam :
    def __init__ (self, pixels) :
        self.pixels = pixels
        self.energy = energy
        self.removed = false

class TestHeap :
    def __init__(self):
        self.h = []

    def add (self, edge) :
        heapq.heappush(self.h, edge)

    def get_top (self) :
        return (heapq.heappop(self.h))

# calculates the lowest seam starting at a given pixel with Dijkstra's
#helper methods may be added later

class Heap :

    def __init__(self):

        self.list = []

    def get_children(self, p) :
        if p*2+1 > len(self.list) :
            return []
        elif p*2+1 == (len(self.list) - 1) :
            return [p*2+1]
        else :
            return [p*2+1, p*2+2]

    def switch(self, p1, p2) :
        t = self.list[p1]
        self.list[p1] = self.list[p2]
        self.list[p2] = t

    def b_up(self, p) :
        if p == 0 :
            return
        elif p%2 == 0 :
            par = (p-2)/2
        else :
            par = (p-1)/2
        if self.list[par] > self.list[p] :
            self.switch(par,p)
            b_up(par)

    def b_down(self, p) :
        c = self.list[p].get_children
        if len(c) == 1 :
            if self.list[p] > c[0] :
                self.switch(p,c[0])
        elif len(self.list[p].get_children) == 2 :
            if self.list[p] > c[0] or self.list[p] > c[1] :
                if c[0] < c[1] :
                    self.switch(p,c[0])
                else :
                    self.switch(p,c[1])
            self.b_down(c[0])
            self.b_down(c[1])

    def add (self, edge) :
        self.list.append(edge)
        self.b_up (len(self.list)-1)

    def get_top (self) :
        val = self.list.pop(0)
        self.b_down (0)
        return val

class Edge :
    def __init__(self, source, sink, weight):

        self.source = source
        self.sink = sink
        self.weight = weight

    def __cmp__(self,other):
        return (self.weight - other.weight)
    
    def __str__(self):

        return "[%s]" % str(self.weight)
        
def seam_dijk (image, dir) :
    super_source = None
    heap = TestHeap ()
    def get_path(edge, path) :
        path.append(edge.sink)
        if edge.source is None:
            return path
        else :
            get_path(edge.source, path)

    for pix in image.top_vert_row(): #also do top horz rowm
        heap.add(Edge(None, pix, pix.energy))

    while True :
        edge = heap.get_top()

        if edge.sink.y == (image.height-1) :
            return (get_path(edge,[]))

        down =image.pixels[ (edge.sink.x, (edge.sink.y+1)) ]
        heap.add(Edge(edge, down, down.energy+edge.weight))

        if edge.sink.x == (image.width-1) :
            left = image.pixels[ ((edge.sink.x-1), (edge.sink.y+1)) ]
            heap.add(Edge(edge, left, left.energy+edge.weight))

        elif edge.sink.x == 0 :
            right = image.pixels[ ((edge.sink.x+1), (edge.sink.y+1)) ]
            heap.add(Edge(edge, right, right.energy+edge.weight))   
        else :
            left = image.pixels[ ((edge.sink.x-1), (edge.sink.y+1)) ]
            right = image.pixels[ ((edge.sink.x+1), (edge.sink.y+1)) ]
            heap.add(Edge(edge, right, right.energy+edge.weight))   
            heap.add(Edge(edge, left, left.energy+edge.weight)) 




# calculates the lowest seam starting at a given pixel with dynamic programming
#helper methods may be added later
def seam_dyn (image, pixel, dir) :
    raise NotImplementedError
    return seam





