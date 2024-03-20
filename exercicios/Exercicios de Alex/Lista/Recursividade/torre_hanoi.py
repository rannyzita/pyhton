def torres_de_hanoi(N_discos, pino_a='A', pino_b='B', pino_c='C'):
    
    if N_discos == 1:
        print(f'Mover disco 1 do pino {pino_a} para o pino {pino_c}')
        return
        
    torres_de_hanoi(N_discos - 1, pino_a, pino_b, pino_c)
    
    print(f'Mover disco {N_discos} do pino {pino_a} para o pino {pino_c}')
    
    torres_de_hanoi(N_discos - 1, pino_b, pino_c, pino_a)

N_discos = int(input('Digite a quantidade de discos: '))
torres_de_hanoi(N_discos)
