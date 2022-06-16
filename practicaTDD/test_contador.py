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
        self.assertEqual(contador1.get_limite(),5)


    def test2(self):
        
        c2=contador.Contador(limite=3)

        self.assertEqual(c2.get_inicial(),0)
        self.assertEqual(c2.get_incremento(),1)
        self.assertEqual(c2.get_limite(),3)#

    def test3(self):
        contador3=contador.Contador()

        self.assertGreaterEqual(contador3.incremento(),0);

    def test4(self):
        contador4=contador.Contador(0,7,10)
        contador4.incremento()
        self.assertEquals(contador4.getContador(),0)

    def test5(self):
        contador5=contador.Contador(0,3,10)
        contador5.incremento()
        self.assertEquals(contador5.reiniciar(),0)

    def test6(self):
        contador6=contador.Contador(0,4,11)
        contador6.incremento();
        self.assertEquals(contador6.getContador(),4)

if __name__=="__main__":
    unittest.main()