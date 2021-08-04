# // NAME:   MARCELLO B.
# // BACKUP: EX1

print('=-='*30)

size  = float(input('METROS² A SEREM PINTADOS :'))
lts   = (size/3)
latas = int(lts/18)

if  lts % 18 != 0:
    lts += 1

print('=-='*30)
print(f'VOCE TERA QUE COMPRAR {lts} LATAS')
print(f'SEU PREÇO TOTAL FICA EM {lts*80} reais')
print('--'*40)
