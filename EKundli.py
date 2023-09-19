import json
import tkinter
import platform
import appGUI.dataGUI


if __name__ == "__main__":
    root = tkinter.Tk()
    mframe = tkinter.Frame(root)
    root.title("EKundli")
    root.resizable(width=False, height=False)
    root.geometry("700x500")
    if platform.system().lower() == "windows":
        root.iconbitmap("kundli-icon.ico")
    image_pos = None
    with open("img_pos.json", "r") as opn:
        image_pos = json.load(opn)

    app_gui = appGUI.dataGUI.App(mframe, root, image_pos, "Kundli-Design.png")
    
    app_gui.app_entry.ent_name.place(x=100, y=25)
    app_gui.app_entry.ent_year.place(x=100, y=60)
    # app_gui.app_entry.ent_month.place(x=100, y=100)
    app_gui.app_dropdownlist.droplist_months.place(x=100, y=100)
    app_gui.app_dropdownlist.droplist_months.current(0)
    # app_gui.app_entry.ent_day.place(x=100, y=140)
    app_gui.app_dropdownlist.droplist_days.place(x=100, y=140)
    app_gui.app_dropdownlist.droplist_days.current(0)
    app_gui.app_entry.ent_latitude.place(x=300, y=25)
    app_gui.app_entry.ent_longitude.place(x=300, y=60)
    app_gui.app_entry.ent_utc.place(x=300, y=100)
    # app_gui.app_entry.ent_hour.place(x=300, y=140)
    app_gui.app_dropdownlist.droplist_hour.place(x=300, y=140)
    app_gui.app_dropdownlist.droplist_hour.current(0)
    # app_gui.app_entry.ent_minute.place(x=390, y=140)
    app_gui.app_dropdownlist.droplist_minute.place(x=390, y=140)
    app_gui.app_dropdownlist.droplist_minute.current(0)
    app_gui.app_dropdownlist.ayanamsa.place(x=100, y=170)
    app_gui.app_dropdownlist.ayanamsa.current(1)

    app_gui.app_label.lbl_name.place(x=60, y=25)
    app_gui.app_label.lbl_year.place(x=70, y=60)
    app_gui.app_label.lbl_month.place(x=56, y=100)
    app_gui.app_label.lbl_day.place(x=70, y=140)
    app_gui.app_label.lbl_latitude.place(x=249, y=25)
    app_gui.app_label.lbl_longitude.place(x=236, y=60)
    app_gui.app_label.lbl_utc.place(x=270, y=100)
    app_gui.app_label.lbl_hour.place(x=266, y=140)
    app_gui.app_label.lbl_minute.place(x=343, y=140)
    app_gui.app_label.lbl_ayanamsa.place(x=36, y=170)
    app_gui.app_button.ent_btn_enter.place(x=200, y=200)

    mframe.pack(ipadx=346, ipady=240)
    root.mainloop()
