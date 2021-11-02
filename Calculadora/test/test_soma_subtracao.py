import Calculadora.calculadora as c
import pytest

class TestSomaSubtracao():
    def test_soma(self):
        assert c.Calculadora.soma(1, 2) == 3

    def test_subtracao(self):
        assert c.Calculadora.subtracao(9, 3) == 12

    def test_subtracao_com_string(self):
        with pytest.raises(TypeError):
            c.Calculadora.subtracao(3, "2")


