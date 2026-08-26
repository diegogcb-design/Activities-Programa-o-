
from turtle import *
from time import sleep

t = Turtle()



# Bandeira do Reino Unido
# 1.Fundo azul
t.penup()
t.goto(-300, -150)
t.pendown()
t.color("#00247D")
t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.left(90)
    t.fd(300)
    t.left(90)
t.end_fill()

# 2. Diagonais Brancas 
t.color("#FFFFFF")
t.pensize(50)

t.penup()
t.goto(-300, -150)
t.pendown()
t.goto(300, 150)

t.penup()
t.goto(-300, 150)
t.pendown()
t.goto(300, -150)

# 3. Diagonais Vermehlas
t.color("#C2112C")
t.pensize(18)

# Superior izquerda a inferior direita
t.penup()
t.goto(-280, 140)
t.pendown()
t.goto(0, 0)

t.penup()
t.goto(0, 0)
t.pendown()
t.goto(280, -140)

# Inferior izquerda a superior direita
t.penup()
t.goto(-280, -140)
t.pendown()
t.goto(0, 0)

t.penup()
t.goto(0, 0)
t.pendown()
t.goto(280, 140)

# 4. Cruz branca pra o fundo
t.pensize(1)
t.penup()
t.goto(0, -150)
t.pendown()
t.color("#FFFFFF")
t.begin_fill()
t.setheading(0)
t.fd(50)
t.left(90)
t.fd(100)
t.right(90)
t.fd(250)
t.left(90)
t.fd(100)
t.left(90)
t.fd(250)
t.right(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.right(90)
t.fd(250)
t.left(90)
t.fd(100)
t.left(90)
t.fd(250)
t.right(90)
t.fd(100)
t.left(90)
t.fd(50)
t.end_fill()

# 5. Cruz vermehla
t.penup()
t.goto(0, -150)
t.pendown()
t.color("#C2112C")
t.begin_fill()
t.setheading(0)

t.fd(30)
t.left(90)
t.fd(120)
t.right(90)
t.fd(270)
t.left(90)
t.fd(60)
t.left(90)
t.fd(270)
t.right(90)
t.fd(120)
t.left(90)
t.fd(60)
t.left(90)
t.fd(120)
t.right(90)
t.fd(270)
t.left(90)
t.fd(60)
t.left(90)
t.fd(270)
t.right(90)
t.fd(120)
t.left(90)
t.fd(30)

t.end_fill()

sleep(2)
t.clear()

# Bandeira da Inglatera
t.penup()
t.goto(0, -150)
t.pendown()
t.color("#C2112C")
t.begin_fill()
t.setheading(0)

t.fd(30)
t.left(90)
t.fd(120)
t.right(90)
t.fd(270)
t.left(90)
t.fd(60)
t.left(90)
t.fd(270)
t.right(90)
t.fd(120)
t.left(90)
t.fd(60)
t.left(90)
t.fd(120)
t.right(90)
t.fd(270)
t.left(90)
t.fd(60)
t.left(90)
t.fd(270)
t.right(90)
t.fd(120)
t.left(90)
t.fd(30)
t.end_fill()

t.penup()
t.goto(0,-150)
t.pendown()
t.color("black")

t.setheading(0)

t.fd(300)
t.left(90)
t.fd(300)
t.left(90)
t.fd(600)
t.left(90)
t.fd(300)
t.left(90)
t.fd(300)



sleep(2)
t.clear()

mainloop()