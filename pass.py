import random
letras = '123456789qwertyuiopasdfghjklçzxcvbnm,.-:;<>/()=?«»!#$%&^~+*'
tamanho_pass = int(input('Qual tamanho deseja para a sua passe? '))
for l in range(0, tamanho_pass):
    escolha = random.choice(letras)
    for l in escolha:
        print(l, end='')
