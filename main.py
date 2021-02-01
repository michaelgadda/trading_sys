import tkinter as tk
from tkinter import filedialog, Text, simpledialog, Label, ttk, Entry
import pullback_calc as pb
import os
import finvizscraper as fs
root = tk.Tk()

def addFile():
    #This doesnt add a task rn, instead it just opens file manager (part of tutorial)
    filename = filedialog.askopenfilename(initialdir="/", title = "select File")
    filetypes=(("executables", "*.exe"),("All files","*.*"))



canvas = tk.Canvas(root, height = 1080, width = 1920, bg = 'white')
canvas.pack()




frame = tk.Frame(root, bg = "black")
frame1 = tk.Frame(root,bg = "thistle1")
frame.place(relwidth=.5, relheight= 1, y = 100)
frame1.place(relwidth=.5, relheight=.1)
frame2 = tk.Frame(root, bg = 'orange')
frame3 = tk.Frame(root, bg = 'gold')
frame2.place(relwidth=.5, relheight= .25, y = 80, x = (1920/2))
frame3.place(relwidth=.5, relheight=.09, x = (1920/2))
frame4 = tk.Frame(root, bg = 'misty rose')
frame5 = tk.Frame(root, bg = 'royal blue')
frame4.place(relwidth=.5, relheight= .75, y = (1080*.25)+100, x = (1920/2))
frame5.place(relwidth=.5, relheight=.1, x = (1920/2), y= (1080*.25)+80)

#Title for right side sections
frame5_title = Label(frame5,text = 'Entry and Exit Calculator', font = ('daytona', 40), bg = 'royal blue').place(relx = .2, rely = .2)

frame3_title = Label(frame3,text = 'Pullback and Squeeze Calculator', font = ('daytona', 40), bg = 'gold').place(relx = .1, rely = .2)
#Adding in labels and entry boxies for inputs into the pullback/squeeze calculator

note_label = Label(frame2, text = 'If you dont want to input a value, just input 0!', bg = 'orange', fg = 'black', font = ('Baskerville Old Face', 12))
note_label.place(relx = .05, y = 22)

float_label_entry = Label(frame2, text = "Float: ", bg = 'orange')
float_label_entry.place(x=100,y=50)
float_entry = Entry(frame2, width = 25, borderwidth = 2, text = "Float: ")
float_entry.place(x= 175, y = 50)

pm_volume_label_entry = Label(frame2, text = "Pre Market Vol: ", bg = 'orange')
pm_volume_label_entry.place(x=50,y=100)
pm_volume_entry = Entry(frame2, width = 25, borderwidth = 2, text = "Pre Market Vol: ")
pm_volume_entry.place(x= 175, y = 100)

pm_range_label_entry = Label(frame2, text = "Premarket Range: ", bg = 'orange')
pm_range_label_entry.place(x=40,y=150)
pm_range_entry = Entry(frame2, width = 25, borderwidth = 2, text = "Premarket Range: ")
pm_range_entry.place(x= 175, y = 150)

open_price_retr_label_entry = Label(frame2, text = "Retracement from open:", bg = 'orange')
open_price_retr_label_entry.place(x=10,y=200)
open_price_retr_entry = Entry(frame2, width = 25, borderwidth = 2, text = "Retracement from open:")
open_price_retr_entry.place(x= 175, y = 200)

#function that takes the info given and gives output of squeeze % and pullback

def plb_sqz_output():
    flt = float(float_entry .get())
    pmv = float(pm_volume_entry.get())
    pmr = float(pm_range_entry.get())
    opr = float(open_price_retr_entry.get())
    plb_sqz_list = pb.pb_sqz_calculator(flt, pmv, pmr, opr)
    #turning floats into percentages
    plb_sqz0 = "{:.1%}".format(plb_sqz_list[0])
    plb_sqz1 = "{:.1%}".format(plb_sqz_list[1])

    pmv_label = Label(frame2, text= plb_sqz0, bg='orange', font= (None, 25))
    pmv_label.place(relx = .7, y = 50)
    pmv_label1 = Label(frame2, text= 'Avg. Pullback %:', bg='orange', font=(None, 15))
    pmv_label1.place(relx=.5, y=57)


    pmr_label = Label(frame2, text= plb_sqz1, bg='orange', font= (None, 25))
    pmr_label.place(relx = .7 , y = 100)
    pmr_label1 = Label(frame2, text='Avg. Squeeze %:', bg='orange', font=(None, 15))
    pmr_label1.place(relx=.5, y=107)

    opr_label = Label(frame2, text=plb_sqz_list[2], bg='orange', font=(None, 25))
    opr_label.place(relx=.7, y=150)
    opr_label1 = Label(frame2, text= 'Sample Count:', bg='orange', font= (None, 15))
    opr_label1.place(relx = .5, y = 157)

output_plb_sqz = tk.Button(frame2, text = "Get Pullback and Squeeze %", command = plb_sqz_output, bg = 'green', fg = 'thistle1')
output_plb_sqz.place(x= 175, y =235)

#Entry and exit calc -- placing input areas first

min_req_entry_label = Label(frame4, text = "Min Required Average Entry Price",  bg = 'royal blue', fg = 'misty rose')
min_req_entry_label.place(x=5,y=100)
min_req_entry = Entry(frame4, width = 25, borderwidth = 2, text = "Price")
min_req_entry.place(x= 200, y = 100)

planned_exit_label_entry = Label(frame4, text = "Planned Exit Price:",  bg = 'royal blue', fg = 'misty rose')
planned_exit_label_entry.place(x=80,y=150)
planned_exit_entry = Entry(frame4, width = 25, borderwidth = 2, text = "Planned Exit Price:")
planned_exit_entry.place(x= 200, y = 150)

planned_stop_label_entry = Label(frame4, text = "Planned Stop out price: ",  bg = 'royal blue', fg = 'misty rose')
planned_stop_label_entry.place(x=50,y=200)
planned_stop_entry = Entry(frame4, width = 25, borderwidth = 2, text = "Planned Stop out price: ")
planned_stop_entry.place(x= 200, y = 200)

risk_amount_label_entry = Label(frame4, text = "Dollar Risk Amount: ", bg = 'royal blue', fg = 'misty rose')
risk_amount_label_entry.place(x=70,y=250)
risk_amount_entry = Entry(frame4, width = 25, borderwidth = 2, text = "Dollar Risk Amount:  ")
risk_amount_entry.place(x= 200, y = 250)
#info label
info_label = Label(frame4, text="Trade Information", bg='misty rose', font=("Verdana 15 underline"))
info_label.place(relx=.1, y=300)


def entry_exit_calc():
    min_entry = float(min_req_entry.get())
    pl_exit = float(planned_exit_entry.get())
    pl_stop = float(planned_stop_entry .get())
    risk_am = float(risk_amount_entry.get())



    percent_gain = (pl_exit - min_entry)/min_entry
    percent_loss = (min_entry - pl_stop)/pl_stop
    pct_gain = "{:.1%}".format(percent_gain)
    pct_loss = "{:.1%}".format(percent_loss)

    max_pos_size = risk_am/percent_loss
    mxs = "${}".format(int(max_pos_size))

    est_gain = max_pos_size*percent_gain
    eg = "${}".format(int(est_gain))

    max_shares = max_pos_size//min_entry
    ms = "{} Shares".format(max_shares)

    R_R = est_gain//risk_am
    rr = "{}Rs".format(R_R)


    pct_gain_label = Label(frame4, text= pct_gain, bg='green2', font= (None, 15), width = 25)
    pct_gain_label.place(relx = .4, y = 350)
    pct_gain_label1 = Label(frame4, text= 'Est. % Gain:', bg='misty rose', font=(None, 15))
    pct_gain_label1.place(relx=.1, y=350)


    pct_loss_label = Label(frame4, text= pct_loss, bg='red2', font= (None, 15), width = 25)
    pct_loss_label.place(relx = .4 , y = 400)
    pct_loss_label1 = Label(frame4, text='Est. % at Risk:', bg='misty rose', font=(None, 15))
    pct_loss_label1.place(relx=.1, y=400)

    mxs_label = Label(frame4, text=mxs, bg='Green', fg = 'snow', font=(None, 15), width = 25)
    mxs_label.place(relx=.4, y=450)
    mxs_label1 = Label(frame4, text= 'Max. Position Size:', bg='misty rose', fg = 'black', font= (None, 15))
    mxs_label1.place(relx = .1, y = 450)

    eg_label = Label(frame4, text=eg, bg='green2', fg='black', font=(None, 15), width = 25)
    eg_label.place(relx=.4, y=500)
    eg_label1 = Label(frame4, text='Estimated Dollar Gain:', bg='misty rose', fg='black', font=(None, 15))
    eg_label1.place(relx=.1, y=500)

    ms_label = Label(frame4, text=ms, bg='slate gray', fg='white', font=(None, 15), width = 25)
    ms_label.place(relx=.4, y=550)
    ms_label1 = Label(frame4, text='Max. Shares:', bg='misty rose', fg='black', font=(None, 15))
    ms_label1.place(relx=.1, y=550)

    rr_label = Label(frame4, text=rr, bg='slate gray', fg='white', font=(None, 15), width = 15)
    rr_label.place(relx=.4, y=600)
    rr_label1 = Label(frame4, text='R/R:', bg='misty rose', fg='black', font=(None, 15))
    rr_label1.place(relx=.1, y=600)

entry_exit_output = tk.Button(frame4, text = "Get Trade Info", command = entry_exit_calc, bg = 'white', fg = 'black', font = ("Calisto_MT 15 bold") )
entry_exit_output.place(relx = .55, rely = .2, width = 200, height = 50)


#float, pm_volume, pm_range, open_price_retr

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup,text= msg)
    label.pack(side = "top", fill = 'x', pady = 10)
    pu_button = ttk.Button(popup, text="Okay", command = popup.destroy())
    pu_button.pack()
    popup.mainloop()

listnum = 0

def addImpInfo():
    global listnum


    if listnum == 5:
        popupmsg("Remove current stock info to add more")

    global marketCapLabel
    global InstOwnLabel
    global ATRLabel
    global floatLabel
    global ShortFloatLabel
    global tickerLabel
    tickerList = fs.findImpInfoOnTicker()
    marketCapLabel = Label(frame, text = "Market Cap: " + str(tickerList[0]), fg = 'black')
    floatLabel = Label(frame, text = "Float: " + str(tickerList[1]), fg = 'black')
    ShortFloatLabel = Label(frame, text="Short Float: " + str(tickerList[2]), fg='black')
    ATRLabel = Label(frame, text="ATR: " + str(tickerList[3]), fg='black')
    InstOwnLabel = Label(frame, text="Inst Own: " + str(tickerList[4]), fg='black')
    tickerLabel = Label(frame, text = tickerList[5], fg = 'blue')
    tickerLabel.pack(pady=10)
    marketCapLabel.pack(pady= 5)
    floatLabel.pack(pady= 5)
    ShortFloatLabel.pack(pady= 5)
    InstOwnLabel.pack(pady= 5)
    ATRLabel.pack(pady= 5)
    listnum +=1

def deleteStockInfo():
    global listnum
    listnum = 0
    marketCapLabel.destroy()
    InstOwnLabel.destroy()
    floatLabel.destroy()
    ShortFloatLabel.destroy()
    ATRLabel.destroy()
    for widget in frame.winfo_children():
        widget.destroy()

AddStockInfo = tk.Button(frame1, text = "Get Stock Info", padx = 5, pady = 5, fg = 'black', bg = 'white', command = addImpInfo)
AddStockInfo.pack(pady = 5, side = 'top')


removeInfo = tk.Button(frame1, text = "Remove Stock Info", command = deleteStockInfo, bg = 'red')
removeInfo.pack(pady= 10, side = 'top')






root.mainloop();