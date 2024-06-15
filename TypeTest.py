import mysql.connector as mc
from tkinter import *
from tkinter import ttk
import timeit
import random

pwd = "*"
color = "#F5F5F5"
front_window = Tk()
front_window.geometry("1000x800")
front_window.title("Typing Test")
front_window.configure(bg=color)
front_window.resizable(False,False)

conc1 = mc.connect(host="localhost", user="root", password=pwd, database="typetest")
cur1 = conc1.cursor()
cur1.execute("Select * from tt;")
l = cur1.fetchall()

def dest():
    global Name
    Name = n1.get()
    front_window.destroy()

def entry_table(parent_window):
    global l
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading",background="#FFD700",font=("Arial", 12, "bold"))
    style.map("Treeview.Heading", background=[("active", "lightblue")])
    table = ttk.Treeview(parent_window,style="my.Treeview")
    table.tag_configure("myfont", font=("Arial", 12, "normal"))

    table['columns']=['Sr No','Name','WPM','Accuracy']
    table.column("#0",anchor=CENTER,width=0)
    table.column("Sr No", anchor=CENTER, width=200)
    table.column("Name", anchor=CENTER, width=400)
    table.column("WPM", anchor=CENTER, width=200)
    table.column("Accuracy", anchor=CENTER, width=200)

    for column in table['columns']:
        table.heading(column, text=column, anchor=CENTER)
    for i in range(len(l)):
        table.insert(parent="", index="end", iid=i+1, text="",tags=("myfont"), values=l[i])
    table.place(relx=0.0, rely=0.7)
    table["height"] = len(l) + 1

ent1 = Label(front_window, font=("Georgia",30,"bold"),background=color, text="Welcome To The Ultimate Typing Test").place(relx=0.1, rely=0.1)
ent2 = Label(front_window, font=("Times New Roman",20,"bold"),background=color, text="Instructions:").place(relx=0.3, rely=0.2)
ent2 = Label(front_window, font=("arial",15),background=color, text="1. This is a 60 seconds typing test").place(relx=0.3, rely=0.25)
ent4 = Label(front_window, font=("arial",15),background=color, text="2. Please Enter Your Name").place(relx=0.3, rely=0.3)
ent5 = Label(front_window, font=("arial",15),background=color, text="3. Timer will start once you start typing").place(relx=0.3, rely=0.35)
ent6 = Label(front_window, font=("arial",20,"bold"),background="white", text="Enter Name").place(relx=0.3, rely=0.5)
n1 = Entry(front_window, font=("arial",20,"bold"), width=20)
n1.place(relx=0.5, rely=0.5)
btn = Button(front_window, font=("arial",20,"bold"), text="Submit", command=dest).place(relx=0.45, rely=0.6)
entry_table(front_window)

front_window.mainloop()

window = Tk()
window.geometry("1200x800")
window.title("Typing Test")
window.configure(bg=color)
window.resizable(False,False)

conc2 = mc.connect(host="localhost", user="root", password=pwd, database="typetest")
cur2 = conc2.cursor()

words = ['At first the professor scowled with concern. But then he said, thats all right. Run to my house. Tell my wife to give you one of my shirts. "Mrs. Esputa quickly fetched one of her husbands white shirts. But when Philip put it on, she began to exclaim, "Oh, dear! Gracious!" The shirt was so large that Philip was almost lost in it. Hastily Mrs. Esputa found a box of pins. In a twinkling, her nimble fingers pinned enough tucks in the shirt to make it fit Philip. They both heaved a big sigh of relief when the job was finished. Then, free from anxiety, Philip hurried back to the school. The concert finally began, and soon it was time for Philips also. Stood up, placed the violin under his chin, and raised his bow.',
         'Now we have devised robots that are much more complicated than any other machines we have ever had. They are complicated enough to do jobs that until now only human beings could do, but that are too simple for the marvellous brains we all have. The robots, even though they are smarter than other machines, are still only capable of very simple tasks - the kind of tasks human beings ought not to waste their time doing. In that case, why not let the robots do it? Why shouldnt human beings do other and better things? After all, whenever there is an important new invention, some jobs are lost. When the automobile came into use, there was a gradual, but steady, loss of jobs that involved horses.',
         'Sher Singh breathed one more prayer, of thanks this time, and scrambled down into the river-bed. He stepped into the river, usual, and deeper than it had been. Sher Singh had to go slowly made ready to move with Kunwar on his back once again. Han Sher Singh had been to this river often. But it was colder than because of slime on the stones. Thank goodness there was a bridge at the second river, he thought. It was a flimsy thing made of bamboo poles, stones, thick grass and river gravel. But it was at least a bridge. As Sher Singh washed up on to the shore, water twinkled in his footprints before sinking into the sand. Coming up out of the river were another set of prints-a tigers and there was glitter in them too.',
         'Switzerland is the most peaceful country in the world. Although always prepared to face any hazard of war, it has never faced any hostile army since the Swiss Confederation was founded in 1815, nor has its army ever fired at anyone in aggression. Switzerland is, therefore, totally free of the ravages of war. No other European country can claim this distinction. Most of Switzerlands 16,000 square mile area is a continuous, rolling lush countryside of pastures, Vineyards and grain farms, except one third of the mountainous and extremely beautiful region. Three quarters of the population lives in small towns and villages which remain exquisitely medieval in their architecture and external appearance.'
         ]

sentence = random.choice(words)
l1 = Label(window, font=("georgia", 20), text=sentence, wraplength="1200", bg=color)
l1.place(x=0, y=0)
l1.grid(row=0, column=0,sticky=W)

l2 = Text(window, font=("arial", 15, "bold"), height=10, width=100, bg="#FFD700", bd=0.5)
l2.place(x=2, y=300)
l2.grid(row=1, column=0, pady=20,sticky=W,padx= 40)

l3 = Label(window, font=("arial", 20), text="Words Per Minute: 0")
l3.place(x=50, y=600)
l3.grid(row=2, column=0, sticky=W, padx=150, pady=20)

l4 = Label(window, font=("arial", 20 ), text="Time: 0s")
l4.place(x=50, y=600)
l4.grid(row=2, column=0, pady=20,sticky=W,padx=900)

l5 = Label(window, font=("arial", 20 ), text="Accuracy: 00.00%")
l5.place(x=50, y=600)
l5.grid(row=2, column=0, pady=20, sticky=W, padx=520)

start_time = 0 
writing_time = 0  
disable_text = False  
mistakes = 0
wpm = 0
acc = 100

def get_start_time(event):
    global start_time, writing_time, disable_text
    if start_time == 0:
        start_time = timeit.default_timer()

    writing_time = round(timeit.default_timer() - start_time)
    l4.config(text="Time: {}s".format(writing_time))

    if writing_time >= 60:
        l4.config(text="Time: 60s",font=("arial",20,"bold"))
        disable_text = True
        l2.config(state=DISABLED)
        l6 = Label(window,text="TIME IS UP!!!",font=("arial",50,"bold"),background="#FFD700")
        l6.place(relx=0.35,rely=0.5)
    else:
        l2.config(state=NORMAL)

l2.bind("<Key>", get_start_time)

def check_time():
    global writing_time
    writing_time = round(timeit.default_timer() - start_time)
    w_p_m = round(len(l2.get("1.0", "end-1c").split()) / max(1, writing_time) * 60,2)
    l3.config(text="Words Per Minute : {}".format(w_p_m), font=("arial",20))

    if writing_time >= 60:
        l2.config(state=DISABLED)
        w_p_m = len(l2.get("1.0", "end-1c").split())
        l3.config(text="Words Per Minute : {}".format(w_p_m),font=("arial",20,"bold"))
        global wpm
        wpm = w_p_m
    else:
        l3.config(text="Words Per Minute : {}".format(w_p_m),font=("arial",20))

    window.after(1000, check_time)

check_time()

def check_typing():
    global mistakes, writing_time
    user_text = l2.get("1.0", "end-1c")
    i = 0
    for i, char in enumerate(user_text):
        if char == sentence[i]:
            l2.config(foreground="black")
        else:
            mistakes += 1
            l2.delete("end-2c")
            l2.config(foreground="red")
    if len(user_text) > 1 and len(user_text) > mistakes and writing_time <= 60 and writing_time >= 1:
        accuracy = (len(user_text) - mistakes) / len(user_text) * 100
        l5.config(text="Accuracy:{}%".format(round(accuracy, 2)))
    elif len(user_text) < mistakes:
        l5.config(text="Accuracy:0%")
    elif writing_time >= 60 and len(user_text) > 1 and len(user_text) > mistakes:
        accuracy = (len(user_text) - mistakes) / len(user_text) * 100 
        l5.config(text="Accuracy:{}%".format(round(accuracy, 1)),font=("arial",20,"bold"))
        global acc
        acc = round(accuracy,2)

    window.after(200, check_typing)

check_typing()

def save_results():
    sql_query = "INSERT INTO tt (Name, WPM, Accuracy) VALUES (%s, %s, %s)"
    values = (Name, wpm, acc)
    cur2.execute(sql_query, values)
    conc2.commit()
    conc2.close()
    window.destroy()


save_button = Button(window, font=("arial", 20, "bold"), text="Save Results", command=save_results)
save_button.place(x=500, y=650)
window.mainloop()