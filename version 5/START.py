from random import*
from tkinter import*
from time import*
from winsound import* #импортируем музыку
from threaded import* #импортируем поток
import webbrowser 

tk=Tk() #создаем окошко
wid=tk.winfo_screenwidth()
heg=tk.winfo_screenheight()

r=1#rezhim

tk.geometry('%dx%d+%d+%d'%(wid/3.3,7*wid/12,(wid-wid/3.3)/2,(heg-7*wid/12)/2))



mbt=PhotoImage(file='mbt.gif')
mbw=mbt.width()
mbt=mbt.zoom(int((wid/30)/10),int((wid/30)/10))
mbt=mbt.subsample(int(mbw/100),int(mbw/100))

sbt=PhotoImage(file='sbt.gif')
sbw=sbt.width()
sbt=sbt.zoom(int((wid/30)/10),int((wid/30)/10))
sbt=sbt.subsample(int(sbw/100),int(sbw/100))

hbt=PhotoImage(file='hbt.gif')
hbw=hbt.width()
hbt=hbt.zoom(int((wid/30)/10),int((wid/30)/10))
hbt=hbt.subsample(int(hbw/100),int(hbw/100))

pbt=PhotoImage(file='pbt.gif')
pbw=pbt.width()
pbt=pbt.zoom(int((wid/30)/10),int((wid/30)/10))
pbt=pbt.subsample(int(pbw/100),int(pbw/100))

nbt=PhotoImage(file='nbt.gif')
nbw=nbt.width()
nbt=nbt.zoom(int((wid/30)/10),int((wid/30)/10))
nbt=nbt.subsample(int(nbw/100),int(nbw/100))

clb=PhotoImage(file='classic.gif')
clw=clb.width()
clb=clb.zoom(int((wid/30)/10),int((wid/30)/10))
clb=clb.subsample(int(clw/100),int(clw/100))

ewb=PhotoImage(file='easywin.gif')
eww=ewb.width()
ewb=ewb.zoom(int((wid/30)/10),int((wid/30)/10))
ewb=ewb.subsample(int(eww/100),int(eww/100))

msb=PhotoImage(file='mysterious.gif')
msw=msb.width()
msb=msb.zoom(int((wid/30)/10),int((wid/30)/10))
msb=msb.subsample(int(msw/100),int(msw/100))

imb=PhotoImage(file='impossible.gif')
imw=imb.width()
imb=imb.zoom(int((wid/30)/10),int((wid/30)/10))
imb=imb.subsample(int(imw/100),int(imw/100))

def start():
    tk.destroy()
    PlaySound(None,SND_FILENAME)
    if r==0:
        exec(open("EasyWin.py").read())
    elif r==1:
        exec(open("Classic.py").read())
    elif r==2:
        exec(open("Mysterious.py").read())
    elif r==3:
        exec(open("Impossible.py").read())

    exit()

b=Button(tk,command=start,relief=FLAT,image=mbt)
b.pack()
b.place(relx=0,rely=0,relheight=2/7,relwidth=1)

def nx():
    global m,r
    if r==0:
        m.destroy()
        m=Button(tk,relief=FLAT,command=nx,image=clb)
        m.pack()
        m.place(relx=0,rely=1/3.5,relheight=1/7,relwidth=1)
        r=1
    elif r==1:
        m.destroy()
        m=Button(tk,relief=FLAT,command=nx,image=msb)
        m.pack()
        m.place(relx=0,rely=1/3.5,relheight=1/7,relwidth=1)
        r=2
    elif r==2:
        m.destroy()
        m=Button(tk,relief=FLAT,command=nx,image=imb)
        m.pack()
        m.place(relx=0,rely=1/3.5,relheight=1/7,relwidth=1)
        r=3
    elif r==3:
        m.destroy()
        m=Button(tk,relief=FLAT,command=nx,image=ewb)
        m.pack()
        m.place(relx=0,rely=1/3.5,relheight=1/7,relwidth=1)
        r=0

m=Button(tk,relief=FLAT,command=nx,image=clb)
m.pack()
m.place(relx=0,rely=1/3.5,relheight=1/7,relwidth=1)



s=Button(tk,relief=FLAT,image=sbt)
s.pack()
s.place(relx=0,rely=3/7,relheight=2/7,relwidth=1)

h=Button(tk,text='Помощь',command=lambda:webbrowser.open("https://vk.com/akhvn"),relief=FLAT,image=hbt)
h.pack()
h.place(relx=0,rely=5/7,relheight=2/7,relwidth=1)

@Threaded #новый поток для музыки
def music():
    PlaySound("main.wav",SND_FILENAME|SND_LOOP|SND_ASYNC)
thread = music()
thread.start()

tk.mainloop()
