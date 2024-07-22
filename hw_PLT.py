import matplotlib.pyplot as plt



# построит график y(x)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [21, 52, 23, 25, 80, 22, 66, 45, 48, 21]
plt.plot(x, y)
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y
plt.title('Мой график') #Название
plt.show()

# столбчатая диаграмма
x = ['первый', 'второй', 'третий']
y = [99, 55, 88]
plt.bar(x, y, label='столбцы') #легенда графика
plt.xlabel('Ось Х') #Подпись для оси х
plt.ylabel('Ось У') #Подпись для оси y
plt.title('Столбчатая диаграмма') #Название
plt.legend()
plt.show()


#круговая диаграмма
vals = [25, 25, 20, 30]
labels = ["я", "ты", "он", "она"]
plt.pie(vals, labels=labels, autopct='%1.1f%%') #Подпись значения
plt.title("вместе дружная семья")  #Название
plt.show()