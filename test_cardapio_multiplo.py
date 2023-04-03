# passo 01: importar pytest
import pytest

# passo 02: transformar o código em uma função
def cardapio(pedidos):
    
    # separar a entrada de dados da lógica do programa
    codigos = pedidos.split()
    total = 0.0
    for codigo in codigos:
        if codigo == '100':
            print('Você pediu um Cachorro Quente no valor de 9,00')
            total += 9.00
        elif codigo == '101':
            print('Você pediu um Cachorro Quente Duplo no valor de 11,00')
            total += 11.00
        elif codigo == '102':
            print('Você pediu um X-Egg no valor de 12,00')
            total += 12.00
        elif codigo == '103':
            print('Você pediu um X-Salada no valor de 12,00')
            total += 12.00
        elif codigo == '104':
            print('Você pediu um X-Bacon no valor de 14,00')
            total += 14.00
        elif codigo == '105':
            print('Você pediu um X-Tudo no valor de 17,00')
            total += 17.00
        elif codigo == '200':
            print('Você pediu um Refrigerante Lata no valor de 5,00')
            total += 5.00
        elif codigo == '201':
            print('Você pediu um Chá Gelado no valor de 4,00')
            total += 4.00
        else:
            print('Opção inválida')
            continue
    
    print(f'VALOR AQUI {total}')
    print(f'O total a ser pago é: {total:.2f} R$')

cardapio('100 101')

"""
# passo 03: analisar e comentar os inputs
def test_cardapio():
    assert cardapio('100 101 201') == 'O total a ser pago é: 24.00 R$'
    assert cardapio('102 103 104') == 'O total a ser pago é: 38.00 R$'
    assert cardapio('100 105 200 201') == 'O total a ser pago é: 35.00 R$'
    assert cardapio('999 105 200') == 'O total a ser pago é: 22.00 R$'
    assert cardapio('100') == 'O total a ser pago é: 9.00 R$'
"""