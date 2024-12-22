import csv
import matplotlib.pyplot as plt
import tkinter as tk
import os


def main():
    new_window = tk.Tk()
    new_window.title("Functions")
    new_window.geometry("400x400")
    tk.Label(new_window, text="\n\tWelcome to the European Soccer Game Data Analysis Program.\nWhat do you want to do?\n").pack()

    tk.Button(new_window, text="Create a New File", command=New_File).pack()
    tk.Button(new_window, text="Read an Existing File", command=Read_File).pack()
    tk.Button(new_window, text="Append to an Existing File", command=Append_File).pack()
    tk.Button(new_window, text="Search for a Record in a File", command=Search_File).pack()
    tk.Button(new_window, text="Modify a Record in a File", command=Modify_File).pack()
    tk.Button(new_window, text="Plot Graph for Comparison", command=Graph_File).pack()
    tk.Button(new_window, text="Delete a File", command=Delete_File).pack()
    tk.Button(new_window, text="EXIT", command=new_window.destroy).pack()

    new_window.mainloop()


def Content():
    new_window_1 = tk.Tk()
    new_window_1.title("New Record!")
    new_window_1.geometry("400x400")

    def save_text():
        with open("Soccer.csv", 'a', newline='') as fin:
            w = csv.writer(fin)
            t1 = tb1.get()
            t2 = tb2.get()
            t3 = tb3.get()
            t4 = tb4.get()
            w.writerow([t1, t2, t3, t4])
        tk.Label(new_window_1, text="Contents Added! Do you want to enter more?").pack()

    def input_fields():
        global tb1, tb2, tb3, tb4
        tk.Label(new_window_1, text="Enter the country name of the team").pack()
        tb1 = tk.Entry(new_window_1)
        tb1.pack()
        tk.Label(new_window_1, text="Enter the matches won by that team").pack()
        tb2 = tk.Entry(new_window_1)
        tb2.pack()
        tk.Label(new_window_1, text="Enter player name").pack()
        tb3 = tk.Entry(new_window_1)
        tb3.pack()
        tk.Label(new_window_1, text="Enter goals scored by that player").pack()
        tb4 = tk.Entry(new_window_1)
        tb4.pack()
        tk.Button(new_window_1, text="Save to Soccer.csv", command=save_text).pack(pady=10)

    input_fields()


def New_File():
    with open("Soccer.csv", 'w', newline='') as fin:
        w = csv.writer(fin)
        w.writerow(["Country Name", "Matches Won", "Player Name", "Goals Scored by the Player"])
    Content()


def Read_File():
    data = []

    def open_file():
        with open("Soccer.csv", 'r', newline='') as fin:
            r = csv.reader(fin)
            for i in r:
                data.append(i)

    open_file()
    new_window_1 = tk.Tk()
    new_window_1.title("File Reader")
    text = tk.Text(new_window_1, width=70, height=20)
    text.pack()
    for i in data:
        text.insert("end", ",\t".join(i) + "\n")


def Append_File():
    Content()


def Search_File():
    def search():
        pname = search_entry.get()
        with open("Soccer.csv", 'r', newline='') as fin:
            r = csv.reader(fin)
            for i in r:
                if i[2].lower() == pname.lower():
                    result_text.insert("end", "\t".join(i) + "\n")
                    return
            result_text.insert("end", "No such record found!\n")

    new_window_1 = tk.Tk()
    new_window_1.title("Search Record")
    tk.Label(new_window_1, text="Enter player name whose record you wish to search:").pack()
    search_entry = tk.Entry(new_window_1)
    search_entry.pack()
    tk.Button(new_window_1, text="Search", command=search).pack()
    result_text = tk.Text(new_window_1, width=90, height=30)
    result_text.pack()


def Modify_File():
    def modify():
        pname = modify_entry.get()
        modified = False
        newrows = []
        with open("Soccer.csv", 'r', newline='') as fin:
            data = list(csv.reader(fin))
            for row in data:
                if row[2].strip().lower() == pname.lower():
                    row = [tb1.get(), tb2.get(), tb3.get(), tb4.get()]
                    modified = True
                newrows.append(row)
        with open("Soccer.csv", 'w', newline='') as fout:
            w = csv.writer(fout)
            w.writerows(newrows)
        if modified:
            result_text.insert("end", "Record updated.\n")
        else:
            result_text.insert("end", "No such record found!\n")

    def input_fields():
        global tb1, tb2, tb3, tb4
        tk.Label(new_window_1, text="Enter the country name of the team").pack()
        tb1 = tk.Entry(new_window_1)
        tb1.pack()
        tk.Label(new_window_1, text="Enter the matches won by that team").pack()
        tb2 = tk.Entry(new_window_1)
        tb2.pack()
        tk.Label(new_window_1, text="Enter player name").pack()
        tb3 = tk.Entry(new_window_1)
        tb3.pack()
        tk.Label(new_window_1, text="Enter goals scored by that player").pack()
        tb4 = tk.Entry(new_window_1)
        tb4.pack()
        tk.Button(new_window_1, text="Modify Record", command=modify).pack()

    new_window_1 = tk.Tk()
    new_window_1.title("Modify Record")
    tk.Label(new_window_1, text="Enter player name whose record you wish to modify:").pack()
    modify_entry = tk.Entry(new_window_1)
    modify_entry.pack()
    tk.Button(new_window_1, text="Next", command=input_fields).pack()
    result_text = tk.Text(new_window_1, width=80, height=10)
    result_text.pack()


def Delete_File():
    def delete():
        if os.path.exists("Soccer.csv"):
            os.remove("Soccer.csv")

    new_window_1 = tk.Tk()
    tk.Label(new_window_1, text="Warning! You're going to delete the file. Do you want to proceed?\n").pack()
    tk.Button(new_window_1, text="YES", command=lambda: [delete(), new_window_1.destroy()]).pack()
    tk.Button(new_window_1, text="NO", command=new_window_1.destroy).pack()


def Graph_File():
    data = []
    with open("Soccer.csv", 'r', newline='') as fin:
        r = csv.reader(fin)
        for i in r:
            data.append(i)

    def team_graph():
        x, y = [], []
        for i in data[1:]:
            x.append(i[0])
            y.append(int(i[1]))
        plt.bar(x, y, label="Matches Won")
        plt.title("Team VS Matches Won")
        plt.xlabel("Country")
        plt.ylabel("Matches Won")
        plt.legend()
        plt.show()

    def player_graph():
        x, y = [], []
        for i in data[1:]:
            x.append(i[2])
            y.append(int(i[3]))
        plt.bar(x, y, label="Goals Scored")
        plt.title("Player VS Goals Scored")
        plt.xlabel("Player")
        plt.ylabel("Goals Scored")
        plt.legend()
        plt.show()

    new_window_1 = tk.Tk()
    new_window_1.geometry("400x400")
    tk.Label(new_window_1, text="Select one of the following").pack()
    tk.Button(new_window_1, text="Plot graph between Team and Matches Won", command=team_graph).pack(pady=20)
    tk.Button(new_window_1, text="Plot graph between Player and Goals Scored", command=player_graph).pack()


main()
