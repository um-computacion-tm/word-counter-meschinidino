import unittest

from contar_palabras import contar_palabras


class MyTest(unittest.TestCase):
    def test_simple(self):
        resultado = contar_palabras("hola mundo")
        self.assertEqual(resultado, {"hola": 1,
                                     "mundo": 1
                                     })
    def test_complejo(self):
        resultado = contar_palabras("hola hola hola como estas todo bien bien vos bien tambien gracias")
        self.assertEqual(resultado, {"hola": 3,
                                      "como": 1,
                                      "estas": 1,
                                      "todo": 1,
                                      "bien": 3,
                                      "vos": 1,
                                      "tambien": 1,
                                      "gracias": 1
                                      })
if __name__ == '__main__':
    unittest.main()