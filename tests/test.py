import unittest

from hawksoft.relation import Relation

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #print ("this setupclass() method only called once.\n")
        pass
    @classmethod
    def tearDownClass(cls):
        #print ("this teardownclass() method only called once too.\n")
        pass
    def setUp(self):
        #print ("do something before test : prepare environment.\n")
        pass
    def tearDown(self):
        #print ("do something after test : clean up.\n")
        pass
        
    def atest_Relation(self):
        Relation.setA(1,2,3)
        r1 = Relation((1,2),(2,3),(1,3),(2,1),(3,2),(3,1),name ='relation')
        #Relation.setA('a','b','c')
        #r1 = Relation(('a','b'),('a','c'),name ='first')
        #r1 = Relation(name ='first')
        r1.showSet()
        r1.showMatrix()
        r1.showGraph()
    def atest_universal(self):
        Relation.setA(1,2,3,4,5,6,7,8,9,10,11)
        r1 = Relation.getUniversal()
        r1.showSet()
        r1.showMatrix()
        r1.showGraph()

    def atest_sub(self):
        Relation.setA(1,2,3)
        r1 = Relation((1,2),(2,3),(1,3),(2,1),(3,2),(3,1),name ='relation')
        r2 = Relation((1,2),(2,3),(1,3))
        r3 = r1 -r2
        r3.showSet()
        r3.showMatrix()
        r3.showGraph()
    def atest_pow(self):
        Relation.setA(1,2,3)
        r1 = Relation((1,2),(2,3))
        r3 = r1 ** -1
        r3.showSet()
        r3.showMatrix()
        r3.showGraph()
    def atest_intersection(self):
        Relation.setA(1,2,3)
        r1 = Relation((1,2),(2,3))
        r2 = Relation((1,2))
        r3 = r1.intersect(r2)
        r3.showSet()
        r3.showMatrix()
        r3.showGraph()
    def atest_identity(self):
        Relation.setA(1,2,3,4,5,6,7,8,9,10,11)
        r1 = Relation.getIdentity()
        r1.showSet()
        r1.showMatrix()
        r1.showGraph()
    def test_closure(self):
        Relation.setA(1,2,3,4,5,6,7,8,9)
        r1 = Relation((1,2),(2,3),(4,5),(5,6),(6,7))
        r2 = r1.reflectiveClosure()
        r2.showSet()
        r3 = r2.symmetricClosure()
        r3.showSet()
        r4 = r3.transitiveClosure()
        r4.showSet()
        r4.showGraph()

        
if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)