# Aprendendo e praticando o uso de If e Else em Python

name = str(input('Informe seu nome: ').capitalize())
orientation_sex = str(input('Como voce gostaria de ser identificado: M - masculino / F - feminino ').upper())

if orientation_sex == 'M':
    print('Como vai {}, como posso ajuda-lo?'.format(name))
else:
    print('Como vai {}, como posso ajuda-la?'.format(name))

 # Condicao simplificada