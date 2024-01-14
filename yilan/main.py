import turtle
import time
import random

hiz=0.30
pencere=turtle.Screen()            #pencere oluşturduk
pencere.title("Yilan Oyunu")       #pencere başlığı
pencere.bgcolor("lightgreen")      #pencerenin arka plan rengi
pencere.setup(width=600,height=600)#pencerenin boyutu
pencere.tracer(0)                  #pencere üzerinde güncelleme olmasın diye


#Yilan başi :D
yilanKafasi=turtle.Turtle()
yilanKafasi.speed(0)               #yilanın hızı
yilanKafasi.shape("square")        #yilanın kafasının şekli
yilanKafasi.color("black")         #yilanın kafasnın rengi
yilanKafasi.penup()                #yilan ilerlerken yazı yazmayacak
yilanKafasi.goto(0,100)      #yilan kafasının haraket boyutu
yilanKafasi.direction='stop'       #başlangıçta

yemek=turtle.Turtle()
yemek.speed(0)                   #yemek hızı
yemek.shape("circle")            #yemek  şekli
yemek.color("red")               #yemek  rengi
yemek.penup()                    #yemek  yazı yazmayacak
yemek.goto(0,0)            #yemek  haraket boyutu
yemek.shapesize(0.80,0.80)       #başlangıçta

yilaninKuyrugu=[]
puan=0

yaz=turtle.Turtle()
yaz.speed(0)                     #Yazı hızı
yaz.shape("square")              #Yazı  şekli
yaz.color("blue")               #Yazı  rengi
yaz.penup()
yaz.goto(0,260)            #yemek  haraket boyutu
yaz.hideturtle()                 #Herhangi bir şekli olmayacak
yaz.write("Puan : {}".format(puan),align='center',font=('Courier',24,'normal')) #Yazı tipi ve özellikleri


created=turtle.Turtle()
created.speed(0)                     #Yazı hızı
created.shape("square")              #Yazı  şekli
created.color("black")               #Yazı  rengi
created.penup()
created.goto(150,-290)            #yemek  haraket boyutu
created.hideturtle()                 #Herhangi bir şekli olmayacak
created.write("Created by Chubush".format(),align='center',font=('Italic',24,'normal')) #Yazı tipi ve özellikleri
def haraket():
    if yilanKafasi.direction=='up':
        y=yilanKafasi.ycor()
        yilanKafasi.sety(y+20)           #eğer yukarı haraket ederse 20px gitsin.
    if yilanKafasi.direction=='down':
        y=yilanKafasi.ycor()
        yilanKafasi.sety(y-20)
    if yilanKafasi.direction=='right':
        x=yilanKafasi.xcor()
        yilanKafasi.setx(x+20)
    if yilanKafasi.direction=='left':
        x=yilanKafasi.xcor()
        yilanKafasi.setx(x-20)

def yukari():
    if yilanKafasi.direction !='down':
        yilanKafasi.direction='up'

def asagi():
    if yilanKafasi.direction !='up':
        yilanKafasi.direction='down'

def saga():
    if yilanKafasi.direction !='left':
        yilanKafasi.direction='right'
def sola():
    if yilanKafasi.direction !='right':
        yilanKafasi.direction='left'

pencere.listen()
pencere.onkey(yukari,"Up")
pencere.onkey(asagi,"Down")
pencere.onkey(saga,"Right")
pencere.onkey(sola,"Left")

while True:
    pencere.update()

    if yilanKafasi.xcor()>300 or yilanKafasi.xcor()<-300 or yilanKafasi.ycor()>300 or yilanKafasi.ycor()< -300:
        time.sleep(1)
        yilanKafasi.goto(0,0)
        yilanKafasi.direction='stop'

        for kuyruk in yilaninKuyrugu:
            kuyruk.goto(1000,1000)

        yilaninKuyrugu=[]
        puan=0
        yaz.clear()
        yaz.write("Puan : {}".format(puan), align='center', font=('Courier', 24, 'normal'))  # Yazı tipi ve özellikleri
        hiz=0.30

    if yilanKafasi.distance(yemek) < 20: #eğer kafa ile yemek arasindaki mesafe 20px'den az ise
        x = random.randint(-250,250)  # rastgele sayi aralığı
        y = random.randint(-250,250)  # rastgele sayi aralığı
        yemek.goto(x,y)

        puan=puan+10
        yaz.clear()
        yaz.write("Puan : {}".format(puan), align='center', font=('Courier', 24, 'normal'))  # Yazı tipi ve özellikleri

        hiz=hiz-0.01



        #Yeni kuruğun özellikleri
        yeniKuyruk=turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape('square')
        yeniKuyruk.color('white')
        yeniKuyruk.penup()
        yilaninKuyrugu.append(yeniKuyruk)

    #Yeni kuyruğun eklenmesi
    for i in range(len(yilaninKuyrugu)-1,0,-1):
        x=yilaninKuyrugu[i-1].xcor()
        y=yilaninKuyrugu[i-1].ycor()
        yilaninKuyrugu[i].goto(x,y)

    if len(yilaninKuyrugu)>0:
       x =yilanKafasi.xcor()
       y =yilanKafasi.ycor()
       yilaninKuyrugu[0].goto(x,y)

    haraket()
    time.sleep(hiz)


