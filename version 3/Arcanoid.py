from random import*
from tkinter import*
from time import*
from winsound import* #импортируем музыку
from threaded import* #импортируем поток
class ball:
    def __init__(s,x,y,p,r,c):
        s.x=x
        s.y=y
        s.p=p #скорость шарика
        s.r=r #радиус
        s.n=randint(1,2)#направление движения шарика
        s.c=c #цвет
        s.o=w.create_oval(x-r,y-r,x+r,y+r,fill=c,outline='#000000') #рисуем объект
    def move(s):
        s.p=spb #spb глобальная переменная
        if s.n==1:
            s.x-=s.p
            s.y-=s.p
            return(-s.p,-s.p)
        elif s.n==2:
            s.x+=s.p
            s.y-=s.p
            return(s.p,-s.p)
        elif s.n==3:
            s.x+=s.p
            s.y+=s.p
            return(s.p,s.p)
        elif s.n==4:
            s.x-=s.p
            s.y+=s.p
            return(-s.p,s.p)
    def wall(s):
        if s.x-s.r<=0:
            if s.n==1:s.n=2
            if s.n==4:s.n=3
        elif s.x+s.r>=wid: #ширина экрана
            if s.n==2:s.n=1
            if s.n==3:s.n=4
        if s.y-s.r<=0:
            if s.n==2:s.n=3
            if s.n==1:s.n=4
        elif s.y+s.r>=heg: #высота экрана
            if s.n==3:s.n=2
            if s.n==4:s.n=1
    def plat(s,pl):
        if s.y+s.r>pl.y-pl.he/2: #and s.y-s.r<pl.y+pl.he/2:
            if s.x+s.r-(pl.x-pl.wi/2)>0 and s.x+s.r-(pl.x-pl.wi/2)<0.005*wid: #проверка, что бы шарик по абсциссе был внутри платформы
                if s.n==3:s.n=4
                if s.n==2:s.n=1
            elif pl.x+pl.wi/2-(s.x-s.r)>0 and pl.x+pl.wi/2-(s.x-s.r)<0.005*wid:
                if s.n==4:s.n=3
                if s.n==1:s.n=2
        if s.y+s.r-(pl.y-pl.he/2)>0 and s.y+s.r-(pl.y-pl.he/2)<0.005*wid:#отталкивание от бока платформы
            if s.x>pl.x-pl.wi/2 and s.x<pl.x+pl.wi/2:
                if s.n==3:s.n=2
                if s.n==4:s.n=1
    def inr(s,a,b,c):
        if a>=b and a<=c or a>=c and a<=b:
            return True
    def box(s,bx): #шарик внутри коробки
        if s.inr(s.x+s.r,bx.x-bxw/2,bx.x+bxw/2) and s.inr(s.y,bx.y-bxh/2,bx.y+bxh/2):
            if s.n==2:#левый бок коробки
                s.n=1
            if s.n==3:#левый бок с другой стороны
                s.n=4
            w.delete(bx.o)
            bx.x=-9999
            bx.y=-9999
        if s.inr(s.x-s.r,bx.x-bxw/2,bx.x+bxw/2) and s.inr(s.y,bx.y-bxh/2,bx.y+bxh/2):
            if s.n==1:#правый бок
                s.n=2
            if s.n==4:
                s.n=3
            w.delete(bx.o)
            bx.x=-9999
            bx.y=-9999
        if s.inr(s.x,bx.x-bxw/2,bx.x+bxw/2) and s.inr(s.y+s.r,bx.y-bxh/2,bx.y+bxh/2):
            if s.n==3:#верх
                s.n=2
            if s.n==4:
                s.n=1
            w.delete(bx.o)
            bx.x=-9999
            bx.y=-9999
        if s.inr(s.x,bx.x-bxw/2,bx.x+bxw/2) and s.inr(s.y-s.r,bx.y-bxh/2,bx.y+bxh/2):
            if s.n==2: #низ
                s.n=3
            if s.n==1:
                s.n=4
            w.delete(bx.o)
            bx.x=-9999
            bx.y=-9999
class box:
    def __init__(s,x,y,a,t): #создание коробки
        s.x=x
        s.y=y
        s.a=a #текущая анимация
       # s.c="#%s%s%s"%tuple(('00'+hex(randint(15,255))[2:])[-2:]for i in range(3))
        s.t=t #тип коробки
        s.o=w.create_image(x,y,image=bxm[t][a]) #создание картинки для коробки
class platform:
    def __init__(s,x,y,wi,he,p):
        s.x=x
        s.y=y
        s.wi=wi
        s.he=he
        s.p=p #скорость платформы
        s.o=w.create_rectangle(x-wi/2,y-he/2,x+wi/2,y+he/2,fill="#000000",outline="#FFEE00", width = 3)
    def move(s,x):
        s.p=spp
        if s.x>x: #х положение мышки s.x положение платформы
            m=-min(s.x-x,s.p)
            s.x+=m #перемещение платформы
            return m
        elif s.x<x:
            m=min(x-s.x,s.p)
            s.x+=m
            return m
        else:
            return 0
class bonus:
    def __init__(s,x,y,wi,he,e):
        names=['end','<_>','+_+','+.+','-.-','-_-','>_<']
        s.x=x
        s.y=y
        s.he=he
        s.wi=wi
        s.e=e #эффекты от бонуса
        s.o=w.create_rectangle(x-wi/2,y-he/2,x+wi/2,y+he/2,fill="",outline="#FFFFFF",width=3)
        s.t=w.create_text(x,y,text=names[e],font='ComicSansMS 24 bold',fill='#FFFFFF')
    def inr(s,a,b,c): #вспомогательная функция
        return(a>=b and a<=c)or(a>=c and a<=b)
    def plat(s,pl):
        global spb,spp
        if s.y+s.he/2>=pl.y-pl.he/2 and s.inr(s.x,pl.x-pl.wi/2,pl.x+pl.wi/2):
            w.delete(s.o)
            w.delete(s.t)
            s.o=0
            s.t=0
            global bonuses
            bonuses=[e for e in bonuses if e.o!=0]
            if s.e==1: #увеличение платформы на 100
                pl.wi+=100
                w.delete(pl.o)
                pl.o=w.create_rectangle(pl.x-pl.wi/2,pl.y-pl.he/2,pl.x+pl.wi/2,pl.y+pl.he/2,fill="#000000",outline="#FFEE00")
            if s.e==-1:#уменьшение платформы на 100
                pl.wi-=100
                w.delete(pl.o)
                pl.o=w.create_rectangle(pl.x-pl.wi/2,pl.y-pl.he/2,pl.x+pl.wi/2,pl.y+pl.he/2,fill="#000000",outline="#FFEE00")
            if s.e==2:#ускорение платформы на 33%
                spp/=0.75
            if s.e==-2: #замедление на 25%
                spp*=0.75
            if s.e==3: # ускорение и замедление шарика 
                spb/=0.75
            if s.e==-3:
                spb*=0.75
    def down(s,pl): #бонус падает
        w.move(s.o,0,heg/400) #объект бонуса
        w.move(s.t,0,heg/400) #рисунок бонуса
        s.y+=heg/400
        s.plat(pl) #бонус упал на платформу
        if s.y>heg: 
            w.delete(s.o)
            w.delete(s.t)
            s.o=0
            s.t=0
            global bonuses
            bonuses=[e for e in bonuses if e.o!=0] #генератор с фильтром
            
def motion(e):
    global tx,ty #положение мышки
    tx=e.x
tk=Tk() #создаем окошки
wid=tk.winfo_screenwidth()
heg=tk.winfo_screenheight()

bxm=[[PhotoImage(file='box%d.gif'%(j+1),format = 'gif -index %d'%i)for i in range([35,37,49][j])]for j in range(0,3)]#двумерный список смены кадров
                                                                            #количество кадров в гифках
#ратягивание и сужение разных гифок
for i in range(35):
    bxw=bxm[0][i].width()
    bxm[0][i]=bxm[0][i].zoom(int((wid/10)/10),int((wid/10)/10))
    bxm[0][i]=bxm[0][i].subsample(int(bxw/10),int(bxw/10))
for i in range(37):
    bxw=bxm[1][i].width()
    bxm[1][i]=bxm[1][i].zoom(int((wid/10)/10),int((wid/10)/10))
    bxm[1][i]=bxm[1][i].subsample(int(bxw/10),int(bxw/10))
for i in range(49):
    bxw=bxm[2][i].width()
    bxm[2][i]=bxm[2][i].zoom(int((wid/10)/10),int((wid/10)/10))
    bxm[2][i]=bxm[2][i].subsample(int(bxw/10),int(bxw/10))
#актуальная ширина и высота гифки
bxw=bxm[2][-1].width()
bxh=bxm[2][-1].height()

tx=wid/2
ty=0
srt=500 #пробивная способность шариков(не нужна)
spb=0.0015*wid #скорость шарика
spp=0.002*wid #скорость платформы
tk.geometry('%dx%d+0+0'%(wid,heg))#положение и размер формы
w=Canvas(tk,width=wid,height=heg) #окошко для рисования
w.pack()
w.create_rectangle(0,0,wid,heg,fill='#000000',outline="#000000")
plat=platform(0.4*wid,0.95*heg,0.25*wid,0.15*heg,0.002*wid) #ФОРМИРОВАНИЕ ПЛАТФОРМЫ
bal=ball(wid/2,heg/2,0.0015*wid,0.01*wid,'#880088')
boxes=[[box(bxw/2+j*bxw,bxh/2+bxh*i,randint(0,34),randint(0,2))for j in range(10)]for i in range(4)]
                                    #каждая гифка с разного кадра начинается
bonuses=[]
w.bind_all("<Motion>",motion)#привязываем мышку, каждый раз проверяем положение мышки
bonv=[i for i in range(-3,3+1)] #для эффектов бонусов, чтобы можно было брать случайные бонусы
bonv.remove(0)
at=time() #начальное время

@Threaded #новый поток для музыки
def music():
    PlaySound("fone.wav", SND_FILENAME)
thread = music()
thread.start()

while True:
    t=time() #текущее время

    #tk.title(str(bal.n)+' '+str(bal.y))
    w.move(plat.o,plat.move(tx),0)
    w.move(bal.o,*bal.move())
    bal.wall() #проверка врезания в стену
    bal.plat(plat) #врезался в платформу
    if time()-at>=0.05: #если прошло больше 50мс, запускаем следующий кадр
        for i in range(4):
            for j in range(10):
                a=boxes[i][j].a+1
                if boxes[i][j].t==0:
                    a=a%35
                if boxes[i][j].t==1:
                    a=a%37
                if boxes[i][j].t==2:
                    a=a%49
                boxes[i][j].a=a
                w.itemconfig(boxes[i][j].o,image=bxm[boxes[i][j].t][a])#меняем картинки всех коробочек
        at=time()#перезаписываем время
        
    for i in range(4): #проверка шарика на врезание в коробочки
        for j in range(10):
            bal.box(boxes[i][j]) 
    if randint(1,350)==1 and len(bonuses)<4: #если равно 1, то падает бонус их может быть только <=4 бонусов
        bonuses+=[bonus(randint(0,wid),0,wid*0.05,heg*0.07,bonv[randint(0,5)])]
    for b in bonuses: #передвижение бонусов
        if b.o!=0:
            b.down(plat)
    w.update() #перерисовка, обновление окошка
    while time()-t<0.013: #каждое следующее действие происходит через 13 мс
        pass

