a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
def pocet_znakov(veta):
    pole = veta.split(' ')
    print(f'Počet slov: {len(pole)}')
    cena = str(len(pole) / 10)
    pole = cena.split('.')
    if len(cena[1]) == 1:
        cena += '0'
    print(f'Cena SMS: {cena} €')
    veta = veta.upper()
    for i in range(len(a)):
        print(f'{a[i]} sa v SMS nachádza {veta.count(a[i])} - krát')


pocet_znakov('dnes je fest pekne')