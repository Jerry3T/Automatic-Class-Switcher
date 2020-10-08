from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
import webbrowser
from datetime import datetime
import re
import time
from threading import Thread
import os.path
from os import path

def killer():
    if messagebox.askyesno("Exit", "Do you want to quit the application?"):
        root.quit()

def saver():
    with open('dumpfile.txt', 'w') as handler:
        if advisory == 1 and advisorynum == 1:
            handler.write("1\n%s\n%s\n" % (trueadvurl1, trueadvtime1))
        elif advisory == 1 and advisorynum == 2:
            handler.write("2\n%s\n%s\n%s\n%s\n" % (trueadvurl1, trueadvtime1, trueadvurl2, trueadvtime2))
        else:
            handler.write('0\n')
        for i in adayurl, adaytime, bdayurl, bdaytime:
            handler.write('%s\n' % i)

def loader():
    global adayurllist, adaytimelist, bdayurllist, bdaytimelist
    with open ('dumpfile.txt', 'r') as handler:
        yeet = handler.readline().rstrip()
        if yeet == "1":
            trueadvurl1 = handler.readline().rstrip()
            trueadvtime1 = handler.readline().rstrip()
            adayurl = handler.readline().rstrip()
            adaytime = handler.readline().rstrip()
            bdayurl = handler.readline().rstrip()
            bdaytime = handler.readline().rstrip()

            adayurllist = [i for i in re.split("Aday=", adayurl) if i != '']
            adaytimelist = [i for i in re.split("Aday=", adaytime) if i != '']
            bdayurllist = [i for i in re.split("Bday=", bdayurl) if i != '']
            bdaytimelist = [i for i in re.split("Bday=", bdaytime) if i != '']
            
            adayurllist.append(trueadvurl1)
            adaytimelist.append(trueadvtime1)
            bdayurllist.append(trueadvurl1)
            bdaytimelist.append(trueadvtime1)

        elif yeet == "2":
            trueadvurl1 = handler.readline()[5:].rstrip()
            trueadvtime1 = handler.readline()[5:].rstrip()
            trueadvurl2 = handler.readline()[5:].rstrip()
            trueadvtime2 = handler.readline()[5:].rstrip()
            adayurl = handler.readline().rstrip()
            adaytime = handler.readline().rstrip()
            bdayurl = handler.readline().rstrip()
            bdaytime = handler.readline().rstrip()

            adayurllist = [i for i in re.split("Aday=", adayurl) if i != '']
            adaytimelist = [i for i in re.split("Aday=", adaytime) if i != '']
            bdayurllist = [i for i in re.split("Bday=", bdayurl) if i != '']
            bdaytimelist = [i for i in re.split("Bday=", bdaytime) if i != '']

            adayurllist.append(trueadvurl1)
            adaytimelist.append(trueadvtime1)
            bdayurllist.append(trueadvurl2)
            bdaytimelist.append(trueadvtime2)
        else:
            adayurl = handler.readline().rstrip()
            adaytime = handler.readline().rstrip()
            bdayurl = handler.readline().rstrip()
            bdaytime = handler.readline().rstrip()

            adayurllist = [i for i in re.split("Aday=", adayurl) if i != '']
            adaytimelist = [i for i in re.split("Aday=", adaytime) if i != '']
            bdayurllist = [i for i in re.split("Bday=", bdayurl) if i != '']
            bdaytimelist = [i for i in re.split("Bday=", bdaytime) if i != '']
            
def blockcount():
    global tkwidth, tkheight, xcord, ycord, classesentry, root, fontStyle
    root = Tk()
    root.withdraw()
    fontStyle = tkFont.Font(family="Lucida Grande", size=12)

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
        elif advisory == 1:
            sop.destroy()
            numadvisory()
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
    Label(rop, text="Please put an Aday= or Bday= in front of your BLOCK TIME AND URL \n so I can tell what goes where (For example, Aday=16:03 & Bday=https://www). \n If you have two advisories, please include the Aday= and Bday= \n If you have one, don't include them", font=fontStyle).pack(expand = YES)
    closebutton = Button(rop, text="Close", command=rop.destroy).pack(expand = YES)

def incorrectab():
    mop = Toplevel()
    mop.attributes("-topmost", True)
    mop.title("uwu")
    mop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    Label(mop, text="Please make sure your fields are correct and you're \n putting an Aday= or Bday= before the proper URLs and times. Thank you", font=fontStyle).pack(expand = YES)
    closebutton = Button(mop, text="Close", command=mop.destroy).pack(expand = YES)

def incorrectblock():
    pop = Toplevel()
    pop.attributes("-topmost", True)
    pop.title("uwu")
    pop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    Label(pop, text="Please make sure you're putting in a correct number of blocks. Thank you", font=fontStyle).pack(expand = YES)
    closebutton = Button(pop, text="Close", command=pop.destroy).pack(expand = YES)

def numadvisory():
    global numadv, fop
    fop = Toplevel()
    fop.attributes("-topmost", True)
    fop.title("uwu")
    fop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    Label(fop, text="How many advisories do you have?", font=fontStyle).pack(expand = YES)
    numadv = Entry(fop)
    numadv.pack(expand = YES)
    submitbutton = Button(fop, text="Submit", command=number).pack(expand = YES)

def number():
    global advisorynum
    advisorynum = int(numadv.get())
    if advisorynum >= 3:
        fop.destroy()
        dop = Toplevel()
        dop.attributes("-topmost", True)
        dop.title("uwu")
        dop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
        Label(dop, text="Die", font=fontStyle).pack(expand = YES)
        numadvisory()
    else:
        fop.destroy()
        urltimewindow()
        abnotice()

def numblocks():
    global classesentry, sop, zeroor1
    sop = Toplevel()
    sop.title("uwu")
    sop.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    sop.protocol("WM_DELETE_WINDOW", killer)
    
    zeroor1 = IntVar()

    classes = Label(sop, text="How many blocks do you have? \n (please use numbers): ", font=fontStyle)
    classesentry = Entry(sop)
    classesbutton = Button(sop, text="Submit", command=blockclick)
    checkmark = Checkbutton(sop, text="If you want to include Advisory, click me", variable=zeroor1)

    classes.pack(expand=YES)
    classesentry.pack(expand=YES)
    checkmark.pack(expand=YES)
    classesbutton.pack(expand=YES)

def urltimewindow():
    global top, count, urls, times, advurl, advtime, advurl1, advtime1, advurl2, advtime2
    top = Toplevel()
    top.title("i love phil")
    top.geometry("%dx%d+%d+%d" % (tkwidth, tkheight, xcord, ycord))
    top.protocol("WM_DELETE_WINDOW", killer)
    urls = []
    times = []

    if advisory == 1 and advisorynum == 1:
        Label(top, text="Advisory Google URL").grid(row = 0, column=5)
        advurl1 = Entry(top)
        advurl1.grid(row = 0, column=45)
        Label(top, text="Advisory Time (HH:MM ex. 16:03)").grid(row = 0, column = 65)
        advtime1 = Entry(top)
        advtime1.grid(row = 0, column=80)
    elif advisory == 1 and advisorynum == 2:
        Label(top, text="Advisory Google URL").grid(row = 0, column=5)
        advurl1 = Entry(top)
        advurl1.grid(row = 0, column=45)
        Label(top, text="Advisory Time (HH:MM ex. 16:03)").grid(row = 0, column = 65)
        advtime1 = Entry(top)
        advtime1.grid(row = 0, column=80)
        Label(top, text="Advisory Google URL").grid(row = 2, column=5)
        advurl2 = Entry(top)
        advurl2.grid(row = 2, column=45)
        Label(top, text="Advisory Time (HH:MM ex. 16:03)").grid(row = 2, column = 65)
        advtime2 = Entry(top)
        advtime2.grid(row = 2, column=80)

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
    global adayurllist, bdayurllist, adaytimelist, bdaytimelist, trueadvurl1, trueadvtime1, trueadvurl2, trueadvtime2
    urls_list = ""
    times_list = ""
    
    for i in urls:
        urls_list = urls_list + str(i.get())

    for i in times:
        times_list = times_list + str(i.get())

    if advisory == 1 and advisorynum == 1:
        trueadvurl1 = advurl1.get()
        trueadvtime1 = advtime1.get()
    elif advisory == 1 and advisorynum == 2:
        trueadvurl1 = advurl1.get()
        trueadvtime1 = advtime1.get()
        trueadvurl2 = advurl2.get()
        trueadvtime2 = advtime2.get()

    try:
        global adayurl, adaytime, bdayurl, bdaytime
        adayurl = urls_list[:urls_list.index("Bday=")]
        adaytime = times_list[:times_list.index("Bday=")]
        bdayurl = urls_list[urls_list.index("Bday="):]
        bdaytime = times_list[times_list.index("Bday="):]
        adayurllist = [i for i in re.split("Aday=", adayurl) if i != '']
        adaytimelist = [i for i in re.split("Aday=", adaytime) if i != '']
        bdayurllist = [i for i in re.split("Bday=", bdayurl) if i != '']
        bdaytimelist = [i for i in re.split("Bday=", bdaytime) if i != '']
        saver()
        top.destroy()
        loader()
        adayorbdaywindows()
    except ValueError:
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
    Label(zop, text="Is today an A day or a B day? Please type in the capital letter", font=fontStyle).pack(expand = YES)
    
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
    Label(dop, text="All done! Just wait until it's time for your class. Minimize this tab but \n please don't close out of it because it exits the program", font=fontStyle).pack(expand = YES)
    Thread(target=loop, daemon = True).start()

def loop():
    while True:
        current_time = datetime.now()
        printed_time = current_time.strftime("%H:%M")
        if teller == "A":
            for count,i in enumerate(adaytimelist):
                print(i, adayurllist, count)
                if i == printed_time:
                    webbrowser.open(adayurllist[count])
                    time.sleep(61)
        if teller == "B":
            for sount,i in enumerate(bdaytimelist):
                print(sount, i, bdayurllist)
                if i == printed_time:
                    webbrowser.open(bdayurllist[sount])
                    time.sleep(61)

if path.exists("dumpfile.txt"):
    root = Tk()
    root.withdraw()
    fontStyle = tkFont.Font(family="Lucida Grande", size=12)
    loader()
    adayorbdaywindows()
    root.mainloop()
else: 
    blockcount()
    root.mainloop()
