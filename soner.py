import turtle
import time

# Tam ekran ve siyah arka plan
ekran = turtle.Screen()
ekran.setup(width=1.0, height=1.0)  # Ekranı tam ekran gibi yap
ekran.bgcolor("black")
ekran.title("Soner Çelebi & Pornhub")

# Çizimi gizle, sonra topluca göster
turtle.tracer(0)

kalem = turtle.Turtle()
kalem.hideturtle()
kalem.penup()
kalem.color("white")
kalem.speed(0)

# Harf aralığı
harf_araligi = 18

# SONER ÇELEBİ
metin = "Soner Çelebi"
kalem.goto(-120, 50)
for harf in metin:
    kalem.write(harf, font=("Arial", 24, "bold"))
    kalem.forward(harf_araligi)
    time.sleep(0.05)

# PORNHUB
kalem.goto(-60, -20)
kalem.color("white")
kalem.write("Porn", font=("Arial", 36, "bold"))

kalem.goto(55, -20)
kalem.color("orange")
kalem.write("hub", font=("Arial", 36, "bold"))

turtle.update()  # Her şeyi bir anda göster
turtle.done()
