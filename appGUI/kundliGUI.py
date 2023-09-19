import os
import tkinter
import datetime
from tkinter import filedialog, messagebox
from imgEdit.kundli_Img import EditImg
from PIL import ImageTk, ImageFilter


class AppLabelText:
    def __init__(self, root):
        self.font = 3
        self.font_a = 1
        self.lbl_chart   = tkinter.Label(root, font=(10,))
        self.lbl_asc     = tkinter.Label(root, text="Asc", font=(self.font,))
        self.lbl_sun     = tkinter.Label(root, text="Sun", font=(self.font,))
        self.lbl_moon    = tkinter.Label(root, text="Moon", font=(self.font,))
        self.lbl_mercury = tkinter.Label(root, text="Mercury", font=(self.font,))
        self.lbl_venus   = tkinter.Label(root, text="Venus", font=(self.font,))
        self.lbl_mars    = tkinter.Label(root, text="Mars", font=(self.font,))
        self.lbl_jupiter = tkinter.Label(root, text="Jupiter", font=(self.font,))
        self.lbl_saturn  = tkinter.Label(root, text="Saturn", font=(self.font,))
        self.lbl_rahu    = tkinter.Label(root, text="Rahu", font=(self.font,))
        self.lbl_ketu    = tkinter.Label(root, text="Ketu", font=(self.font,))
        self.lbl_neptune = tkinter.Label(root, text="Neptune", font=(self.font,))
        self.lbl_uranus  = tkinter.Label(root, text="Uranus", font=(self.font,))
        self.lbl_pluto   = tkinter.Label(root, text="Pluto", font=(self.font,))
        
        self.lbl_name        = tkinter.Label(root, text="Name: ", font=(self.font_a,))
        self.lbl_year        = tkinter.Label(root, text="Year: ", font=(self.font_a,))
        self.lbl_month       = tkinter.Label(root, text="Month: ", font=(self.font_a,))
        self.lbl_day         = tkinter.Label(root, text="Day: ", font=(self.font_a,))
        self.lbl_hour        = tkinter.Label(root, text="Hour: ", font=(self.font_a,))
        self.lbl_minute      = tkinter.Label(root, text="Minute: ", font=(self.font_a,))
        self.lbl_latitude    = tkinter.Label(root, text="Latitude: ", font=(self.font_a,))
        self.lbl_longitude   = tkinter.Label(root, text="Longitude: ", font=(self.font_a,))
        self.lbl_utc         = tkinter.Label(root, text="UTC: ", font=(self.font_a,))
    

class KundliGUI:
    def __init__(self, root, birth_chart, navamsa_chart, transit_chart, moon_chart, image_pos, kundli_desgin,
                name, year, month, day, hour, minute, latitude, longitude, utc):
        self.window = tkinter.Toplevel(root)
        self.window.title("Kundli")
        self.window.iconbitmap("kundli-icon.ico")
        self.window.geometry("1080x590")
        self.name      = name
        self.year      = year
        self.month     = month
        self.day       = day
        self.hour      = hour
        self.minute    = minute
        self.latitude  = latitude
        self.longitude = longitude
        self.utc       = utc
        self.kundli_design = kundli_desgin
        self.image_pos     = image_pos 
        self.birth_chart   = birth_chart
        self.navamsa_chart = navamsa_chart
        self.transit_chart = transit_chart
        self.moon_chart    = moon_chart
        self.birth_chart_planet   = {}
        self.transit_chart_planet = {}
        self.lbl_text          = AppLabelText(self.window)
        self.btn_lagna         = tkinter.Button(self.window, text="Lagna Kundli", command=self.lagnaKundli)
        self.btn_transit       = tkinter.Button(self.window, text="Transit Kundli", command=self.transitKundli)
        self.btn_navamsa       = tkinter.Button(self.window, text="Navamsa Kundli", command=self.navamsaKundli)
        self.btn_moon          = tkinter.Button(self.window, text="Moon Kundli", command=self.moonKundli)
        self.btn_save          = tkinter.Button(self.window, text="Save", command=self.saveFiles, width=9, padx=5)
        self.planets_label = {
            "asc":self.lbl_text.lbl_asc, "sun":self.lbl_text.lbl_sun, "moon":self.lbl_text.lbl_moon, "mercury":self.lbl_text.lbl_mercury, "venus":self.lbl_text.lbl_venus, "mars":self.lbl_text.lbl_mars, 
            "jupiter":self.lbl_text.lbl_jupiter,"saturn":self.lbl_text.lbl_saturn, "rahu":self.lbl_text.lbl_rahu, "ketu":self.lbl_text.lbl_ketu, "neptune":self.lbl_text.lbl_neptune, "uranus":self.lbl_text.lbl_uranus,
            "pluto":self.lbl_text.lbl_pluto                      
        }
        self.planets_full_name = {
            "Asc":"Asc", "su":"Sun", "mo":"Moon", "me":"Mercury", "ve":"Venus", "ma":"Mars", "ju":"Jupiter", 
            "sa":"Saturn", "ra":"Rahu", "ke":"Ketu", "ne":"Neptune", "ur":"Uranus", "pl":"Pluto"
        }

        self.get_planet_data(self.birth_chart, 0)
        self.get_planet_data(self.transit_chart, 1)
        self.birth_chart_img   = EditImg().write_to_image(self.birth_chart, self.image_pos, self.kundli_design, 0)
        self.transit_chart_img = EditImg().write_to_image(self.transit_chart, self.image_pos, self.kundli_design, 1)
        self.navamsa_chart_img = EditImg().write_to_image(self.navamsa_chart, self.image_pos, self.kundli_design, 2)
        self.moon_chart_img    = EditImg().write_to_image(self.moon_chart, self.image_pos, self.kundli_design, 1)

        self.lbl_img = tkinter.Label(self.window, width=700, height=500)
        
        self.lbl_text.lbl_chart.configure(text="Lagna Chart")
        self.lbl_text.lbl_chart.place(x=322, y=10)
        self.lbl_text.lbl_asc.place(x=740, y=100)
        self.lbl_text.lbl_sun.place(x=740, y=120)
        self.lbl_text.lbl_moon.place(x=740, y=140)
        self.lbl_text.lbl_mercury.place(x=740, y=160)
        self.lbl_text.lbl_venus.place(x=740, y=180)
        self.lbl_text.lbl_mars.place(x=740, y=200)
        self.lbl_text.lbl_jupiter.place(x=740, y=220)
        self.lbl_text.lbl_saturn.place(x=740, y=240)
        self.lbl_text.lbl_rahu.place(x=740, y=260)
        self.lbl_text.lbl_ketu.place(x=740, y=280)
        self.lbl_text.lbl_neptune.place(x=740, y=300)
        self.lbl_text.lbl_uranus.place(x=740, y=320)
        self.lbl_text.lbl_pluto.place(x=740, y=340)

        self.lbl_text.lbl_name.place(x=740, y=400)
        self.lbl_text.lbl_year.place(x=740, y=420)
        self.lbl_text.lbl_month.place(x=740, y=440)
        self.lbl_text.lbl_day.place(x=740, y=460)

        self.lbl_text.lbl_hour.place(x=740, y=480)
        self.lbl_text.lbl_minute.place(x=806, y=480)
        self.lbl_text.lbl_latitude.place(x=900, y=420)
        self.lbl_text.lbl_longitude.place(x=900, y=440)
        self.lbl_text.lbl_utc.place(x=900, y=462)

        self.lbl_text.lbl_name.configure(text="Name: {0}".format(self.name))
        self.lbl_text.lbl_year.configure(text="Year: {0}".format(self.year))
        self.lbl_text.lbl_month.configure(text="Month: {0}".format(self.month))
        self.lbl_text.lbl_day.configure(text="Day: {0}".format(self.day))
        self.lbl_text.lbl_hour.configure(text="Hour: {0}".format(self.hour))
        self.lbl_text.lbl_minute.configure(text="Minute: {0}".format(self.minute))
        self.lbl_text.lbl_latitude.configure(text="Latitude: {0}".format(self.latitude))
        self.lbl_text.lbl_longitude.configure(text="Longitude: {0}".format(self.longitude))
        self.lbl_text.lbl_utc.configure(text="UTC: +{0}".format(str(self.utc[0])+":"+str(self.utc[1]) if len(self.utc) != 1 else str(self.utc[0]) ))

        self.lbl_img.place(x=10, y=36)
        self.btn_lagna.place(x=740, y=40)
        self.btn_navamsa.place(x=826, y=40)
        self.btn_transit.place(x=926, y=40)
        self.btn_save.place(x=740, y=70)
        self.btn_moon.place(x=826, y=70)
        self.lagnaKundli()
        self.window.mainloop()
    
    def saveFiles(self):
        folder = filedialog.askdirectory(title="Select Folder")
        now_time = datetime.datetime.now().strftime("%H-%M-%S_%Y-%m-%d")
        filename_lagna = "{0}_lagna_{1}.png".format(self.name, now_time) 
        filename_navamsa = "{0}_navamsa_{1}.png".format(self.name, now_time)
        filename_transit = "{0}_transit_{1}.png".format(self.name, now_time)
        filename_moon    = "{0}_moon_{1}.png".format(self.name, now_time)
        self.birth_chart_img.save(os.path.join(folder, filename_lagna))
        self.navamsa_chart_img.save(os.path.join(folder, filename_navamsa))
        self.transit_chart_img.save(os.path.join(folder, filename_transit))
        self.moon_chart_img.save(os.path.join(folder, filename_moon))
        messagebox.showinfo("Files Saved", "Saved to: {0}".format(folder))

    def lagnaKundli(self):
        self.lbl_text.lbl_chart.configure(text="Lagna Chart")
        img = ImageTk.PhotoImage(self.birth_chart_img.filter(ImageFilter.SMOOTH).resize((700,500)))
        self.lbl_img.configure(image=img)
        self.lbl_img.image = img
        for item in self.birth_chart_planet:
            self.planets_label[item.lower()].configure(text="{0} = ".format(item))

        for item in self.birth_chart_planet:
            self.planets_label[item.lower()].configure(text="{0} = {1}".format(item, self.birth_chart_planet[item]))
    
    def navamsaKundli(self):
        self.lbl_text.lbl_chart.configure(text="Navamsa Chart")
        img = ImageTk.PhotoImage(self.navamsa_chart_img.filter(ImageFilter.SMOOTH).resize((700,500)))
        self.lbl_img.configure(image=img)
        self.lbl_img.image = img
        for item in self.birth_chart_planet:
            self.planets_label[item.lower()].configure(text="{0} = ".format(item))

        for item in self.birth_chart_planet:
            self.planets_label[item.lower()].configure(text="{0} = {1}".format(item, self.birth_chart_planet[item]))
        
    def transitKundli(self):
        self.lbl_text.lbl_chart.configure(text="Transit Chart")
        img = ImageTk.PhotoImage(self.transit_chart_img.filter(ImageFilter.SMOOTH).resize((700,500)))
        self.lbl_img.configure(image=img)
        self.lbl_img.image = img
        for item in self.transit_chart_planet:
            self.planets_label[item.lower()].configure(text="{0} = ".format(item))
        
        for item in self.transit_chart_planet:
            self.planets_label[item.lower()].configure(text="{0} = {1}".format(item,self.transit_chart_planet[item]))
    
    def moonKundli(self):
        self.lbl_text.lbl_chart.configure(text="Moon Chart")
        img = ImageTk.PhotoImage(self.moon_chart_img.filter(ImageFilter.SMOOTH).resize((700,500)))
        self.lbl_img.configure(image=img)
        self.lbl_img.image = img
        for item in self.birth_chart_planet:
            self.planets_label[item.lower()].configure(text="{0} = ".format(item))
        
        for item in self.birth_chart_planet:
            self.planets_label[item.lower()].configure(text="{0} = {1}".format(item, self.birth_chart_planet[item]))

    def get_planet_data(self, kundli, mode):
        if mode == 0:
            for house in range(len(kundli)):
                if house == 0 and kundli[house].asc_signlon != 0:
                    self.birth_chart_planet["Asc"] = kundli[house].asc_degree
                
                if len(kundli[house].planets) != 0:
                    for planet in kundli[house].planets:
                        temp = list(planet)
                        temp[0] = temp[0].upper()
                        self.birth_chart_planet["".join(temp)] = kundli[house].planets[planet]["degree"]
        
        if mode == 1:
            for house in range(len(kundli)):
                if kundli[house].is_ascendant:
                    self.transit_chart_planet["Asc"] = kundli[house].asc_degree
                
                if len(kundli[house].planets) != 0:
                    for planet in kundli[house].planets:
                        temp = list(planet)
                        temp[0] = temp[0].upper()
                        self.transit_chart_planet["".join(temp)] = kundli[house].planets[planet]["degree"]
