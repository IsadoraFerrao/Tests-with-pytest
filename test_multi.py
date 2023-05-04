import pytest 

def multiplicacao(x,y):
    multi = x*y
    return multi

#def test_multiplicacao():
    #assert multiplicacao(5,6) == 30
    #assert multiplicacao(5,6) == 31
    
def soma(x,y):
    soma = x+y
    return soma

def test_soma():
    assert soma(2,10) ==  12
    assert soma(5,10) == 15
    assert soma(10,10) == 20
    assert soma(10,2) == 15

# para rodar, pytest + nome_arquivo.py