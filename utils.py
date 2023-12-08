import turtle
import itertools

def secret_message():
    phrase = 'Cats are cute!'
    color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    font_size = 40  # Adjusted font size
    spacing = 40  # Adjust the spacing between characters

    turtle.speed(1)
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.bgcolor("black")  # Set background color
    color_cycle = itertools.cycle(color_list)

    for char in phrase:
        color = next(color_cycle)
        turtle.color(color)
        turtle.write(char, font=("Courier", font_size, "normal"))
        turtle.forward(spacing)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    secret_message()
