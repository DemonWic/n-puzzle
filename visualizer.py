from tkinter import *

BOX_SIZE = 200
COLOR_BACK = '#E0ffff'
INFINITY = False
SPEED = 500  # ms


def visualuzation(array, puzzle_size):
    cnt = 0
    # for ar in array:
    #     print(ar)
    # заводим ткинтер
    tkinter = Tk()
    tkinter.title("n-puzzle")
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
                               text=array[cnt][y * 3 + x], font=("Courier", 50))
            x += 1
        y += 1
        x = 0
    cnt += 1

    if cnt < len(array):
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

