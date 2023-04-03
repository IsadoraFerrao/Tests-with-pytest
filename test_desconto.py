import pytest
def calculo_desconto(valor_unitario,quantidade):
    #valor_unitario = float(input('Valor unitário do produto: '))
    #quantidade = int(input('Quantidade: '))
    desconto = 1

    if quantidade >= 10 and quantidade <= 99:
        desconto = 0.95
    elif quantidade >= 100 and quantidade <= 999:
        desconto = 0.90
    elif quantidade >= 1000:
        desconto = 0.85

    valor_com_desconto = valor_unitario * desconto * quantidade
    valor_sem_desconto = valor_unitario * quantidade
    return valor_com_desconto

    #print(f'Valor total sem desconto: {valor_sem_desconto:.2f} R$')
    #print(f'Valor total com desconto: {valor_com_desconto:.2f} R$')
    
def test_calculo_desconto():
    assert calculo_desconto(100,300) == 27000