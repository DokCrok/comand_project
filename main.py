from random import choice, randint
from tkinter import *

window = Tk()
window.title("Random Weather")
window.geometry("500x400")

canvas = Canvas(width=500, height=400, bg="#fff7f9")
canvas.pack()

t = 0
g = 0

canvas.create_rectangle(90, 90, 410, 110, outline="#ff94c9")

b = canvas.create_text(250, 100, text="Press 'Space' button to generate weather")
x = canvas.create_text(450, 390, text="Made by Anna")


def random_weather(event):
    canvas.create_rectangle(90, 190, 410, 230, outline="#ff94c9")
    global t, g
    canvas.delete(t)
    canvas.delete(g)

    temperature = randint(-20, 40)

    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    months = (
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
    "December")
    weather = ("sunny", "cloudy", "rainy", "windy", "snowy", "stormy")
    number = []

    for i in range(1, 32):
        number.append(i)

    random_month = choice(months)
    random_number = choice(number)
    random_day = choice(days)
    random_weather = choice(weather)

    while random_number > 29 and random_month == 'February':
        random_month = choice(months)
        random_number = choice(number)

    while random_number > 30 and random_month == "September":
        random_number = choice(number)

    while random_number > 30 and random_month == "November":
        random_number = choice(number)

    while random_number > 30 and random_month == "April":
        random_number = choice(number)

    while random_number > 30 and random_month == "June":
        random_number = choice(number)

    if temperature > 1:
        month_temp = ["March", "April", "May", "June", "July", "August"]
        random_month = choice(month_temp)

    if temperature < 1:
        month_temp = ["January", "February", "September", "October", "November", "December"]
        random_month = choice(month_temp)

    if random_weather == "snowy":
        month_temp = ["January", "February", "November", "December"]
        temperature = randint(-25, 0)
        random_month = choice(month_temp)

    t = canvas.create_text(250, 200, text="Temperature on " + str(random_month) + ", " + str(
        random_number) + ", " + random_day + " is: " + str(temperature) +
                                          " degrees.")
    g = canvas.create_text(250, 220, text="Weather is: " + str(random_weather) + '.')


canvas.bind_all('<space>', random_weather)

mainloop()