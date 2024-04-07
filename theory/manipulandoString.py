# Trabalhando com Strings 

# Trabalhando com Fatiamento: 

'''
    Regras para fatiamento:
        name[5] -> Pega o caracter contido no espaco de posicao 5 no array string => l
        name[0:6] -> Fatia tudo o que estiver entre o caractere na posicao 0 ate a 5 => Rafael (ele nao considera o ultimo caractere)
        name[0:12:2] ->Fatia do caractere na posicao 0 ate a posicao 12 pulando de 2 em 2 caracteres. 
        name[:5] -> Fatia do caractere 0 ate o de posicao 4
        name[ 7:] -> Fatia do caractere na posicao 7 ate o final da string
        name[9::3] -> Fatia do caractere na pocisao 9 e vai ate o final, pulando de 3 em 3
'''

# Analise 
'''
    name.count('o',0,13) -> Ele conta do caractere 0 ao 13 quantas letras 'o' sao encontradas
    name.find('deo') -> Ele indica em que posicao a string entre parenteses e iniciada 
        => Nota: se voce receber o valor -1 significa que a string entre parenteses nao foi encontrada na string analisada 
    'Rafael' in name -> valida se existe a string (Rafael) dentro da string analisada 
    name.replace('Rafael','Joao') -> Replace significa trocar. Nesse caso o replace vai substituir uma string pela outra.
    name.upper() -> deixa todas as strings em maiucula 
    name.lower() -> deixa todas as strings em minusculas 
    nome.capitalize() -> deixa a primeira letra de cada palavra em maiuscla 
    name.title() -> deixa a primeira letra de cada palavra em maiuscla 
    name.stripe() -> remove todos os espacos inuteis, no inicio e no final da string 
    name.rstrip() -> remove o espaco do lado direito da string 
    name.lstrip() -> remove o espaco do lado esquerdo da string

# Divisao

    name.split() -> cria uma divisao onde existe espacos da string (PESQUISAR)

# Juncao

    '-'.join(name) -> vai juntar todos os elementos da string separando-os com o traco indicado entre aspas simples

'''

name = 'Rafael Dantas Gomes de Araujo Sather'

print(name[4:23])
print(name[:23])
print(name[0:])
print(name[0::2])
print(name.count('a'))
print(name.upper()) 
