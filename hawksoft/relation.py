import sympy
from sympy.abc import x,y
import graphviz as gz
class Relation(sympy.FiniteSet):
    def __init__(self,*items,name='noName',index = None):
        sympy.FiniteSet(self,*items)
        self.name = name
        if index == None:
            self.findAB()
        else:
            self.id2items = index
    def findAB(self):
        self.A = sympy.FiniteSet()
        self.B = sympy.FiniteSet()
        for i in self:
            self.A = self.A.union(sympy.FiniteSet(i[0]))
            self.B = self.B.union(sympy.FiniteSet(i[1]))
        self.C = self.A.union(self.B)
        self.id2items= {}
        num  = 0
        for i in self.C:
            self.id2items[num] = i
            num = num + 1
    def get_index(self):
        return self.id2items
    def findC(self):
        ta = sympy.ImageSet(sympy.Lambda(x,x),self)
        #ta = sympy.ConditionSet(x,sympy.(x),self)
        print(ta)
        for i in ta:
            print(i[0],i[1])
    def show(self):
        print("{} = ".format(self.name),end="{ ")
        for i in self:
            print(i,end=" ")
        print("}\n")
    def drawGraph(self):
        g = gz.Graph(format='png')
        for i in self.C:
            g.node(str(i))
        l = []
        for i in self:
            l.append(str(i[0])+str(i[1]))
        g.edges(l)
        #print(g.source)
        g.render('./test',view=True) 
    def drawDigraph(self):
        g = gz.Digraph(format='png')
        for i in self.A:
            g.node(str(i))
        l = []
        for i in self:
            l.append(str(i[0])+str(i[1]))
        g.edges(l)
        #print(g.source)
        g.render('./test',view=True) 
    def __sub__(self,subs):
        temp = sympy.Complement(self,subs)
        l = []
        for i in temp:
            l.append(i)
        result = Relation(*l) 
        return result
    def __add__(self,adds):
        temp = self.union(adds)
        l = []
        for i in temp:
            l.append(i)
        result = Relation(*l) 
        return result
    def toMatrix(self):
        mat = []
        for i in range(0,len(self.id2items)):
            line = []
            for j  in range(0,len(self.id2items)):
                item = (self.id2items[i],self.id2items[j])
                if self.contains(item)==True:
                    line.append(1)
                else:
                    line.append(0)
            mat.append(line)
        self.matrix = sympy.Matrix(mat)
        return self.matrix
    def fromMatrix(self,matrix):
        l = []
        for i in range(0,len(self.id2items)):
            rows = matrix.row(i)
            for j in range(0, len(self.id2items)):
                if rows[j] == 1:
                    item = (self.id2items[i],self.id2items[j])
                    l.append(item)
        return Relation(*l)
    def identity(self):
        l = []
        for i in range(0,len(self.id2items)):
             item = (self.id2items[i],self.id2items[i])
             l.append(item)
        return Relation(*l)
    def converse(self):
        mat1 = self.toMatrix()
        mat2 = mat1.T
        return self.fromMatrix(mat2)
    def compound(self,num):
         mat = self.toMatrix()
         mat = mat**num
         return self.fromMatrix(mat)
    def refClosure(self):
        return self + self.identity()
    def symClosure(self):
        return self + self.converse()

