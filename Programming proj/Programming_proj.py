
import os
from re import A
from tkinter.tix import ComboBox
os.system("pip install customtkinter")
os.system("pip install pillow")
os.system("pip install BeautifulSoup4")
os.system("pip install requests --upgrade")


from PIL import Image, ImageTk
from customtkinter import *
import customtkinter
import webbrowser
import urllib.request


from bs4 import BeautifulSoup

import requests

app = CTk()
app.geometry("500x500")
app.attributes('-fullscreen',True)

set_appearance_mode("dark")



def click_handler():
    SongName = entrySong.get()
    ArtistName = entryArtist.get()
    Song = f"{ArtistName} {SongName}-lyrics"
    Song = Song.replace(" ","-")
    url = "https://genius.com/a"
    url = url.replace("a",Song)

    #webbrowser.open(url)

    url = requests.get(url)
    htmltext = url.text


    soup = BeautifulSoup(htmltext,"html.parser")

    while True:
        try:
            target = soup.find("div", class_= "SongHeaderdesktop__CoverArtContainer-sc-1effuo1-6 jLdecJ")
            for c in target.children:
                if c != "\n":
                    images = soup.findAll("img")[1]
                    imglink = images.get("src")
                    img_data = requests.get(imglink).content  
                    with open("album.png", "wb") as handler:
                        handler.write(img_data)
                    IMAGE_PATH = 'album.png'

                    cover = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH)), size=(IMAGE_WIDTH , IMAGE_HEIGHT))
                    label = customtkinter.CTkLabel(master=app, image=cover, text='')
                    label.place(relx=0.5, rely=0.3, anchor="center")

                    
                    label = customtkinter.CTkLabel(app, text=f"Playing: {SongName} by {ArtistName}", fg_color="transparent")
                    label.place(relx=0.5, rely=0.46, anchor="center")
                     
                    LyricTarget = soup.find("div", class_= "Lyrics__Container-sc-1ynbvzw-1 kUgSbL")
                    for c in LyricTarget.children:
                        #print(c)

                        c = str(c)

                        for line in c.split("\n"):
                            remove = soup.find("href", class_= "ReferentFragmentdesktop__ClickTarget-sc-110r0d9-0 cehZkS")
                            line = line.replace("<br/>"," ")
                            print(line)   


                            textbox = customtkinter.CTkTextbox(app)
                            textbox.place(relx=0.2, rely=0.2)
                            textbox.insert("0.0", line)  # insert at line 0 character 0
                            textbox.configure(state="normal")  # configure textbox to be read-only





            break
        except :
            IMAGE_PATH = 'ERROR.png'
            error = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH)), size=(IMAGE_WIDTH , IMAGE_HEIGHT))
            label = customtkinter.CTkLabel(master=app, image=error, text='')
            label.place(relx=0.5, rely=0.3, anchor="center")

            print("error")
            break
 




IMAGE_WIDTH = 300
IMAGE_HEIGHT = 300
IMAGE_PATH = 'bob.png'

your_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH)), size=(IMAGE_WIDTH , IMAGE_HEIGHT))
label = customtkinter.CTkLabel(master=app, image=your_image, text='')
label.place(relx=0.5, rely=0.3, anchor="center")

entryArtist = CTkEntry(master=app, placeholder_text="Enter artist name")
entrySong = CTkEntry(master=app, placeholder_text="Enter Song name")
btn = CTkButton(master=app, text="Submit", command=click_handler)

entryArtist.place(relx=0.5, rely=0.5, anchor="center") 
entrySong.place(relx=0.5, rely=0.6, anchor="center")
btn.place(relx=0.5, rely=0.7, anchor="center") 
#https://github.com/RoyChng/customtkinter-tutorial/tree/master
#https://www.youtube.com/watch?v=Miydkti_QVE
app.mainloop()