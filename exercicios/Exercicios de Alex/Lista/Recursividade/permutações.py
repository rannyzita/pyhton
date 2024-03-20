def permutacoes_string(string):
    
    if len(string) == 1:
        return string
    
    perms = []
    #range percorre cada caractere da string
    for i in range(len(string)):
        primeiro = string[i]
        resto = string[:i] + string[i+1:]
        for p in permutacoes_string(resto):
            perms.append(primeiro + p)
    
    return perms

string = input('Digite a palavra que você quer permutar: ')
resultado = permutacoes_string(string)
print(resultado)
