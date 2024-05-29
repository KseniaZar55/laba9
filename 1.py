import os
from PIL import Image
def h1():
    for i in os.listdir("kartinki"):
        img = Image.open("kartinki/" + i)
        img = img.resize((img.width // 3, img.height // 3))
        img.save("mau/img" + i)

def h2():
    for i in os.listdir('kartinki'):
        if i.endswith('.jpg') or i.endswith('.png'):
            img = Image.open("kartinki/" + i)
            img = img.resize((img.width // 3, img.height // 3))
            img.save("mau/img" + i)

def h3():
    import csv
    itog=0
    print('нужно купить:')
    with open('data.csv') as file:
        file = csv.reader(file)
        for i in file:
            name=i[0]
            kolvo=int(i[1])
            cn=int(i[2])
            itog+=kolvo*cn
            print(i[0] + "-"+ i[1] + "шт" + " " +i[2] + " руб.")
    print("итог:" + str(itog))

h3()
