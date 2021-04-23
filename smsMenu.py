import tkinter as tk
import PyPDF2
import requests
import tkinter.font as tkFont
import customtkinter
from PIL import Image, ImageTk
import sqlite3


#################################
####  DATABASE CREATION  ########
#################################

# If I HAD one!




root = tk.Tk()


root.iconbitmap("msgicon.ico")
root.title("    -SMS Caster-  (Python Edition!)")
root.resizable(width=False, height=False)
fontStyle = tkFont.Font(root, family="Unispace", size=60)
customtkinter.set_appearance_mode("Dark")
canvas = tk.Canvas(root, width=940, height=610, bg="#323232")
canvas.grid(columnspan=3, rowspan=3)

#Logo
logo = Image.open('logo.png')
logo = logo.resize((120, 120), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)

logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=0, row=0)




def Send_SMS():

	target_number=entry.get()
	message_content=message_capture.get()

	resp = requests.post('https://textbelt.com/text', {
  'phone': (target_number),
  'message': (message_content),
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



# Checks if the input box stored the correct value,
def StoreTarget():

	target_number=entry.get()
	message_content=message_capture.get()
	print("\n\n\n***********  CHECK INPUT FUNCTION *************")
	print(target_number)
	print("\n\n\n\n ***** Message Content *****")
	print(message_content)




def Settings():
	def hideSettings():
		settingsexitbutton.place_forget()
		settingsframe.place_forget()
		settingstitle.place_forget()
		setting1.place_forget()
		setting2.place_forget()



	numberlabel.place_forget()
	message_capture.place_forget()
	entry.place_forget()

	settingsframe = customtkinter.CTkFrame(master=root,
	                                    width=590,
										height=520,
										corner_radius=15,
										fg_color="#616161",
										bg_color="#323232")
	settingsframe.place(relx=0.65, rely=0.5, anchor=tk.CENTER)

	settingsexitbutton = customtkinter.CTkButton(master=root,
	                                        image=settingsexit,
											width=40,
											height=40,
											fg_color=("#616161"),
											bg_color=("#616161"),
											text="Options",
											hover_color=("#3f3f3f"),
											command=hideSettings)
	settingsexitbutton.place(relx=0.40, rely=0.84)

	settingstitle = tk.Label(root, text="SMS-Caster Settings ",
	                 bg="#616161",
					 fg="#FFFFFF")

	settingstitle.grid(columnspan=3, column=1, row=0)
	settingstitle.config(font=("Franklin Gothic Demi Cond", 24))
	settingstitle.place(relx= 0.51, rely = 0.14)

	setting1 = tk.Label(root, text="Setting option 1 ",
	                 bg="#616161",
					 fg="#FFFFFF")

	setting1.grid(columnspan=3, column=1, row=0)
	setting1.config(font=("Calibri", 18))
	setting1.place(relx= 0.40, rely = 0.28)

	setting2 = tk.Label(root, text="Setting option 2 ",
	                 bg="#616161",
					 fg="#FFFFFF")

	setting2.grid(columnspan=3, column=1, row=0)
	setting2.config(font=("Calibri", 18))
	setting2.place(relx= 0.40, rely = 0.36)

def InfoPage():

	def hideSettings():
		infoexitbutton.place_forget()
		infoframe.place_forget()
		infotitle.place_forget()
		phone_pic.place_forget()
		vertitle.place_forget()



	numberlabel.place_forget()
	message_capture.place_forget()
	entry.place_forget()

	infoframe = customtkinter.CTkFrame(master=root,
	                                    width=590,
										height=520,
										corner_radius=15,
										fg_color="#616161",
										bg_color="#323232")
	infoframe.place(relx=0.65, rely=0.5, anchor=tk.CENTER)

	infoexitbutton = customtkinter.CTkButton(master=root,
	                                        image=settingsexit,
											width=40,
											height=40,
											fg_color=("#616161"),
											bg_color=("#616161"),
											text="Options",
											hover_color=("#3f3f3f"),
											command=hideSettings)
	infoexitbutton.place(relx=0.40, rely=0.84)

	infotitle = tk.Label(root, text="SMS-CASTER\n(Python Edition) ",
	                 bg="#616161",
					 fg="#FFFFFF")

	infotitle.grid(columnspan=3, column=1, row=0)
	infotitle.config(font=("Franklin Gothic Demi Cond", 24))
	infotitle.place(relx= 0.54, rely = 0.14)

	phone_icon = ImageTk.PhotoImage(Image.open("phone3.png").resize((200, 200)))
	phone_pic = customtkinter.CTkButton(master=root,
	                                        image=phone_icon,
											width=240,
											height=240,
											fg_color=("#616161"),
											bg_color=("#616161"),
											text="Options",
											hover_color=("#616161"),
											command=InfoPage)
	phone_pic.place(relx=0.53, rely=0.28)

	vertitle = tk.Label(root, text="Version 0.2 (Alpha) \nby Ctab.Tech",
	                 bg="#616161",
					 fg="#FFFFFF")

	vertitle.grid(columnspan=3, column=1, row=0)
	vertitle.config(font=("Calbri", 16))
	vertitle.place(relx= 0.56, rely = 0.68)






def StoredResponses():
	numberlabel.place_forget()
	message_capture.place_forget()
	entry.place_forget()
	innerframe.place_forget()

	#Set up the Stored Responses Frame Content
	innerframe.place(relx=0.65, rely=0.30, anchor=tk.CENTER)

	SRlabel = customtkinter.CTkLabel(master=root,
	                               text="Stored Responses :)",
	                               width=120,
	                               height=25,
	                               corner_radius=8,
								   bg_color="#616161")
	SRlabel.place(relx=0.4, rely=0.15,)








def SingleSMS():
	innerframeSR.place_forget()
	numberlabel.place_forget()
	message_capture.place_forget()
	entry.place_forget()
	SRlabel.place_forget()


	innerframe.place()
	numberlabel.place(relx=0.4, rely=0.15,)
	message_capture.place(relx=0.385, rely=0.22)
	entry.place(relx=0.53, rely=0.15)

	#settingsframe.place_forget()










# Image calls for custom buttons,
settings_icon = ImageTk.PhotoImage(Image.open("settings.ico").resize((40, 40)))
msglogoref = ImageTk.PhotoImage(Image.open("msgicon.ico").resize((40, 40)))
settingsexit = ImageTk.PhotoImage(Image.open("exit.ico").resize((20, 20)))
info_icon = ImageTk.PhotoImage(Image.open("info.ico").resize((40, 40)))





# Frames seen on the Starter Screen.

sideframe = customtkinter.CTkFrame(master=root,
								   width=230,
								   height=520,
								   corner_radius=15,
								   fg_color="#3f3f3f",
								   bg_color="#323232")
sideframe.place(relx=0.18, rely=0.5, anchor=tk.CENTER)

wholeframe = customtkinter.CTkFrame(master=root,
                                    width=590,
									height=520,
									corner_radius=15,
									fg_color="#3f3f3f",
									bg_color="#323232")
wholeframe.place(relx=0.65, rely=0.5, anchor=tk.CENTER)

innerframeSR = customtkinter.CTkFrame(master=root,
									width=540,
									height=220,
									corner_radius=15,
									fg_color="#616161",
									bg_color="#3f3f3f")
innerframeSR.place(relx=0.65, rely=0.30, anchor=tk.CENTER)

innerframe = customtkinter.CTkFrame(master=root,
                                    width=540,
									height=220,
									corner_radius=15,
									fg_color="#616161",
									bg_color="#3f3f3f")
innerframe.place(relx=0.65, rely=0.30, anchor=tk.CENTER)


# Title of the program in the side menu,
msglogo = customtkinter.CTkButton(master=root,
                                        image=msglogoref,
										width=40,
										height=40,
										fg_color=("#3f3f3f"),
										bg_color=("#3f3f3f"),
										text="Options",
										hover_color=("#3f3f3f"),
										command=Send_SMS)
msglogo.place(relx=0.085, rely=0.10)


title = tk.Label(root, text="   SMS-CASTER ",
                 bg="#3f3f3f",
				 fg="#FFFFFF")

title.grid(columnspan=3, column=1, row=0)
title.config(font=("Franklin Gothic Demi Cond", 14))
title.place(relx= 0.135, rely = 0.11)

split = tk.Label(root, text=" ____________________ ",
                 bg="#3f3f3f",
				 fg="#FFFFFF")

split.grid(columnspan=3, column=1, row=0)
split.config(font=("Franklin Gothic Demi Cond", 14))
split.place(relx= 0.07, rely = 0.37)



# ALL of the Single SMS Content

numberlabel = customtkinter.CTkLabel(master=root,
                               text="Phone Number",
                               width=120,
                               height=25,
                               corner_radius=8,
							   bg_color="#616161")
numberlabel.place(relx=0.4, rely=0.15,)


entry = customtkinter.CTkEntry(master=root,
                               width=80,
                               height=25,
                               corner_radius=10,
							   bg_color="#616161")

entry.place(relx=0.53, rely=0.15)


message_capture = customtkinter.CTkEntry(master=root,
                               width=500,
                               height=140,
                               corner_radius=10,
							   bg_color="#616161")

message_capture.place(relx=0.385, rely=0.22)






# Buttons! all the Buttons!

confirmnumberbutton = customtkinter.CTkButton(master=root,
                                              width=130,
											  height=26,
											  fg_color=("#1c94cf"),
											  bg_color=("#616161"),
											  text="Confirm Number",
											  command=lambda: StoreTarget())
confirmnumberbutton.place(relx=0.60, rely=0.84)

button2 = customtkinter.CTkButton(master=root,
                                  width=190,
								  height=25,
								  fg_color=("#1c94cf"),
								  bg_color=("#3f3f3f"),
								  text="Send Default SMS",
								  command=Send_SMS)
button2.place(relx=0.08, rely=0.2)

button3 = customtkinter.CTkButton(master=root,
                                  width=190,
								  height=25,
								  fg_color=("#1c94cf"),
								  bg_color=("#3f3f3f"),
								  text="Stored Templates",
								  command=StoredResponses)
button3.place(relx=0.08, rely=0.26)

button4 = customtkinter.CTkButton(master=root,
                                  width=190,
								  height=25,
								  fg_color=("#1c94cf"),
								  bg_color=("#3f3f3f"),
								  text="Send Single SMS",
								  command=SingleSMS)
button4.place(relx=0.08, rely=0.32)

button5 = customtkinter.CTkButton(master=root,
                                  width=190,
								  height=25,
								  fg_color=("#1c94cf"),
								  bg_color=("#3f3f3f"),
								  text="SMS Marketing",
								  command=SingleSMS)
button5.place(relx=0.08, rely=0.45)

optionsbutton = customtkinter.CTkButton(master=root,
                                        image=settings_icon,
										width=40,
										height=40,
										fg_color=("#3f3f3f"),
										bg_color=("#3f3f3f"),
										text="Options",
										hover_color=("#3f3f3f"),
										command=Settings)
optionsbutton.place(relx=0.08, rely=0.84)

infobutton = customtkinter.CTkButton(master=root,
                                        image=info_icon,
										width=40,
										height=40,
										fg_color=("#3f3f3f"),
										bg_color=("#3f3f3f"),
										text="Options",
										hover_color=("#3f3f3f"),
										command=InfoPage)
infobutton.place(relx=0.16, rely=0.84)









root.mainloop()
