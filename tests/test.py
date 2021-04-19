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
        
    def test_Relation(self):
        r1 = Relation((1,2),(2,3),(1,3),(2,1),(3,2),(3,1),name ='relation')
        #r1 = Relation(('a','b'),('a','c'),name ='first')
        r1.showSet()
        r1.showMatrix()
        r1.showGraph()
        
    def atest_toMatrix(self):
        r1 = Relation(('a','b'),('a','c'))
        r1.show()
        print(r1.toMatrix())
    def atest_fromMatrix(self):
        r1 = Relation((1,2),(2,3),(1,3),(2,1),(3,2),(3,1))
        #r1 = Relation(('a','b'),('a','c'))
        r2 = r1.fromMatrix(r1.toMatrix())
        print('test here')
        r2.show()
    def atest_identity(self):
        r1 = Relation((1,2),(2,3),(1,3),(2,1),(3,2),(3,1))
        print(r1.identity())
    def atest_converse(self):
        r1 = Relation((1,2),(2,3))
        print(r1.converse())
    def atest_compound(self):
        r1 = Relation((1,2),(2,3),(1,3))
        r2 = r1.compound(2)
        r2.show()
    def atest_closure(self):
        r1 = Relation((1,2),(2,3),(1,3))
        r2 = r1.refClosure()
        r2.show()
        r3 = r1.symClosure()
        r3.show()

        
if __name__ == '__main__':
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=1)