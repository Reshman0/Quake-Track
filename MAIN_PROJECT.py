import pandas as pd
import csv
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO
from datetime import datetime
from sys import exit

def main_menu():
    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.title("EARTHQUAKE REPORTING SYSTEM")  
    title_label = tk.Label(window, text="QUAKE TRACK", font=("Courier", 35, "bold"), bg="light gray",fg="black")
    title_label.pack(pady=250)

    options_frame = tk.Frame(window)
    options_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
  
    admin_btn = tk.Button(options_frame, text="View System Data", command=admin_check, width=30, height=2, bg="light yellow")
    admin_btn.pack(pady=5)

    report_btn = tk.Button(options_frame, text="Make a Report", command=user_menu, width=30, height=2, bg="light yellow")
    report_btn.pack(pady=5)

    view_btn = tk.Button(options_frame, text="View Recent Earthquakes", command=recent_earthquakes, width=30, height=2, bg="light yellow")
    view_btn.pack(pady=5)
    
    button = tk.Button(options_frame, text="Exit", command=exit, width=20, height=2,bg="red")
    button.pack(pady=5)

  
    window.mainloop()

#User Menu Functions  
def user_menu():
    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.title("User Menu")

    title_label = tk.Label(window, text="Select an option:", font=("Arial", 25, "bold"),bg="light gray",fg="black")
    title_label.pack(pady=250)

    options_frame = tk.Frame(window)
    options_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    button1 = tk.Button(options_frame, text="I am trapped under rubble", command=under_rubble, width=30, height=2,bg="light blue")
    button1.pack(pady=5)

    button2 = tk.Button(options_frame, text="I will report a debris", command=reporting_debris, width=30, height=2,bg="light blue")
    button2.pack(pady=5)

    button3 = tk.Button(options_frame, text="I need supplies", command=supplies, width=30, height=2,bg="light blue")
    button3.pack(pady=5)
    
    button4 = tk.Button(options_frame, text="Return Main Menu", command=main_menu, width=20, height=2,bg="crimson")
    button4.pack(pady=5)

    window.mainloop()

def under_rubble():
    def submit_report():
        global health_condition

        province = (province_entry.get()).capitalize()
        district = (district_entry.get()).capitalize()
        street_name = (street_entry.get()).capitalize()
        apartment_name = (apartment_entry.get()).capitalize()
        health_condition = health_condition_combo.get()

        if (apartment_name in pd.read_csv("DebrisReport.csv")["APARTMENT NAME"].tolist()) and (province in pd.read_csv("DebrisReport.csv")["PROVINCE"].tolist()) and (district in pd.read_csv("DebrisReport.csv")["DISTRICT"].tolist()) and (street_name in pd.read_csv("DebrisReport.csv")["STREET NAME"].tolist()):
            result_label.config(text="A report has already been made for this apartment.")
        else:
            report = [province, district, street_name, apartment_name, health_condition, "NO HELP YET"]
            with open("DebrisReport.csv", "a", newline='', encoding='utf-8') as ea:
                writer = csv.writer(ea)
                writer.writerow(report)
            result_label.config(text="REPORT SUBMITTED")

    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.title("I am trapped under rubble")

    province_label = tk.Label(window, text="Province:", font=("Arial", 12))
    province_label.pack(pady=10)

    province_entry = tk.Entry(window, width=30)
    province_entry.pack()

    district_label = tk.Label(window, text="District:", font=("Arial", 12))
    district_label.pack(pady=10)

    district_entry = tk.Entry(window, width=30)
    district_entry.pack()

    street_label = tk.Label(window, text="Street Name:", font=("Arial", 12))
    street_label.pack(pady=10)

    street_entry = tk.Entry(window, width=30)
    street_entry.pack()

    apartment_label = tk.Label(window, text="Apartment Name:", font=("Arial", 12))
    apartment_label.pack(pady=10)

    apartment_entry = tk.Entry(window, width=30)
    apartment_entry.pack()

    health_condition_label = tk.Label(window, text="Health Condition:", font=("Arial", 12))
    health_condition_label.pack(pady=10)

    health_condition_combo = ttk.Combobox(window, values=["Heavily Injured", "Injured", "No Injuries"], width=30)
    health_condition_combo.pack()

    submit_button = tk.Button(window, text="Submit", command=submit_report, width=15,bg="green")
    submit_button.pack(pady=20)

    button1 = tk.Button(window, text="Return Upper Menu", command=user_menu, width=30, height=2,bg="crimson")
    button1.pack(pady=5)

    result_label = tk.Label(window, text="", font=("Arial", 12))
    result_label.pack()

    window.mainloop()

def reporting_debris():
    def submit_rprt():

        province = (province_entry.get()).capitalize()
        district = (district_entry.get()).capitalize()
        street_name = (street_entry.get()).capitalize()
        apartment_name = (apartment_entry.get()).capitalize()

        
        if (apartment_name in pd.read_csv("DebrisReport.csv")["APARTMENT NAME"].tolist()) and (province in pd.read_csv("DebrisReport.csv")["PROVINCE"].tolist()) and (district in pd.read_csv("DebrisReport.csv")["DISTRICT"].tolist()) and (street_name in pd.read_csv("DebrisReport.csv")["STREET NAME"].tolist()):
            result_label.config(text="A report has already been made for this apartment.")
        else:
            report = [province, district, street_name, apartment_name] + ["Not Under Rubble"] + ["NO HELP YET"]

            with open("DebrisReport.csv", "a", newline='', encoding='utf-8') as eb:
                writer = csv.writer(eb)
                writer.writerow(report)

            result_label.config(text="REPORT SUBMITTED")

    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.title("Report A Debris")

    province_label = tk.Label(window, text="Province:", font=("Arial", 12))
    province_label.pack(pady=10)

    province_entry = tk.Entry(window, width=30)
    province_entry.pack()

    district_label = tk.Label(window, text="District:", font=("Arial", 12))
    district_label.pack(pady=10)

    district_entry = tk.Entry(window, width=30)
    district_entry.pack()

    street_label = tk.Label(window, text="Street Name:", font=("Arial", 12))
    street_label.pack(pady=10)

    street_entry = tk.Entry(window, width=30)
    street_entry.pack()

    apartment_label = tk.Label(window, text="Apartment Name:", font=("Arial", 12))
    apartment_label.pack(pady=10)

    apartment_entry = tk.Entry(window, width=30)
    apartment_entry.pack()

    submit_button = tk.Button(window, text="Submit", command=submit_rprt, width=15,bg="green")
    submit_button.pack(pady=20)

    button1 = tk.Button(window, text="Return Upper Menu", command=user_menu, width=30, height=2, bg="red")
    button1.pack(pady=5)

    result_label = tk.Label(window, text="", font=("Arial", 12))
    result_label.pack()

    window.mainloop()

def supplies():
    supplies_list = []

    def add_supply():
        supply = (supply_entry.get()).capitalize()
        if supply:
            supplies_list.append(supply)
            supply_entry.delete(0, tk.END)

    def submit_supply():
        province = (province_entry.get()).capitalize()
        district = (district_entry.get()).capitalize()

        for supply in supplies_list:
            supply_report = [province, district, supply]
            with open("SupplyReport.csv", "a", newline='', encoding='utf-8') as s:
                writer = csv.writer(s)
                writer.writerow(supply_report)

        result_label.config(text="REPORT SUBMITTED")

    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.title("Supply Request")

    province_label = tk.Label(window, text="Province:", font=("Arial", 12))
    province_label.pack(pady=10)

    province_entry = tk.Entry(window, width=30)
    province_entry.pack()

    district_label = tk.Label(window, text="District:", font=("Arial", 12))
    district_label.pack(pady=10)

    district_entry = tk.Entry(window, width=30)
    district_entry.pack()

    supply_label = tk.Label(window, text="Supply:", font=("Arial", 12))
    supply_label.pack(pady=10)

    supply_entry = tk.Entry(window, width=30)
    supply_entry.pack()

    add_button = tk.Button(window, text="Add More Supply +1", command=add_supply, width=17)
    add_button.pack(pady=5)

    submit_button = tk.Button(window, text="Submit", command=submit_supply, width=15,bg="green")
    submit_button.pack(pady=20)

    button1 = tk.Button(window, text="Return Upper Menu", command=user_menu, width=30, height=2,bg="crimson")
    button1.pack(pady=5)

    result_label = tk.Label(window, text="", font=("Arial", 12))
    result_label.pack()

    window.mainloop()

#Admin Menu Functions
def admin_check():
    def login_info():
        username = username_entry.get()
        password = password_entry.get()

        if username == "admin" and password == "admin":
            admin_menu()
        else:
            result_label.config(text="Wrong username or password !")
    

    window= tk.Tk()
    window.title("Authentication")
    window.eval('tk::PlaceWindow . center')
    
    username_label = tk.Label(window, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(window, width=30)
    username_entry.pack()

    password_label = tk.Label(window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(window, width=30, show="*")
    password_entry.pack() 

    submit_button = tk.Button(window, text="Submit", command=login_info,bg="green")
    submit_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()

def admin_menu():
    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.title("Admin Menu")

    title_label = tk.Label(window, text="Select an option:", font=("Arial", 25, "bold"),bg="light gray",fg="black")
    title_label.pack(pady=250)

    options_frame = tk.Frame(window)
    options_frame.place(relx=0.5, rely=0.5, anchor="center")

    button1 = tk.Button(options_frame, text="See Information About Earthquake Reports", command=show_report_table, width=35, height=2,bg="light blue")
    button1.pack(pady=5)

    button2 = tk.Button(options_frame, text="See Information About Supply Requests", command=show_supply_table, width=35, height=2,bg="light blue")
    button2.pack(pady=5)

    button3 = tk.Button(options_frame, text="View General Data Reports", command=report, width=35, height=2,bg="light blue")
    button3.pack(pady=5)

    button4 = tk.Button(options_frame, text="Return To Main Menu", command=main_menu, width=25, height=2,bg="crimson")
    button4.pack(pady=5)

    window.mainloop()
    
def report():
    def show_most_requested_supplies():
        supply_dict = {}
        for supply in pd.read_csv("SupplyReport.csv")["NEEDED SUPPLY"]:
            supply_dict[supply] = supply_dict.get(supply, 0) + 1

        fig.clear()
        plt.barh(list(supply_dict.keys()), list(supply_dict.values()))  
        plt.title("Most Requested Supplies")
        plt.xlabel("COUNT") 
        plt.ylabel("SUPPLY NAME")  #
        canvas.draw()


    def show_report_distribution_by_city():
        province_dict = {}
        for province in pd.read_csv("DebrisReport.csv")["PROVINCE"]:
            province_dict[province] = province_dict.get(province, 0) + 1 

        fig.clear()
        plt.pie(province_dict.values(), labels=province_dict.keys(), autopct="%1.1f%%")
        plt.title("Report Distribution By City")
        canvas.draw()

    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.title("Report Menu")

    label = tk.Label(window, text="Select a report option:", font=("Arial", 20, "bold"),bg="light gray",fg="black")
    label.pack(pady=10)

    button_frame = tk.Frame(window)
    button_frame.pack()

    button1 = tk.Button(button_frame, text="View Most Requested Supplies", command=show_most_requested_supplies, width=30, height=2, bg="blue", fg="white")
    button1.pack(side=tk.LEFT, padx=5)

    button2 = tk.Button(button_frame, text="View Report Distribution By City", command=show_report_distribution_by_city, width=30, height=2, bg="green", fg="white")
    button2.pack(side=tk.LEFT, padx=5)

    fig = plt.figure(figsize=(10, 6))
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().pack()

    return_button = tk.Button(window, text="Return to Upper Menu", command=admin_menu, width=30, height=2, bg="crimson")
    return_button.pack(pady=10)

    window.mainloop()

def show_report_table():
    dict_of_file = pd.read_csv("DebrisReport.csv").to_dict("list")
    list_of_status = dict_of_file["REPORT STATUS"]

    for i in range(len(list_of_status)):
        if list_of_status[i] != "HELP ARRIVED":
            list_of_status[i] = random.choice(["HELP ARRIVED","NO HELP YET","NO HELP YET","NO HELP YET"])  # increasing the probability of "No Help Yet" to make the program more realistic

    dict_of_file["REPORT STATUS"] = list_of_status
    pd.DataFrame.from_dict(dict_of_file).to_csv("DebrisReport.csv", index=False)

    def show_in_map():
        selected_item = treeview.focus()
        if selected_item:
            item_text = treeview.item(selected_item)["values"]
            location = f"{item_text[0]}, {item_text[1]}" 
            show_map(location)

    def show_map(location):
        api_key = "AIzaSyDZVEC3l5lA53c2JyVdEYmziytllm8f-s4" 
        url = f"https://maps.googleapis.com/maps/api/staticmap?center={location}&zoom=13&size=400x300&markers=color:red%7C{location}&key={api_key}"
        
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        map_image = ImageTk.PhotoImage(image)
        label.configure(image=map_image)
        label.image = map_image

    def on_item_select(event):
        selected_item = treeview.focus()
        if selected_item:
            button.config(state=tk.NORMAL)

    window = tk.Toplevel()
    window.attributes("-fullscreen", True)
    window.title("Earthquake Report Data")

    treeview = ttk.Treeview(window)
    treeview.pack(fill="both", expand=True)

    data = pd.read_csv("DebrisReport.csv")

    treeview["columns"] = list(data.columns)
    treeview.heading("#0", text="Index", anchor="w")

    for column in data.columns:
        treeview.heading(column, text=column, anchor="w")

    index = 1
    for _, row in data.iterrows():
        values = row.values.tolist()
        treeview.insert("", "end", text=index, values=values)
        index += 1

    treeview.bind("<<TreeviewSelect>>", on_item_select)
    
    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    button = tk.Button(button_frame, text="Show in Map", command=show_in_map, state=tk.DISABLED, width=50, height=2, bg="yellow", fg="black")
    button.pack(pady=5)

    return_button = tk.Button(button_frame, text="Return to Upper Menu", command=admin_menu, width=30, height=2)
    return_button.pack()

    label = tk.Label(window, text="")
    label.pack()

    window.mainloop()

def show_supply_table():
    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.title("Supply Report Data")

    treeview = ttk.Treeview(window)
    treeview.pack(fill="both", expand=True)

    data = pd.read_csv("SupplyReport.csv")

    treeview["columns"] = list(data.columns)
    treeview.heading("#0", text="Index", anchor="w") 

    button = tk.Button(window, text="Return To Upper Menu", command=admin_menu, width=30, height=2, bg="crimson")
    button.pack(pady=5) 

    for column in data.columns:
        treeview.heading(column, text=column, anchor="w")

    index = 1
    for _, row in data.iterrows():
        values = row.values.tolist()
        treeview.insert("", "end", text=index, values=values)
        index += 1

    window.mainloop()
#------------------------#
earthquake_data = [] 
def recent_earthquakes():

    def fetch_earthquake_data():
        global earthquake_data

        url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
        infos = {
            "format": "geojson",
            "minmagnitude": "2.5",
            "limit": "5",
            "minlatitude": "36.0",
            "maxlatitude": "42.0",
            "minlongitude": "26.0",
            "maxlongitude": "45.0"
        }

        response = requests.get(url, params=infos)
        data = response.json()

        for veri in data["features"]:
            place = "PLACE: " + str(veri["properties"]["place"])
            magnitude = "MAGNITUDE: " + str(veri["properties"]["mag"])
            time_str = "TIME: " + str(datetime.fromtimestamp(veri["properties"]["time"] / 1000.0))

            earthquake_data.append(place + "\n" + magnitude + "\n" + time_str + "\n\n")

        
        data_text.delete('1.0', tk.END)

        
        for data in earthquake_data:
            data_text.insert(tk.END, data)

    
        data_text.tag_configure("center", justify="center")
        data_text.tag_add("center", "1.0", "end")


    window = tk.Tk()
    window.attributes("-fullscreen", True)
    window.title("Real-Time Earthquake Data")

    data_text = tk.Text(window, font=("Courier New", 12))
    data_text.pack(fill=tk.BOTH, expand=True)

    fetch_button = tk.Button(window, text="Get Real-Time Data", command=fetch_earthquake_data, bg="#4caf50", fg="white", width=20, height=2)
    fetch_button.pack(pady=5)

    button = tk.Button(window, text="Return To Main Menu", command=main_menu, width=30, height=2, bg="crimson")
    button.pack(pady=10) 
    
    for data in earthquake_data:
        data_text.insert(tk.END, data)

    data_text.tag_configure("center", justify="center")
    data_text.tag_add("center", "1.0", "end")

    window.mainloop()


#initialize the files
with open('DebrisReport.csv','w', newline='',encoding='utf-8') as file2:
    debris_data = [
    ["PROVINCE", "DISTRICT", "STREET NAME", "APARTMENT NAME", "HEALTH CONDITION", "REPORT STATUS"],
    ["Kahramanmaraş", "Elbistan", "Lale", "Gül", "Heavily Injured", "NO HELP YET"],
    ["Hatay", "İskenderun", "Karanfil ", "Cennet", "Injured", "NO HELP YET"],
    ["Gaziantep", "Karkamış", "Adalet", "Nesil", "Heavily Injured", "NO HELP YET"],
    ["Malatya", "Darende", "Yıldırım", "Şeref", "Injured", "NO HELP YET"],
    ["Diyarbakır", "Sur", "Deniz", "Zafer", "Injured", "NO HELP YET"],
    ["Şanlıurfa", "Harran", "Özgürlük", "Doğuş", "Injured", "NO HELP YET"],
    ["Adıyaman", "Gölbaşı", "Street 659", "Güneş", "No Injuries", "NO HELP YET"],
    ["Osmaniye", "Kadirli", "Uğur", "Şahin", "Heavily Injured", "NO HELP YET"],
    ["Adana", "Ceyhan", "Pınar", "Çınar", "Heavily Injured", "NO HELP YET"],
    ["Malatya", "Arguvan", "İstiklal", "Hayat", "Injured", "NO HELP YET"],
    ["Diyarbakır", "Bismil", "Kavaklık", "Emek", "No Injuries", "NO HELP YET"],
    ["Kilis", "Mazidağı", "Şehitler", "Huzur", "Injured", "NO HELP YET"],
    ["Şanlıurfa", "Harran", "Kepez", "Gönül", "Heavily Injured", "NO HELP YET"],
    ["Adıyaman", "Samsat", "Çınarlı", "Gözde", "No Injuries", "NO HELP YET"],
    ["Osmaniye", "Kadirli", "Esenler", "Işık", "Heavily Injured", "NO HELP YET"],
    ["Adana", "Kozan", "Sultanahmet", "Deniz", "Heavily Injured", "NO HELP YET"],
    ["Kahramanmaraş", "Pazarcık", "Göksu", "Nazar", "Injured", "NO HELP YET"],
    ["Hatay", "Dörtyol", "Şelale", "Gündoğan", "No Injuries", "NO HELP YET"]]
    writer = csv.writer(file2)
    writer.writerows(debris_data)

with open('SupplyReport.csv','w', newline='',encoding='utf-8') as file1:
    supply_data = [
    ['PROVINCE', 'DISTRICT', 'NEEDED SUPPLY'],
    ['Hatay', 'Dörtyol', 'Food'],
    ['Kahramanmaraş', 'Göksun', 'Clothes'],
    ['Osmaniye', 'Kadirli', 'Water'],
    ['Adıyaman', 'Merkez', 'Tent'],
    ['Adana', 'Merkez', 'Medicine'],
    ['Gaziantep', 'Araban', 'Food'],
    ['Şanlıurfa', 'Bozova', 'Food'],
    ['Diyarbakır', 'Bismil', 'Medicine'],
    ['Malatya', 'Yeşilyurt', 'Water'],
    ['Hatay', 'İskenderun', 'Tent'],
    ['Kahramanmaraş', 'Pazarcık', 'Tent'],
    ['Osmaniye', 'Düziçi', 'Water'],
    ['Adıyaman', 'Samsat', 'Food'],
    ['Adana', 'Ceyhan', 'Clothes'],
    ['Kilis', 'Merkez', 'Clothes']]
    writer = csv.writer(file1)
    writer.writerows(supply_data)

main_menu()
        
