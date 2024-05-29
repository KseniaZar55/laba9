def h1():
    import os
    from PIL import Image
    os.mkdir('mau')
    k=0
    for i in os.listdir('laba9'):
        img = Image.open("C:\Users\Vladik\Documents\laba9")
        img = img.resize((img.width // 3, img.height // 3))
        k+=1
        img.save("C:\Users\Vladik\Documents\laba9\mau\img" + i + ".jpg")

def h2():
    k=1
    import os
    from PIL import Image
    os.mkdir('pupusiki')
    for i in os.listdir('laba9'):
        if i.endswith('.jpg') or i.endswith('.png'):
            img = Image.open(i)
            img = img.resize((img.width // 3, img.height // 3))
            img.save("D:\питон\pupusiki\img" + str(k) + ".jpg")
            k+=1

def h3():
    import csv
    itog=0
    print('покупки :')
    with open('data.csv') as file:
        file = csv.reader(file)
        for i in file:
            name=i[0]
            kol=int(i[1])
            cn=int(i[2])
            itog+=kolvo*cn


h1()