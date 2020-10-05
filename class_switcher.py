from tkinter import *
from tkinter import ttk
import webbrowser
from datetime import datetime
import re
import time
from threading import Thread
import pickle
import os.path
from os import path
from tkinter import messagebox

def killer():
    if messagebox.askyesno("Exit", "Do you want to quit the application?"):
        root.quit()

def saver():
    with open ('adayurls.txt', 'wb') as fp:
        pickle.dump(adayurllist, fp)
    with open ('adaytimes.txt', 'wb') as fp:
        pickle.dump(adaytimelist, fp)
    with open ('bdayurls.txt', 'wb') as fp:
        pickle.dump(bdayurllist, fp)
    with open ('bdaytimes.txt', 'wb') as fp:
        pickle.dump(bdaytimelist, fp)

def loader():
    global adayurllist, adaytimelist, bdayurllist, bdaytimelist
    with open ('adayurls.txt', 'rb') as fp:
        adayurllist = pickle.load(fp)
    with open ('adaytimes.txt', 'rb') as fp:
        adaytimelist = pickle.load(fp)
    with open ('bdayurls.txt', 'rb') as fp:
        bdayurllist = pickle.load(fp)
    with open ('bdaytimes.txt', 'rb') as fp:
        bdaytimelist = pickle.load(fp)
    print (adayurllist, adaytimelist, bdayurllist, bdaytimelist)

def blockcount():
    global tkwidth, tkheight, xcord, ycord, classesentry, root
    root = Tk()
    root.withdraw()

    tkwidth = 590
    tkheight = 225
    screen_width = (root).winfo_screenwidth()
    screen_height = (root).winfo_screenheight()
    xcord = (screen_width/2) - (tkwidth/2)
    ycord = (screen_height/2) - (tkheight/2)

    numblocks()

def blockclick():
    global blocks2
    blocks = classesentry.get()
    try:
        blocks2 = int(blocks)
        sop.destroy()
        urltimewindow()
        abnotice()
    except:
        sop.destroy()
        numblocks()
        incorrectblock()

def abnotice():
    rop = Toplevel()
    rop.attributes("-topmost", True)
    rop.title("bruh")
    rop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    Label(rop, text="Please put an A- or B- in front of your block time AND URL \n so I can tell what goes where (For example, A-16:03 & B-https://www). Thanks <3").pack(expand = YES)
    closebutton = Button(rop, text="Close", command=rop.destroy).pack(expand = YES)

def incorrectab():
    mop = Toplevel()
    mop.attributes("-topmost", True)
    mop.title("bruh")
    mop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    Label(mop, text="Please make sure your fields are correct and you're \n putting an A or B before your URLs and times. Thank you").pack(expand = YES)
    closebutton = Button(mop, text="Close", command=mop.destroy).pack(expand = YES)

def incorrectblock():
    pop = Toplevel()
    pop.attributes("-topmost", True)
    pop.title("bruh")
    pop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    Label(pop, text="Please make sure you're putting in a correct number of blocks. Thank you").pack(expand = YES)
    closebutton = Button(pop, text="Close", command=pop.destroy).pack(expand = YES)

def numblocks():
    global classesentry, sop
    sop = Toplevel()
    sop.title("bruh")
    sop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    sop.protocol("WM_DELETE_WINDOW", killer)
    
    classes = Label(sop, text="How many blocks do you have? If you want to include Advisory just add 1 \n (please use numbers): ")
    classesbutton = Button(sop, text="Submit", command=blockclick)
    classesentry = Entry(sop)

    classes.pack(expand=YES)
    classesentry.pack(expand=YES)
    classesbutton.pack(expand=YES)

def urltimewindow():
    global top, count, urls, times
    top = Toplevel()
    top.title("Hello")
    top.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    top.protocol("WM_DELETE_WINDOW", killer)
    count = 0
    urls = []
    times = []

    for i in range(1, blocks2+1):
        count += 1
        Label(top, text="Block %d Google URL" % i).grid(row = 0 + count, column=5)
        myurls = Entry(top)
        myurls.grid(row = 0 + count, column=45)
        urls.append(myurls)
        Label(top, text="Block %d Time (HH:MM ex. 16:03)" % i).grid(row = 0 + count, column = 65)
        mytimes = Entry(top)
        mytimes.grid(row = 0 + count, column=80)
        times.append(mytimes)

    submitbutton = Button(top, text="Submit", command=urltimeclick).grid(row = 10, column=60)

def urltimeclick():
    global adayurllist, bdayurllist, adaytimelist, bdaytimelist
    urls_list = ""
    times_list = ""
    
    for i in urls:
        urls_list = urls_list + str(i.get())

    for i in times:
        times_list = times_list + str(i.get())

    try:
        adayurl = urls_list[:urls_list.index("B-")]
        bdayurl = urls_list[urls_list.index("B-"):]
        adaytime = times_list[:times_list.index("B-")]
        bdaytime = times_list[times_list.index("B-"):]
        adayurllist = [i for i in re.split("A-", adayurl) if i != '']
        bdayurllist = [i for i in re.split("B-", bdayurl) if i != '']
        adaytimelist = [i for i in re.split("A-", adaytime) if i != '']
        bdaytimelist = [i for i in re.split("B-", bdaytime) if i != '']
        saver()
        top.destroy()
        adayorbdaywindows()
    except:
        top.destroy()
        urltimewindow()
        incorrectab()

def adayorbdaywindows():
    global tkwidth, tkheight, xcord, ycord
    tkwidth = 590
    tkheight = 225
    screen_width = (root).winfo_screenwidth()
    screen_height = (root).winfo_screenheight()
    xcord = (screen_width/2) - (tkwidth/2)
    ycord = (screen_height/2) - (tkheight/2)
    
    global zop
    zop = Toplevel()
    zop.title("owwu")
    zop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    zop.protocol("WM_DELETE_WINDOW", killer)
    Label(zop, text="Is today an A day or a B day? Please type in the capital letter").pack(expand = YES)
    
    global day
    day = Entry(zop)
    day.pack(expand = YES)
    closebutton = Button(zop, text="Submit", command=adayorbdayclicks).pack(expand = YES)

def adayorbdayclicks():
    global teller
    teller = day.get()
    zop.destroy()
    
    dop = Toplevel()
    dop.title("uwu")
    dop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    dop.protocol("WM_DELETE_WINDOW", killer)
    Label(dop, text="All done! Just wait until it's time for your class. Minimize this tab but \n please don't close out of it because it exits the program").pack(expand = YES)
    Thread(target=loop, daemon = True).start()

def loop():
    while True:
        current_time = datetime.now()
        printed_time = current_time.strftime("%H:%M")
        if teller == "A":
            for count,i in enumerate(adaytimelist):
                if i == printed_time:
                    webbrowser.open(adayurllist[count])
                    time.sleep(61)
                    continue
        if teller == "B":
            for count,i in enumerate(bdaytimelist):
                if i == printed_time:
                    webbrowser.open(bdayurllist[count])
                    time.sleep(61)
                    continue

if path.exists("adayurls.txt") and path.exists("adaytimes.txt") and path.exists("bdayurls.txt") and path.exists("bdaytimes.txt"):
    root = Tk()
    root.withdraw()
    loader()
    adayorbdaywindows()
    root.mainloop()
else: 
    blockcount()
    root.mainloop()

