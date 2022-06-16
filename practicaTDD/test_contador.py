import unittest

import contador
class Test_contador(unittest.TestCase):
    #Este es el primer test
    def test1(self):
    # Condiciones iniciales#
        contador1 = contador.Contador(0,2,5)
    #Verificar#
        self.assertEqual(contador1.get_inicial(),0)
        self.assertEqual(contador1.get_incremento(),2)
        self.assertEqual(contador1.get_limite(),1)


    def test2(self):
        
        c2=contador.Contador(limite=3)

        self.assertEqual(c2.inicial,0)
        self.assertEqual(c2.incremento,1)
        self.assertEqual(c2.limite,3)#

        

if __name__=="__main__":
    unittest.main()