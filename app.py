from tkinter import *
import requests, json
from datetime import datetime, date, timedelta
import re
from weather_utils import cities, get

import tkinter.messagebox as MessageBox


def go():
    city = entry.get()
    try:
        lo = 0
        hi = len(autocompleteList)-1
        while lo<=hi:
            mid = (lo+hi)//2
            if (autocompleteList[mid].lower()) == city.lower():
                break
            elif (autocompleteList[mid].lower()) < city.lower():
                lo = mid + 1
            else:
                hi = mid - 1
        if lo <= hi:
            dic = get(city) 
        else:
            raise Exception("Invalid location")
    except requests.exceptions.ConnectionError:
        MessageBox.showwarning("Alert", "Computer not Connected to the internet")
        return
    except ValueError:
        MessageBox.showwarning("Alert", "Server Error")
        return
    except:
        MessageBox.showwarning("Alert", "Invalid City!")
        return
    
    main = Toplevel()  
    main.geometry('450x450+200+200')
    main.title(city)
    main.geometry("{0}x{1}+0+0".format(main.winfo_screenwidth(), main.winfo_screenheight()))
    main.resizable(width=False, height=False)

    
    tmp = dic['today']['temp']
    tmp_min = dic['today']['min']
    tmp_max = dic['today']['max']
    t = tmp
    tmp = str(tmp) + "°C"
    tmp_min = "Min : " + str(tmp_min) + "°C"
    tmp_max = "Max : " + str(tmp_max) + "°C"

    canvas = Canvas(main, width=1920, height=1080)
    canvas.create_image(0, 0, anchor=NW, image=back_img2)
    canvas.create_text(screen_width / 2, screen_height * 0.066667, text=city, fill="white", font="Comic 60 ")
    canvas.create_image(main.winfo_screenwidth() // 12, main.winfo_screenheight() * 2 * 0.066667 * 3.5, image=therm1)
    canvas.create_text(screen_width * 0.066667 * 4, screen_height * 5.5 * 0.066667, text=tmp_min, fill="white", font="Sans 30 ")
    canvas.create_text(screen_width * 0.066667 * 11, screen_height * 5.5 * 0.066667, text=tmp_max, fill="white", font="Sans 30 ")

   
    if t <= 2:
        canvas.create_image(screen_width / 12, screen_height * 2 * 0.066667 * 3.5, image=therm1)
    elif t <= 15:
        canvas.create_image(screen_width / 12, screen_height * 2 * 0.066667 * 3.5, image=therm2)
    elif t <= 25:
        canvas.create_image(screen_width / 12, screen_height * 2 * 0.066667 * 3.5, image=therm3)
    elif t <= 35:
        canvas.create_image(screen_width / 12, screen_height * 2 * 0.066667 * 3.5, image=therm4)
    else:
        canvas.create_image(screen_width / 12, screen_height * 2 * 0.066667 * 3.5, image=therm5)

    canvas.create_text(screen_width / 2, screen_height * 7.2 * 0.066667, text=dic['today']['desc'], fill="white", font="Sans 40")
    canvas.create_line(screen_width / 5, screen_height * 8 * 0.066667, screen_width / 1.2, screen_height * 8 * 0.066667, fill="white", width=0.1)
    canvas.create_text(screen_width / 3.8, screen_height * 9 * 0.066667, text=dic[1]['day'], fill="white", font="Sans 20 bold")
    canvas.create_text(screen_width / 2.3, screen_height * 9 * 0.066667, text=dic[2]['day'], fill="white", font="Sans 20 bold")
    canvas.create_text(screen_width / 1.65, screen_height * 9 * 0.066667, text=dic[3]['day'], fill="white", font="Sans 20 bold")
    canvas.create_text(screen_width / 1.3, screen_height * 9 * 0.066667, text=dic[4]['day'], fill="white", font="Sans 20 bold")

    canvas.pack()


def matches(fieldValue, acListEntry):
    pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
    return re.search(pattern, acListEntry)


if __name__ == '__main__':
    autocompleteList = list(set(cities()))  
    autocompleteList.sort()

    win = Tk()
    win.geometry("320x180+600+400")
    win.resizable(width=False, height=False)
    win.title('Weather Reporter')

    back_label = Label(win)
    back_label.place(x=0, y=0, relwidth=1, relheight=1)

    entry = autocompleteist(autocompleteList, win, listboxLength=6, width=32, matchesFunction=matches)
    entry.insert(END, 'Enter City Here ...')
    entry.place(relx=0.5, rely=0.5, anchor=CENTER)

    b = Button(text="GO", command=go, width=50, height=50, font=("Comic sans ms", 10, "bold"), compound=RIGHT, bg="light blue", relief=RIDGE)
    b.place(relx=0.5, rely=0.7, anchor=CENTER)

    
    therm1 = PhotoImage(file="path/to/therm1.png")
    therm2 = PhotoImage(file="path/to/therm2.png")
    therm3 = PhotoImage(file="path/to/therm3.png")
    therm4 = PhotoImage(file="path/to/therm4.png")
    therm5 = PhotoImage(file="path/to/therm5.png")

    win.mainloop()
