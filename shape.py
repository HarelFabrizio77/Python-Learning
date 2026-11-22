import turtle
while True: 
    hud = turtle.Screen()
    hud.title("Drawing App")
    hud.bgcolor("white")
    pen = turtle.Turtle()
    pen.pensize(10)
    pen.speed(3)

    sidelength = int(input("Length: "))
    color = input("Color: ")

    if color == "red":
        pen.pencolor("red")
    elif color == "black":
        pen.pencolor("black")
    elif color == "blue":
        pen.pencolor("blue")
    elif color == "green":
        pen.pencolor("green")
    else:
        print("That ain't a color")

    shape = input("What shape: ")

    def triangle(side_length):
        for x in range(3):
            pen.forward(sidelength)
            pen.right(120)

    def hexagon():
        for x in range(6):
            pen.forward(sidelength)
            pen.right(60)

    def pentagon():
        for x in range(5):
            pen.forward(sidelength)
            pen.right(72)

    def square():
        for x in range(5):
            pen.forward(sidelength)
            pen.right(90)

    if shape == "square" or shape == "Square":
        square()
    elif shape == "hexagon" or shape == "Hexagon":
        hexagon()
    elif shape == "triangle" or shape == "Triangle":
        triangle()
    elif shape == "pentagon" or shape == "Pentagon":
        pentagon()

    hud.exitonclick() 
