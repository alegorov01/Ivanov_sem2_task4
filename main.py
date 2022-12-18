import turtle as tur

def curve(iter):
    if(iter < 0):
        tur.forward(size)
        return None
    curve(iter-1)
    tur.right(45)
    tur.forward(size)
    tur.right(45)
    curve(iter-1)
    for i in range(3):
        tur.left(45)
        tur.forward(size)
    tur.left(45)
    curve(iter-1)
    tur.right(45)
    tur.forward(size)
    tur.right(45)
    curve(iter-1)


def draw(iter):
    for i in range(4):
        curve(iter-1)
        tur.right(45)
        tur.forward(size)
        tur.right(45)
# Конфигурация
iter = 5
size = 5
tur.tracer(1000)

# Начало для черепашки
offset=70

tur.setpos(-(offset+1)*size,(offset+1)*size)
tur.clear()

#Рисуем
draw(iter)

tur.mainloop()