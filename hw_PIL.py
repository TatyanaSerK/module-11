from PIL import Image

img = Image.open("images.png")  # открывает изображение для работы

img.show()  # выводит на экран
x, y = img.size  # размеры изображения (кортеж)
new_img = img.resize((x * 2, y * 2))  # изменить размер
new_img.save("new_img.png") # сохраняет изображение
new_img.show()  # выводит на экран
rotat_img = img.rotate(180, expand=True) # поворот изображения

with Image.open("images.png") as pand:
    pand.load()
gray_img = pand.convert("L")  #оттенки серого
gray_img.show()  # выводит на экран



