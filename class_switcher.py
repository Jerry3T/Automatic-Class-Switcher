from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
from datetime import datetime
import re
import time
from threading import Thread
import os.path
from os import path
import itertools

def killer():
    if messagebox.askyesno("Exit", "Do you want to quit the application?"):
        root.quit()

def saver():
    with open('dumpfile.txt', 'w') as handler:
        if advisory == 1:
            handler.write("1\n%s\n%s\n" % (trueadvurl, trueadvtime))
            handler.write
        for i in adayurl, adaytime, bdayurl, bdaytime:
            handler.write('%s\n' % i)

def loader():
    global adayurllist, adaytimelist, bdayurllist, bdaytimelist, trueadvurl, trueadvtime, advisory
    with open ('dumpfile.txt', 'r') as handler:
        if handler.read(1) == "1":
            advisory = handler.readline().rstrip()
            trueadvurl = handler.readline().rstrip()
            trueadvtime = handler.readline().rstrip()

        adayurl = handler.readline().rstrip()
        adayurllist = [i for i in re.split("A-", adayurl) if i != '']
        adaytime = handler.readline().rstrip()
        adaytimelist = [i for i in re.split("A-", adaytime) if i != '']
        bdayurl = handler.readline().rstrip()
        bdayurllist = [i for i in re.split("B-", bdayurl) if i != '']
        bdaytime = handler.readline().rstrip()
        bdaytimelist = [i for i in re.split("B-", bdaytime) if i != '']

def blockcount():
    global tkwidth, tkheight, xcord, ycord, classesentry, root
    root = Tk()
    root.withdraw()

    tkwidth = 600
    tkheight = 225
    screen_width = (root).winfo_screenwidth()
    screen_height = (root).winfo_screenheight()
    xcord = (screen_width/2) - (tkwidth/2)
    ycord = (screen_height/2) - (tkheight/2)

    numblocks()

def blockclick():
    global blockseparator, advisory
    try:
        blocks = classesentry.get()
        advisory = zeroor1.get()
        blockseparator = int(blocks)
        if blockseparator > 10:
            sop.destroy()
            numblocks()
            incorrectblock()
        else:
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
    rop.title("uwu")
    rop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    Label(rop, text="Please put an A- or B- in front of your BLOCK TIME AND URL so I can tell what goes where \n (For example, A-16:03 & B-https://www). \n You don't have to put anything for Advisory URL/Time").pack(expand = YES)
    closebutton = Button(rop, text="Close", command=rop.destroy).pack(expand = YES)

def incorrectab():
    mop = Toplevel()
    mop.attributes("-topmost", True)
    mop.title("uwu")
    mop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    Label(mop, text="Please make sure your fields are correct and you're \n putting an A- or B- before the proper URLs and times. Thank you").pack(expand = YES)
    closebutton = Button(mop, text="Close", command=mop.destroy).pack(expand = YES)

def incorrectblock():
    pop = Toplevel()
    pop.attributes("-topmost", True)
    pop.title("uwu")
    pop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    Label(pop, text="Please make sure you're putting in a correct number of blocks. Thank you").pack(expand = YES)
    closebutton = Button(pop, text="Close", command=pop.destroy).pack(expand = YES)

def numblocks():
    global classesentry, sop, zeroor1
    sop = Toplevel()
    sop.title("uwu")
    sop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    sop.protocol("WM_DELETE_WINDOW", killer)
    
    zeroor1 = IntVar()

    classes = Label(sop, text="How many blocks do you have? \n (please use numbers): ")
    classesentry = Entry(sop)
    classesbutton = Button(sop, text="Submit", command=blockclick)
    checkmark = Checkbutton(sop, text="If you want to include Advisory, click me", variable=zeroor1)

    classes.pack(expand=YES)
    classesentry.pack(expand=YES)
    checkmark.pack(expand=YES)
    classesbutton.pack(expand=YES)

def urltimewindow():
    global top, count, urls, times, advurl, advtime
    top = Toplevel()
    top.title("i love phil")
    top.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    top.protocol("WM_DELETE_WINDOW", killer)
    urls = []
    times = []

    if advisory == 1:
        Label(top, text="Advisory Google URL").grid(row = 0, column=5)
        advurl = Entry(top)
        advurl.grid(row = 0, column=45)
        Label(top, text="Advisory Time (HH:MM ex. 16:03)").grid(row = 0, column = 65)
        advtime = Entry(top)
        advtime.grid(row = 0, column=80)

    for i in range(1, blockseparator+1):
        Label(top, text="Block %d Google URL" % i).grid(row = 2 + i, column=5)
        myurls = Entry(top)
        myurls.grid(row = 2 + i, column=45)
        urls.append(myurls)
        Label(top, text="Block %d Time (HH:MM ex. 16:03)" % i).grid(row = 2 + i, column = 65)
        mytimes = Entry(top)
        mytimes.grid(row = 2 + i, column=80)
        times.append(mytimes)

    submitbutton = Button(top, text="Submit", command=urltimeclick).grid(row = 30, column=60)

def urltimeclick():
    global adayurllist, bdayurllist, adaytimelist, bdaytimelist, trueadvurl, trueadvtime
    urls_list = ""
    times_list = ""
    
    for i in urls:
        urls_list = urls_list + str(i.get())

    for i in times:
        times_list = times_list + str(i.get())

    if advisory == 1:
        trueadvurl = advurl.get()
        trueadvtime = advtime.get()

    try:
        global adayurl, adaytime, bdayurl, bdaytime
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
    tkwidth = 600
    tkheight = 225
    screen_width = (root).winfo_screenwidth()
    screen_height = (root).winfo_screenheight()
    xcord = (screen_width/2) - (tkwidth/2)
    ycord = (screen_height/2) - (tkheight/2)
    
    global zop
    zop = Toplevel()
    zop.title("uwu")
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

def fuckthisadayshit():
    current_time = datetime.now()
    printed_time = current_time.strftime("%H:%M")
    for count, i in enumerate(adaytimelist):
        if i == printed_time:
            webbrowser.open(adayurllist[count])
            time.sleep(61)
            fuckthisadayshit()
        
    time.sleep(1)
    fuckthisadayshit()

def fuckthisadvshit():
    current_time = datetime.now()
    printed_time = current_time.strftime("%H:%M")
    if printed_time == trueadvtime:
        webbrowser.open(trueadvurl)
        time.sleep(61)
    
    time.sleep(1)
    fuckthisadvshit()
  
def fuckthisbdayshit():
    current_time = datetime.now()
    printed_time = current_time.strftime("%H:%M")
    for count, i in enumerate(bdaytimelist):
        if i == printed_time:
            webbrowser.open(bdayurllist[count])
            time.sleep(61)
            fuckthisbdayshit()

    time.sleep(1)
    fuckthisbdayshit()

def loop():
    if advisory == "1" or 1:
        Thread(target=fuckthisadvshit, daemon = True).start()
    if teller == "A":
        Thread(target=fuckthisadayshit, daemon = True).start()
    elif teller == "B":
        Thread(target=fuckthisbdayshit, daemon = True).start()

if path.exists("dumpfile.txt"):
    root = Tk()
    root.withdraw()
    loader()
    adayorbdaywindows()
    root.mainloop()
else: 
    blockcount()
    root.mainloop()
