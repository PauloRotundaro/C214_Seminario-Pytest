import Calculadora.calculadora as c
import pytest

def teste_soma():
    assert c.Calculadora.soma(1, 2) == 3

def teste_subtracao():
    assert c.Calculadora.subtracao(9, 3) == 6

def teste_subtracao_com_string():
    with pytest.raises(TypeError):
        c.Calculadora.subtracao(3, "2")