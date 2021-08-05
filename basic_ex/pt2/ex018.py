# // NAME:   MARCELLO B.
# // BACKUP: EX1

print('=-='*30)

download_size = float(input('INFORME A QUANTIA A SER BAIXADA (EM MB):'))
link_speed    = float(input('INFORME A VELOCIDADE DO LINK DE INTERNET (EM MBPS):'))

'''
*1024  = 1 mb
*1024 = 1 mb de link
'''

bits_size = (download_size * 1024 * 1024 * 8)
tempo     = bits_size / (link_speed * 1024 * 1024)
minutos   = tempo / 60

print(f'TEMPO DE DOWNLOAD: {minutos} minutos')

