big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
cisla = ['0','1','2','3','4','5','6','7','8','9']
out = ''
with open ("C:/Users/student/Documents/IV.B/Ondrej_Krajcovic/RPP/Maturitne otazky/textaky/list_txt_21.11'22_kraj_RPP_telegram2.txt",'r',encoding = 'utf-8') as subor:
    text = subor.readlines()
    text = text[0]
    for znak in text:
        if znak in big or znak in cisla:
            out += '_'
        else:
            out += znak
    print(out)
    
    
    
# subor:
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna eros quis urna.
# Nunc viverra imperdiet enim. Fusce est. Vivamus a tellus.
# Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin pharetra nonummy pede. Mauris et orci.
# Aenean nec lorem. In porttitor. Donec laoreet nonummy augue.
# Suspendisse dui purus, scelerisque at, vulputate vitae, pretium mattis, nunc. Mauris eget neque at sem venenatis eleifend. Ut nonummy.
