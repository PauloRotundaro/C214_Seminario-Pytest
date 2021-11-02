import Calculadora.calculadora as c

class TestMultiplicacaoDivisao():
    def test_divisao(self):
        assert c.Calculadora.divisao(4, 2) == 2

    def test_multiplicacao(self):
        assert c.Calculadora.multiplicacao(12, 2) == 24

