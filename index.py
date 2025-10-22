nome_hero = input('Digite o nome do Hero: ')
quantidade_xp = int(input('Informe a quantidade de XP do Hero: '))

print(nome_hero)

if quantidade_xp < 1000:
    print('Ferro')
    print(quantidade_xp)
elif quantidade_xp >= 1001 and quantidade_xp < 2000:
    print('Bronze')
    print(quantidade_xp)
elif quantidade_xp >= 2001 and quantidade_xp < 5000:
    print('Prata')
    print(quantidade_xp)
elif quantidade_xp >= 5001 and quantidade_xp < 6000:
    print('Ouro')
    print(quantidade_xp)
elif quantidade_xp >= 6001 and quantidade_xp < 8000:
    print('Platina')
    print(quantidade_xp)
elif quantidade_xp >= 8001 and quantidade_xp < 9000:
    print('Ascendente')
    print(quantidade_xp)
elif quantidade_xp >= 9001 and quantidade_xp < 10000:
    print('Imortal')
    print(quantidade_xp)
else:
    print('Radiante')
    print(quantidade_xp)

print('----------------------------------------------------------------------------')

print(f'O nome do Hero é {nome_hero} e sua quantidade de XP é {quantidade_xp}')