import unittest
from translator import trans1.trans2
class test translator (unittest.TestCase):
def test.trans1(self):
self assert Equal (trans1(0,'yes'),'oui')

def test.trans2(self):
self assert Equal (trans2(1,'oui'),'yes')


def test.trans1(self):
self assert Not Equal (trans1(0,'yes'),'oui')

def test.trans2(self):
self assert Not Equal (trans2(1,'oui'),'yes')




if __name__='__main__':
unittest.main()
