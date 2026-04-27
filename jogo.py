from random import randint  
 
while True:
    escolha = input('Par ou Impar? [P/I]: ').upper()
    if escolha not in ['P', 'I']:
        print('Escolha inválida!')
        continue
    
    jogador = int(input('Digite um valor (0-10): '))
    if not 0 <= jogador <= 10:
        print('Valor inválido!')
        continue
    
    computador = randint(0,10)
    total = jogador + computador
    tipo = "P" if total % 2 == 0 else "I"
    
    print(f'Você jogou {jogador}, computador {computador}. Total {total} = {tipo}')
    
    if escolha == tipo:
        print('Você GANHOU!')
    else:
        print('Você PERDEU!')
    
    continuar = input('Quer continuar? [S/N]: ').upper()
    if continuar == 'N':
        break

print('Fim de jogo!')
