pismena = [' ', ',','.','-','!','?',':',';', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spolu = 0
with open ("C:/Users/ondrej/Documents/school/IV.B GAM/RPP/Python/DU/txt/list_txt_17.11'22_kraj_RPP_telegram3.txt",'r',encoding = 'utf-8') as subor:
    text = subor.readlines()
    text = text[0]
for i in range(len(pismena)):
    print(f'{pismena[i]} sa v texte nachádza {text.count(pismena[i])} - krát')

    # subor:
    # Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna eros quis urna.
    # Nunc viverra imperdiet enim. Fusce est. Vivamus a tellus.
    # Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin pharetra nonummy pede. Mauris et orci.
    # Aenean nec lorem. In porttitor. Donec laoreet nonummy augue.
    # Suspendisse dui purus, scelerisque at, vulputate vitae, pretium mattis, nunc. Mauris eget neque at sem venenatis eleifend. Ut nonummy.