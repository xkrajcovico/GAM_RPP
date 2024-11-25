interpunk = [',','.','-','!','?',':',';']
samo = ['a','e','i','o','u','y']
spolu = 0
with open ("C:/Users/ondrej/Documents/school/IV.B GAM/RPP/Python/DU/txt/list_txt_17.11'22_kraj_RPP_telegram1.txt",'r',encoding = 'utf-8') as subor:
    text = subor.readlines()
    text = text[0]
    for i in range(len(interpunk)):
        print(f'{interpunk[i]} sa v texte nachádza {text.count(interpunk[i])} - krát')
        spolu += text.count(interpunk[i])
    print(f'počet medzier v texte je: {text.count(" ")}')
    for i in range(len(samo)):
        print(f'{samo[i]} sa v texte nachádza {text.count(samo[i])} - krát')
    print(f'spolu je v texte {spolu} interpunkčných znamienok')
    print(f'splu je v texte {len(text)} znakov')
    
    
    
# subor:
# Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna eros quis urna.
# Nunc viverra imperdiet enim. Fusce est. Vivamus a tellus.
# Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin pharetra nonummy pede. Mauris et orci.
# Aenean nec lorem. In porttitor. Donec laoreet nonummy augue.
# Suspendisse dui purus, scelerisque at, vulputate vitae, pretium mattis, nunc. Mauris eget neque at sem venenatis eleifend. Ut nonummy.
