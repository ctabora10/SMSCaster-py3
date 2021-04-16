import tkinter as tk
import PyPDF2
import requests
import tkinter.font as tkFont
import customtkinter 
from PIL import Image, ImageTk


root = tk.Tk()

root.resizable(width=False, height=False)



fontStyle = tkFont.Font(root, family="Lucida Grande", size=60)

canvas = tk.Canvas(root, width=940, height=610, bg="#ccffff")
canvas.grid(columnspan=3, rowspan=3)

#Logo
logo = Image.open('logo.png')
logo = logo.resize((120, 120), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)

logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=0)




def Send_SMS():
	resp = requests.post('https://textbelt.com/text', {
  'phone': '8162673876',
  'message': 'TESING DEFAULT',
  'key': '3ab03b66488923feeada54e25e5118781c190991RIHEVBwMxq0XoZuG8EsnZNJyl',
})
	print(resp.json())
	return

def button2_event():
    print("button2 event was pressed. hoe..")
    
def secondWindow():    
    
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(root)
  
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
  
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
  
    # A Label widget to show in toplevel
    Label(newWindow, 
          text ="This is a new window").pack()
    
    
# Frames seen on the Starter Screen. 

sideframe = customtkinter.CTkFrame(master=root, width=280, height=520, corner_radius=15, fg_color="#ffffff", bg_color="#ccffff")
sideframe.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

wholeframe = customtkinter.CTkFrame(master=root, width=410, height=520, corner_radius=15, fg_color="#ffffff", bg_color="#ccffff")
wholeframe.place(relx=0.72, rely=0.5, anchor=tk.CENTER)
    
    
#instructions
title = tk.Label(root, text=" SMS-CASTER \n (Python Edition!)", bg="#ffffff", fg="#000000")
title.grid(columnspan=3, column=1, row=0)
title.config(font=("Unispace", 14))
title.place(relx= 0.13, rely = 0.09)  
    
    
    
    





#ButtonS
#button1_text = tk.StringVar()
#button1_btn = tk.Button(root, textvariable=button1_text, command=lambda:Send_SMS(), bg="#376fb3", fg="white", height=2, width=40)
#button1_text.set("Send Default Test Message")
#button1_btn.grid(column=1,row =1)


phone = Image.open('phone.png')
phone = phone.resize((260, 500), Image.ANTIALIAS)
phone = ImageTk.PhotoImage(phone)
phone_label = tk.Label(image=phone)
phone_label.image = phone
phone_label.grid(column=0, row=0)
phone_label.place(relx=0.59, rely=0.09)



button2 = customtkinter.CTkButton(master=root, width=240, height=40, fg_color=("lightblue"), text="Send Default SMS",command=button2_event)
button2.place(relx=0.125, rely=0.2)


button3 = customtkinter.CTkButton(master=root, width=240, height=40, fg_color=("lightblue"), text="Change Number",command=secondWindow)
button3.place(relx=0.125, rely=0.28)




root.mainloop()
