import random
escolha = ''
letras = '123456789qwertyuiopasdfghjklçzxcvbnm,.-:;<>/()=?«»!#$%&^~+*'
tamanho_pass = int(input('Qual tamanho deseja para a sua passe? '))
print('Sua passe é a seguinte: ', end='')
for l in range(1, tamanho_pass + 1):
    escolha = random.choice(letras)
    print(escolha, end='')
