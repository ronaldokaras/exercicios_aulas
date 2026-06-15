
email = 'ronaldo@gmail.com'
print(len(email)) # contagem completa
print(email[4]) # isolar letra 
print(email[-4:]) # contagem negativa
print(email[2:10]) # contagem a partir do n ate o final:


texto = 'AbcD.ddda'
print(texto.capitalize()) # deixa a primeira maisculas 
print(texto.casefold()) # deixa todas minusculas
print(texto.upper()) # deixa todas maisculas 
print(texto.title()) # deixa a primeira em cada palavra maisculas 
print(texto.count()) # conta ocorrencia '.'
print(texto.find()) # posição de um txt
print(texto.replace()) # substitui o txt 
print(texto.strip()) # remove espaço em branco
print(texto.split()) # divide string
print(texto.startswith()) # verifica inicio
print(texto.endswith()) # verifica o fim
print(texto.isalnum()) # so letra e numero?
print(texto.isalpha()) # so letra?
print(texto.isnumeric()) # so numero? 

#formatação alinhamento
print('{:>30}'.format('texto')) # direita
print('{:<30}'.format('texto')) # esquerda
print('{:^30}'.format('texto')) # centro

#fromatação numero
print('{:,.2f}'.format(27000)) # 27,000.00
print('{:+.2f}'.format(-230)) # -230.00
print('{:,.2f}'.format(0.6154)) # 61.54%