import tkinter as tk
from tkinter import ttk

def otvor_canvas2():
    #vytvori nove okno
    okno2 = tk.Toplevel(root)
    okno2.title("Canvas 2")

    # vytvori novy canvas v tomto okne
    canvas2 = tk.Canvas(okno2, width=400,height=300, bg="lightyellow")
    canvas2.pack(padx=10, pady=10)

    #nieco nan nakreslime
    canvas2.create_oval(50,50, 200,200, fill='orange', outline='red')
    canvas2.create_text(200,250, text='Toto je Canvas2', font='Arial 14 bold')

def otvor_scale():
    #vytvori nove okno
    okno3 = tk.Toplevel(root)
    okno3.title("Canvas Scale")

    # vytvori novy canvas v tomto okne
    canvas3 = tk.Canvas(okno3, width=440,height=400, bg="white")
    canvas3.pack(padx=10, pady=10)

    #nieco nan nakreslime
    rx, ry = 100, 100
    x, y = 200, 200

    canvas3.create_oval(x-rx, y-ry, x+rx, y+ry, width=5, outline='green', tags='oval')
    def zmena1(event):
        global rx
        rx = scale1.get()
        prekresli()

    def zmena2(event):
        global ry
        ry = scale2.get()
        prekresli()

    def prekresli():
        global ry, rx
        canvas3.coords('oval', [x-rx, y-ry, x+rx, y+ry])

    scale1 = tk.Scale(okno3, from_=10, to=200, orient='horizontal', length=400, command=zmena1, showvalue=0)
    scale1.pack()
    scale1.set(rx)

    scale2 = tk.Scale(okno3, from_=10, to=200, orient='vertical', length=400, command=zmena2)
    scale2.place(x=400, y=0)
    scale2.set(ry)
    
    label1 = tk.Label(okno3, text="Vytvori vstupny modul - posuvac, meni ciselne hodnoty")
    label1.pack()

def otvor_listbox():
    #vytvori nove okno
    okno4 = tk.Toplevel(root)
    okno4.title("Canvas Listbox")

    # vytvori novy canvas v tomto okne
    canvas4 = tk.Canvas(okno4, width=440,height=400, bg="white")
    canvas4.pack(padx=10, pady=10)

    #nieco nan nakreslime
    def prefarbi(event):
        oznacene = listbox1.curselection()
        canvas4['bg'] = listbox1.get(oznacene)

    def pridaj():
        listbox1.insert('end', entry1.get())

    def vymaz():
        oznacene = listbox1.curselection()
        if len(oznacene) == 1:
            listbox1.delete(oznacene)

    listbox1 = tk.Listbox(okno4)
    listbox1.pack()

    farby = ['red', 'green', 'blue', 'orange', 'yellow', 'white']

    for prvok in farby:
        listbox1.insert('end', prvok)

    listbox1.bind('<Double-Button-1>', prefarbi)

    label1 = tk.Label(okno4, text='Napíš názov farby:')
    label1.pack()
    entry1 = tk.Entry(okno4)
    entry1.pack()
    button1 = tk.Button(okno4, text='Pridaj farbu', command=pridaj)
    button1.pack()
    button2 = tk.Button(okno4, text='Vymaž označenú farbu', command=vymaz)
    button2.pack()
    
    label2 = tk.Label(okno4, text="Ukáže v ponuke viaceré možnosti a my môžeme (štandardne) z nich jednu označiť")
    label2.pack()

def otvor_text():
    #vytvori nove okno
    okno5 = tk.Toplevel(root)
    okno5.title("Canvas Text")

    # vytvori novy canvas v tomto okne
    canvas5 = tk.Canvas(okno5, width=200,height=20, bg="grey")
    canvas5.pack(padx=10, pady=10)

    #nieco nan nakreslime
    text1 = tk.Text(okno5, height=2, width=30)
    text1.pack(side='left')

    scrollbar1 = tk.Scrollbar(okno5)
    scrollbar1.pack(side='right', fill='y')
    #vyplní s ním celý voľný priestor v rozsahu osi y
    scrollbar1.config(command=text1.yview)
    #po posunutí sa posunie aj obsah text1
    text1.config(yscrollcommand=scrollbar1.set)
    #po posunutí obsahu text1 sa posunie aj scrollbar1
    prih = ['John', 'Ioan', 'Johan', 'Juan', 'Jovanni', 'Ivan']

    for meno in prih:
        text1.insert('end', meno + '\n')
    
    label1 = tk.Label(okno5, text="Vytvori textove pole a prida moznost ho scrolovat")
    label1.pack()

def otvor_radiobutton():
    #vytvori nove okno
    okno6 = tk.Toplevel(root)
    okno6.title("Canvas Radiobutton")

    # vytvori novy canvas v tomto okne
    canvas6 = tk.Canvas(okno6, width=400,height=400, bg="grey")
    canvas6.pack(padx=10, pady=10)

    #nieco nan nakreslime
    v = tk.IntVar()

    radiobutton1 = tk.Radiobutton(okno6, text='kruh', variable=v, value=1)
    radiobutton1.pack()
    radiobutton2 = tk.Radiobutton(okno6, text='štvorec', variable=v, value=2)
    radiobutton2.pack()
    radiobutton3 = tk.Radiobutton(okno6, text='čiara', variable=v, value=3)
    radiobutton3.pack()
    radiobutton4 = tk.Radiobutton(okno6, text='text', variable=v, value=4)
    radiobutton4.pack()

    def klik(sur):
        typ = v.get()
        if typ == 1:
            canvas6.create_oval(sur.x-10, sur.y-10, sur.x+10, sur.y+10, outline='white')
        if typ == 2:
            canvas6.create_rectangle(sur.x-10, sur.y-10, sur.x+10, sur.y+10, outline='white')
        if typ == 3:
            canvas6.create_line(sur.x-10, sur.y, sur.x+10, sur.y, fill='white')
        if typ == 4:
            canvas6.create_text(sur.x, sur.y, text='['+str(sur.x)+','+str(sur.y)+']', fill='white')
    canvas6.bind('<Button-1>', klik)
    
    label1 = tk.Label(okno6, text="Vytvori skupinu moznosti, z ktorych je mozne vybrat len jednu")
    label1.pack()

def otvor_checkbox():
    #vytvori nove okno
    okno7 = tk.Toplevel(root)
    okno7.title("Canvas Checkbox")

    # vytvori novy canvas v tomto okne
    canvas7 = tk.Canvas(okno7, width=400,height=40, bg="grey")
    canvas7.pack(padx=10, pady=10)

    #nieco nan nakreslime
    def vypis():
        predmety = predmet1.get() + ' ' + predmet2.get() + ' ' + predmet3.get()
        predmety = predmety.strip()
        canvas7.delete('all')
        canvas7.create_text(200,20, text=predmety, font='Arial 30 bold')

    label1 = tk.Label(okno7, text='Z ktorého predmetu idete maturovať?')
    label1.pack()

    predmet1 = tk.StringVar(okno7)
    checkbutton1 = tk.Checkbutton(okno7, text='slovenský jazyk a literatúra', onvalue='SJL', offvalue='', variable=predmet1, command=vypis)
    checkbutton1.pack(anchor='w')
    predmet2 = tk.StringVar(okno7)
    checkbutton2 = tk.Checkbutton(okno7, text='anglický jazyk', onvalue='AJ', offvalue='', variable=predmet2, command=vypis)
    checkbutton2.pack(anchor='w')
    predmet3 = tk.StringVar(okno7)
    checkbutton3 = tk.Checkbutton(okno7, text='nemecký jazyk', onvalue='NJ', offvalue='', variable=predmet3, command=vypis)
    checkbutton3.pack(anchor='w')
    
    label2 = tk.Label(okno7, text="Vytvori skupinu moznosti, z ktorych je mozne vybrat nekolko")
    label2.pack()

def otvor_spinbox():
    #vytvori nove okno
    okno8 = tk.Toplevel(root)
    okno8.title("Canvas Spinbox")

    # vytvori novy canvas v tomto okne
    canvas8 = tk.Canvas(okno8, width=400,height=400, bg="white")
    canvas8.pack(padx=10, pady=10)

    #nieco nan nakreslime
    def on_spinbox_change():
        global value
        value = spinbox.get()
    
    def cislo(sur):
        global value
        x = sur.x
        y = sur.y
        canvas8.create_text(x,y, text=str(value), font='Arial 15')

    # Creating a Spinbox
    spinbox = tk.Spinbox(okno8, from_=0, to=100, width=10, relief="sunken", repeatdelay=500, repeatinterval=100, font=("Arial", 12), bg="lightgrey", fg="blue", command=on_spinbox_change)
    # Setting options for the Spinbox
    spinbox.config(state="normal", cursor="hand2", bd=3, justify="center", wrap=True)
    # Placing the Spinbox in the window
    spinbox.pack(padx=20, pady=20)

    canvas8.bind('<Button-1>', cislo)
    
    label2 = tk.Label(okno8, text="Vytvori vstup pre cislo, je mozne vybrat z urceneho rozsahu")
    label2.pack()

def otvor_commbox():
    #vytvori nove okno
    okno9 = tk.Toplevel(root)
    okno9.title("Canvas Commbox")

    # vytvori novy canvas v tomto okne
    canvas9 = tk.Canvas(okno9, width=500,height=250, bg="grey")
    canvas9.pack(padx=10, pady=10)

    #nieco nan nakreslime
    ttk.Label(okno9, text = "GFG Combobox Widget", 
            background = 'green', foreground ="white", 
            font = ("Times New Roman", 15))

    # label
    ttk.Label(okno9, text = "Select the Month :",
            font = ("Times New Roman", 10))

    # Combobox creation
    n = tk.StringVar(okno9)
    monthchoosen = ttk.Combobox(okno9, width = 27, textvariable = n)

    # Adding combobox drop down list
    monthchoosen['values'] = (' January', ' February', ' March', ' April', ' May', ' June', ' July', ' August', ' September', ' October', ' November', ' December')

    monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()

#hlavne okno
root = tk.Tk()
root.title("Hlavne okno")

#vytvorime menu
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

#pridame menu polozku "Zobrazit"
zobrazit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Dizajn", menu=zobrazit_menu)

#polozka, ktora otvori nove okno s Canvasom
zobrazit_menu.add_command(label="Canvas2", command=otvor_canvas2)
zobrazit_menu.add_command(label="Canvas Scale", command=otvor_scale)
zobrazit_menu.add_command(label="Canvas Listbox", command=otvor_listbox)
zobrazit_menu.add_command(label="Canvas Text", command=otvor_text)
zobrazit_menu.add_command(label="Canvas Radiobutton", command=otvor_radiobutton)
zobrazit_menu.add_command(label="Canvas Checkbox", command=otvor_checkbox)
zobrazit_menu.add_command(label="Canvas Spinbox", command=otvor_spinbox)
zobrazit_menu.add_command(label="Canvas Commbox", command=otvor_commbox)

#hlavny canvas v hlavnom okne
canvas1 = tk.Canvas(root, width=400, height=300, bg='white')
canvas1.pack(padx=10,pady=10)
canvas1.create_rectangle(50,50, 200,200, fill='lightblue',outline="blue")
canvas1.create_text(200,250, text="Toto to je Canvas1", font="Arial 14 bold")

canvas1.mainloop()

""" import tkinter
canvas = tkinter.Canvas(width=400, height=100, bg='white')
canvas.pack()

def oznam():
    vysledok = tkinter.messagebox.showinfo('oznam', 'stlačili ste tlačidlo')
    print(vysledok)

def otazka1():
    vysledok = tkinter.messagebox.askyesno('Pokračovanie', 'Chcete pokračovať?')
    print(vysledok)

def otazka2():
    vysledok = tkinter.messagebox.askyesnocancel('Pokračovanie', 'Chcete pokračovať?')
    print(vysledok)

button1 = tkinter.Button(text='zobraz oznam', command=oznam)
button1.pack()
button2 = tkinter.Button(text='otazka 1', command=otazka1)
button2.pack()
button3 = tkinter.Button(text='otazka 2', command=otazka2)
button3.pack()

canvas.mainloop() """

""" import tkinter, random

okno = tkinter.Tk()
okno.geometry('500x400')
okno.title('Používanie menu')

canvas = tkinter.Canvas(width=400, height=400, bg='white')
canvas.pack()

def otvor():
    pass
def uloz():
    pass
def oprograme():
    text1.place(x=100, y=100)
    button1.place(x=300, y=200)
def oprograme_zatvor():
    text1.place_forget()
    button1.place_forget()

menu1 = tkinter.Menu(okno)
okno.config(menu=menu1)
menu2 = tkinter.Menu(menu1)
menu2.add_command(label='Otvoriť', command=otvor)
menu2.add_command(label='Uložiť', command=uloz)
menu2.add_separator()
menu2.add_command(label='Skončiť', command=okno.destroy) # alebo quit
menu1.add_cascade(label='Súbor', menu=menu2)
menu3 = tkinter.Menu(menu2)
menu3.add_command(label='O programe', command=oprograme)
menu1.add_cascade(label='Pomocník', menu=menu3)
text1 = tkinter.Text(height=5, width=42)
text1.insert('end', 'O programe\ntoto je program na ukážku používania menu\nverzia 1.0')
text1.config(state='disabled')
button1 = tkinter.Button(text='Zatvor', command=oprograme_zatvor)

canvas.mainloop() """

""" import tkinter, random
okno = tkinter.Tk()
canvas = tkinter.Canvas(width=400, height=400, bg='white')
canvas.pack()

def kruh():
    x, y = random.randrange(400), random.randrange(400)
    r = random.randint(10,50)
    canvas.create_oval(x-r, y-r, x+r, y+r)
def stvorec():
    x, y = random.randrange(400), random.randrange(400)
    r = random.randint(10, 50)
    canvas.create_rectangle(x-r, y-r, x+r, y+r)

menu1 = tkinter.Menu(okno)

okno.config(menu=menu1)
menu1.add_command(label='kresli kruh', command=kruh)
menu1.add_command(label='kresli štvorec', command=stvorec)

canvas.mainloop() """

""" import tkinter, random
okno = tkinter.Tk()
canvas = tkinter.Canvas(width=400, height=400, bg='white')
canvas.pack()

def kruh():
    x, y = random.randrange(400), random.randrange(400)
    r = random.randint(10,50)
    canvas.create_oval(x-r, y-r, x+r, y+r)
def stvorec():
    x, y = random.randrange(400), random.randrange(400)
    r = random.randint(10, 50)
    canvas.create_rectangle(x-r, y-r, x+r, y+r)

menu1 = tkinter.Menu(okno)

okno.config(menu=menu1)
menu1.add_command(label='kresli kruh', command=kruh)
menu1.add_command(label='kresli štvorec', command=stvorec)

rx, ry = 100, 50
x, y = 200, 200

canvas.create_oval(x-rx, y-ry, x+rx, y+ry, width=5, outline='green', tags='oval')
canvas.create_rectangle(x-rx, y-ry, x+rx, y+ry, width=5, outline='green', tags='rectangle')
def zmena1(event):
    global rx
    rx = scale1.get()
    prekresli()

def zmena2(event):
    global ry
    ry = scale2.get()
    prekresli()

def prekresli():
    typ = v.get()
    if typ == 1:
        canvas.coords('oval',[x-rx, y-ry, x+rx, y+ry])
    elif typ == 2:
        canvas.coords('rectangle',[x-rx, y-ry, x+rx, y+ry])


def insert():
    listbox1.insert('end', entry1.get())
    text1.insert('end', entry1.get()+'\n')
        
    predmety = predmet1.get() + ' ' + predmet2.get()
    predmety = predmety.strip()
    print('Práve máte vybraté predmety:', predmety)

scale1 = tkinter.Scale(from_=10, to=180, orient='vertical', length=400, command=zmena1)
scale2 = tkinter.Scale(from_=10, to=180, orient='horizontal', length=400, command=zmena2)

scale2.pack()
scale1.pack(side='right')
scale1.set(ry)
scale2.set(rx)

text1 = tkinter.Text(height=5, width=30)
text1.pack()

label1 = tkinter.Label(text='toto je label',)
label1.pack()

entry1 = tkinter.Entry()
entry1.pack()

button1 = tkinter.Button(text='insert', command=insert)
button1.pack()

listbox1 = tkinter.Listbox()
listbox1.pack()

listbox1.insert('end', 'aaaa')
listbox1.curselection()

v = tkinter.IntVar()

radiobutton1 = tkinter.Radiobutton(text='oval', variable=v, value=1)
radiobutton1.pack()
radiobutton2 = tkinter.Radiobutton(text='rectangle', variable=v, value=2)
radiobutton2.pack()

predmet1 = tkinter.StringVar()
checkbutton1 = tkinter.Checkbutton(text='slovenský jazyk a literatúra', onvalue='SJL', offvalue='', variable=predmet1, command=insert)
checkbutton1.pack(anchor='w')
predmet2 = tkinter.StringVar()
checkbutton2 = tkinter.Checkbutton(text='anglický jazyk', onvalue='AJ', offvalue='', variable=predmet2, command=insert)
checkbutton2.pack(anchor='w')

canvas.mainloop() """

""" import tkinter

def vypis():
    predmety = ''
    for prvok in informacie:
        predmety = predmety + ' ' + prvok.get()
        predmety = predmety.strip()
    print('Práve máte vybraté predmety:', predmety)

def reset():
    for informacia in informacie:
        informacia.set('')
        vypis()

subor = open('predmety.txt', 'r')
informacie = []

label1 = tkinter.Label(text='Z ktorého predmetu idete maturovať?')
label1.pack()

for riadok in subor:
    riadok = riadok.strip()
    info = riadok.split(';')
    informacie.append(tkinter.StringVar())
    chb = tkinter.Checkbutton(text=info[0], onvalue=info[1], offvalue='', variable=informacie[-1], command=vypis)
    chb.pack(anchor='w')

subor.close()
button1 = tkinter.Button(text='reset', command=reset)
button1.pack()

label1.mainloop() """

""" import tkinter

def vypis():
    predmety = predmet1.get() + ' ' + predmet2.get() + ' ' + predmet3.get()
    predmety = predmety.strip()
    print('Práve máte vybraté predmety:', predmety)

label1 = tkinter.Label(text='Z ktorého predmetu idete maturovať?')
label1.pack()

predmet1 = tkinter.StringVar()
checkbutton1 = tkinter.Checkbutton(text='slovenský jazyk a literatúra', onvalue='SJL', offvalue='', variable=predmet1, command=vypis)
checkbutton1.pack(anchor='w')
predmet2 = tkinter.StringVar()
checkbutton2 = tkinter.Checkbutton(text='anglický jazyk', onvalue='AJ', offvalue='', variable=predmet2, command=vypis)
checkbutton2.pack(anchor='w')
predmet3 = tkinter.StringVar()
checkbutton3 = tkinter.Checkbutton(text='nemecký jazyk', onvalue='NJ', offvalue='', variable=predmet3, command=vypis)
checkbutton3.pack(anchor='w')

label1.mainloop() """

""" import tkinter
okno = tkinter.Tk()
v = tkinter.StringVar()

mesta = [('Banská Bystrica','BB'), ('Bratislava','BA'), ('Košice','KE'),
('Nitra','NR'), ('Prešov','PO'), ('Trenčín','TN'), ('Trnava','TT'),
('Žilina','ZA')]

def vypis():
    print(v.get())

for mesto, skratka in mesta:
    rb = tkinter.Radiobutton(okno, text=mesto, value=skratka, variable=v, command=vypis)
    rb.pack(anchor='w')

okno.mainloop() """

""" import tkinter
okno = tkinter.Tk()
v = tkinter.IntVar()
def vypis():
    print(v.get())

radiobutton1 = tkinter.Radiobutton(okno, text='kruh', variable=v, value=1, command=vypis)
radiobutton1.pack()
radiobutton2 = tkinter.Radiobutton(okno, text='štvorec', variable=v, value=2, command=vypis)
radiobutton2.pack()
radiobutton3 = tkinter.Radiobutton(okno, text='čiara', variable=v, value=3, command=vypis)
radiobutton3.pack()
radiobutton4 = tkinter.Radiobutton(okno, text='text', variable=v, value=4, command=vypis)
radiobutton4.pack()

okno.mainloop() """

""" import tkinter
canvas = tkinter.Canvas(width=200, height=200, bg='white')
canvas.pack()

v = tkinter.IntVar()

radiobutton1 = tkinter.Radiobutton(text='kruh', variable=v, value=1)
radiobutton1.pack()
radiobutton2 = tkinter.Radiobutton(text='štvorec', variable=v, value=2)
radiobutton2.pack()
radiobutton3 = tkinter.Radiobutton(text='čiara', variable=v, value=3)
radiobutton3.pack()
radiobutton4 = tkinter.Radiobutton(text='text', variable=v, value=4)
radiobutton4.pack()

def klik(sur):
    typ = v.get()
    if typ == 1:
        canvas.create_oval(sur.x-10, sur.y-10, sur.x+10, sur.y+10)
    if typ == 2:
        canvas.create_rectangle(sur.x-10, sur.y-10, sur.x+10, sur.y+10)
    if typ == 3:
        canvas.create_line(sur.x-10, sur.y, sur.x+10, sur.y)
    if typ == 4:
        canvas.create_text(sur.x, sur.y, text='['+str(sur.x)+','+str(sur.y)+']')
canvas.bind('<Button-1>', klik)

canvas.mainloop() """

""" import tkinter
text1 = tkinter.Text(height=5, width=30)
text1.pack(side='left')

scrollbar1 = tkinter.Scrollbar()
scrollbar1.pack(side='right', fill='y')
#vyplní s ním celý voľný priestor v rozsahu osi y
scrollbar1.config(command=text1.yview)
#po posunutí sa posunie aj obsah text1
text1.config(yscrollcommand=scrollbar1.set)
#po posunutí obsahu text1 sa posunie aj scrollbar1
f = open('score.txt', 'r')
for riadok in f:
    text1.insert('end', riadok)
f.close()

text1.mainloop() """

""" import tkinter
canvas = tkinter.Canvas(width=200, height=200, bg='white')
canvas.pack()

text1 = tkinter.Text(height=20, width=30)
text1.pack()

prih = open('prihlaseni.txt', 'r')

meno = prih.readline()
while meno != '':
    text1.insert('end', meno)
    prih.readline()
    meno = prih.readline()

canvas.mainloop() """

""" import tkinter
canvas = tkinter.Canvas(width=440, height=200, bg='white')
canvas.pack()

rx, ry = 100, 50
x, y = 200, 100

canvas.create_oval(x-rx, y-ry, x+rx, y+ry, width=5, outline='green', tags='oval')
def zmena1(event):
    global rx
    rx = scale1.get()
    prekresli()

def zmena2(event):
    global ry
    ry = scale2.get()
    prekresli()

def prekresli():
    canvas.coords('oval',[x-rx, y-ry, x+rx, y+ry])

scale1 = tkinter.Scale(from_=10, to=200, orient='horizontal', length=400, command=zmena1, showvalue=0)
scale1.pack()
scale1.set(rx)

scale2 = tkinter.Scale(from_=10, to=100, orient='vertical', length=200, command=zmena2)
scale2.place(x=400, y=0)
scale2.set(ry)

canvas.mainloop() """

""" import tkinter
canvas = tkinter.Canvas(width=400, height=200, bg='white')
canvas.pack()

def prefarbi(event):
    oznacene = listbox1.curselection()
    canvas['bg'] = listbox1.get(oznacene)

def pridaj():
    listbox1.insert('end', entry1.get())

def vymaz():
    oznacene = listbox1.curselection()
    if len(oznacene) == 1:
        listbox1.delete(oznacene)

listbox1 = tkinter.Listbox()
listbox1.pack()

farby = ['red', 'green', 'blue', 'orange', 'yellow', 'white']

for prvok in farby:
    listbox1.insert('end', prvok)

listbox1.bind('<Double-Button-1>', prefarbi)

label1 = tkinter.Label(text='Napíš názov farby:')
label1.pack()
entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='Pridaj farbu', command=pridaj)
button1.pack()
button2 = tkinter.Button(text='Vymaž označenú farbu', command=vymaz)
button2.pack()

canvas.mainloop() """

""" import tkinter
canvas = tkinter.Canvas(width=400, height=200, bg='white')
canvas.pack()

frame1 = tkinter.Frame()
frame1.pack(side='left')
button1 = tkinter.Button(frame1, text='tlačidlo 1', width=20)
button1.pack()
button2 = tkinter.Button(frame1, text='tlačidlo 2', width=20)
button2.pack()

frame2 = tkinter.Frame()
frame2.place(x=300, y=10)
button3 = tkinter.Button(frame2, text='3', width=10, bg='green')
button3.pack()
button4 = tkinter.Button(frame2, text='4', width=10, fg='red')
button4.pack()

canvas.mainloop() """

""" import tkinter
canvas = tkinter.Canvas(width=400, height=200, bg='white')
canvas.pack()

frame1 = tkinter.Frame()
frame1.pack(side='left')
button1 = tkinter.Button(frame1, text='tlačidlo 1', width=20)
button1.pack()
button2 = tkinter.Button(frame1, text='tlačidlo 2', width=20)
button2.pack()

frame2 = tkinter.Frame()
frame2.pack(side='left')
button3 = tkinter.Button(frame2, text='3', width=10, bg='green')
button3.pack()
button4 = tkinter.Button(frame2, text='4', width=10, fg='red')
button4.pack()

canvas.mainloop() """

""" import tkinter, random

def nakresli():
    x = random.randrange(400)
    y = random.randrange(200)
    canvas1.create_text(x, y, text=entry1.get())
    canvas2.create_text(x, y, text=entry1.get()[::-1])

canvas1 = tkinter.Canvas(width=400, height=200, bg='yellow')
canvas2 = tkinter.Canvas(width=400, height=200, bg='green')
label1 = tkinter.Label(text='Napíš meno:')
entry1 = tkinter.Entry()
button1 = tkinter.Button(text='nakresli', command=nakresli)

canvas1.pack(side='left')
canvas2.pack(side='right')
label1.pack()
entry1.pack(side='bottom')
button1.pack(side='bottom')

canvas1.mainloop()
canvas2.mainloop() """