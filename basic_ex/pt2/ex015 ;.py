# // NAME:   MARCELLO B.
# // BACKUP: EX1

print('=-='*30)
print('CALCULADORA DE SALARIOS')
print('-'*50)

q = float(input('QUANTO VOCÊ GANHA POR HORA ?'))
print('-'*50)

h = float(input('QUANTAS HORAS VOCE TRABALHA POR MÊS ?'))

salario_bruto = (q*h)
inss = (salario_bruto*8)/100
sindicato  = (salario_bruto*5)/100
salario_liquido = (salario_bruto-inss-sindicato)


print('=-='*30)
print('SALARIO BRUTO :', salario_bruto, 'R$')
print('INSS :', inss, 'R$')
print('SINDICATO :', sindicato, 'R$')
print('SALARIO LIQUIDO :', salario_liquido, 'R$')

print('=-='*30)
print('FIM')
print('-'*50)




