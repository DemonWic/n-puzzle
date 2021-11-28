from tkinter import *

BOX_SIZE = 200
COLOR_BACK = '#E0ffff'
INFINITY = False
SPEED = 500  # ms

def visualuzation(array, puzzle_size):
    cnt = 0
    for ar in array:
        print(ar)
    # заводим ткинтер
    tkinter = Tk()
    # размер окна
    size = (BOX_SIZE * puzzle_size)
    # создание окна для вывода изображения
    canvas = Canvas(tkinter, width=size, height=size, bg=COLOR_BACK)
    canvas.pack()

    # подключаем кнопки
    tkinter.bind('<Escape>', ex)

    # запускаем цикл вывода собранных данных
    tkinter.after(0, update, tkinter, canvas, array, puzzle_size, cnt)
    # врубаем ткинтер на полную
    tkinter.mainloop()


def update(tkinter, canvas, array, puzzle_size, cnt):
    if INFINITY and cnt >= len(array):
        cnt = 0

    x = 0
    y = 0
    while y < puzzle_size:
        while x < puzzle_size:
            canvas.create_rectangle(BOX_SIZE * x + 5, BOX_SIZE * y + 5,
                                    BOX_SIZE * x + BOX_SIZE,
                                    BOX_SIZE * y + BOX_SIZE,
                                    fill=get_color(array[cnt], array[len(array) - 1], y * 3 + x))
            canvas.create_text((BOX_SIZE * (x + 1) - BOX_SIZE / 2, BOX_SIZE * (y + 1) - BOX_SIZE / 2),
                               text=array[cnt][y * 3 + x])
            x += 1
        y += 1
        x = 0
    cnt += 1

    tkinter.after(SPEED, update, tkinter, canvas, array, puzzle_size, cnt)
    canvas.update()

def get_color(cur, last, id):
    if cur[id] == 0:
        return 'white'
    if cur[id] == last[id]:
        return 'green'
    else:
        return 'black'

def ex(event):
    exit(0)


array = [[7, 8, 4, 3, 1, 5, 6, 2, 0],
         [7, 8, 4, 3, 1, 0, 6, 2, 5],
         [7, 8, 4, 3, 0, 1, 6, 2, 5],
         [7, 8, 4, 0, 3, 1, 6, 2, 5],
         [0, 8, 4, 7, 3, 1, 6, 2, 5],
         [8, 0, 4, 7, 3, 1, 6, 2, 5],
         [8, 3, 4, 7, 0, 1, 6, 2, 5],
         [8, 3, 4, 7, 1, 0, 6, 2, 5],
         [8, 3, 0, 7, 1, 4, 6, 2, 5],
         [8, 0, 3, 7, 1, 4, 6, 2, 5],
         [8, 1, 3, 7, 0, 4, 6, 2, 5],
         [8, 1, 3, 7, 2, 4, 6, 0, 5],
         [8, 1, 3, 7, 2, 4, 0, 6, 5],
         [8, 1, 3, 0, 2, 4, 7, 6, 5],
         [0, 1, 3, 8, 2, 4, 7, 6, 5],
         [1, 0, 3, 8, 2, 4, 7, 6, 5],
         [1, 2, 3, 8, 0, 4, 7, 6, 5]]

visualuzation(array, 3)
