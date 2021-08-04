# // NAME:   MARCELLO B.
# // BACKUP: EX1

print('=-='*30)

peso = float(input('INSIRA A QUANTIDADE POR KG  :'))
multa = 4
peso_limite = 50

if peso > peso_limite:
    x = (peso - peso_limite)

    print('PESO EXCEDENTE :',  x)
    print('VALOR DA MULTA :', x*multa)

else:
    print('SEM EXCESSO! BOM TRABALHO!')
