import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from tkinter import *
import numpy as np
import csv 
from tkinter import *

global gender_var, mood_var, weather_var, occasion_var
global clothlist

clothlist=[] 
def get_outfit_suggestion():
    df = pd.read_csv(r'D:\21CS028_django\general_miniproject\dataset.csv')

    # Convert categorical variables to numerical
    df = pd.get_dummies(df, columns=['Gender', 'Mood', 'Weather', 'Occasion'])

    # Split the dataset into features and target variable
    X = df.drop('Output', axis=1)
    y = df['Output']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model
    model = RandomForestClassifier(n_estimators=100)
    
    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')
    
    if not gender_var.get() or not mood_var.get() or not weather_var.get() or not occasion_var.get():
        messagebox.showerror("Error", "Please select an option for all categories.")
        return
    
    user_input = pd.DataFrame({
        'Gender': [gender_var.get()],
        'Mood': [mood_var.get()],
        'Weather': [weather_var.get()],
        'Occasion': [occasion_var.get()]
    })
    
    # Convert user input to match the model's training format
    user_input = pd.get_dummies(user_input, columns=['Gender', 'Mood', 'Weather', 'Occasion'])
    user_input = user_input.reindex(columns=X.columns, fill_value=0)
    
    # Make prediction
    prediction = model.predict(user_input)
    
    # Display the prediction
    messagebox.showinfo("Outfit Suggestion", f'Outfit Suggestion: {prediction[0]}')


def wardrobe(clist):
    df = pd.read_csv(r'dataset.csv')
    slnolist,genderlist,weatherlist,moodlist,occlist,oplist=[],[],[],[],[],[]
    for i in clist:
        rows=df.loc[df['Output'] == i]
        print(rows)
        rowarray=np.array(rows)
        
        for j in range(len(rowarray)):
            slnolist.append(rowarray[j,0])
            genderlist.append(rowarray[j,1])
            weatherlist.append(rowarray[j,2])
            moodlist.append(rowarray[j,3])
            occlist.append(rowarray[j,4])
            oplist.append(rowarray[j,5])
        
    
    dict = {'slno': slnolist, 'Gender': genderlist, 'Mood':moodlist,'Weather':weatherlist,'Occasion':occlist,'Output':oplist}
    df1 = pd.DataFrame(dict)
    df1.to_csv(r'updated-file.csv', sep=',', index=False, encoding='utf-8')
    newdf=pd.read_csv(r'updated-file.csv')
    # Convert categorical variables to numerical
    newdf = pd.get_dummies(newdf, columns=['Gender', 'Mood', 'Weather', 'Occasion'])

    # Split the dataset into features and target variable
    X = newdf.drop('Output', axis=1)
    y = newdf['Output']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)

    # Initialize the model
    model =RandomForestClassifier(n_estimators = 100) 
    # Train the model
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')
    
    if not gender_var.get() or not mood_var.get() or not weather_var.get() or not occasion_var.get():
        messagebox.showerror("Error", "Please select an option for all categories.")
        return
    
    user_input = pd.DataFrame({
        'Gender': [gender_var.get()],
        'Mood': [mood_var.get()],
        'Weather': [weather_var.get()],
        'Occasion': [occasion_var.get()]
    })
    
    # Convert user input to match the model's training format
    user_input = pd.get_dummies(user_input, columns=['Gender', 'Mood', 'Weather', 'Occasion'])
    user_input = user_input.reindex(columns=X.columns, fill_value=0)
    
    # Make prediction
    prediction = model.predict(user_input)
    
    # Display the prediction
    messagebox.showinfo("Outfit Suggestion", f'Outfit Suggestion: {prediction[0]}')
    
    
    f = open(r'updated-file.csv', "w")
    f.truncate()
    f.close()
    




def create():
    root = Tk()
    root.title('Outfit Recommendation System')
    root.geometry('925x500+300+170')
    root.configure(bg='lavender')
    root.resizable(False, False)

    lbltitle = Label(root, bd=0, relief=GROOVE, text="OUTFIT RECOMMENDATION SYSTEM", fg="brown", bg="white", font=("times new roman", 30, "bold"))
    lbltitle.pack(side=TOP, fill=BOTH, padx=20, pady=10)

    img = PhotoImage(file='bbb.png')
    Label(root, image=img, bg='white', width=420, height=440).place(x=1, y=60)



    frame = Frame(root, width=500, height=370, bg="rosy brown")
    frame.place(x=400, y=90)

    # Create a label for the gender dropdown menu
    global gender_var, mood_var, weather_var, occasion_var
    gender_label = Label(frame, text="Gender:", bg="rosy brown", font=("times new roman", 16, "bold"))
    gender_label.place(x=50, y=20)

    # Create a combobox for gender selection
    gender_options = ["Male", "Female", "Other"]
    gender_var = StringVar()  # Variable to store selected gender
    gender_combobox = ttk.Combobox(frame, values=gender_options, font=("times new roman", 14), state="readonly", textvariable=gender_var)
    gender_combobox.place(x=200, y=20)
    gender_combobox.set("Select Gender")  # Set the default value

    # Create a label for the mood dropdown menu
    mood_label = Label(frame, text="Mood:", bg="rosy brown", font=("times new roman", 16, "bold"))
    mood_label.place(x=50, y=75)

    # Create a combobox for mood selection
    mood_options = ["Excited", "Mellow", "Droopy", "Sad"]
    mood_var = StringVar()  # Variable to store selected mood
    mood_combobox = ttk.Combobox(frame, values=mood_options, font=("times new roman", 14), state="readonly", textvariable=mood_var)
    mood_combobox.place(x=200, y=75)
    mood_combobox.set("Select Mood")  # Set the default value

    # Create a label for the weather dropdown menu
    weather_label = Label(frame, text="Weather:", bg="rosy brown", font=("times new roman", 16, "bold"))
    weather_label.place(x=50, y=130)

    # Create a combobox for weather selection
    weather_options = ["Sunny", "Cloudy", "Rainy", "Cool"]
    weather_var = StringVar()  # Variable to store selected weather
    weather_combobox = ttk.Combobox(frame, values=weather_options, font=("times new roman", 14), state="readonly", textvariable=weather_var)
    weather_combobox.place(x=200, y=130)
    weather_combobox.set("Select Weather")  # Set the default value

    # Create a label for the occasion dropdown menu
    occasion_label = Label(frame, text="Occasion:", bg="rosy brown", font=("times new roman", 16, "bold"))
    occasion_label.place(x=50, y=185)

    # Create a combobox for occasion selection
    occasion_options = ["Formal", "Party", "Casual", "Ethnic"]
    occasion_var = StringVar()  # Variable to store selected occasion
    occasion_combobox = ttk.Combobox(frame, values=occasion_options, font=("times new roman", 14), state="readonly", textvariable=occasion_var)
    occasion_combobox.place(x=200, y=185)
    occasion_combobox.set("Select Occasion")  # Set the default value

    # Add a button to get outfit suggestions
    suggestion_button = Button(frame, text="Get Outfit Suggestion", bg="gainsboro", font=("times new roman", 14, "bold"), command=get_outfit_suggestion)
    suggestion_button.place(x=285, y=245)

    # Function to open a new window

    
    def open_wardrobe_window():
        new_window = Toplevel(root)
        new_window.title("Create Wardrobe")
        new_window.geometry('950x600+300+100')
        new_window.configure(bg='lavender')
        new_window.resizable(False, False)

        wltitle = Label(new_window, bd=0, relief=GROOVE, text="CREATE WARDROBE", fg="brown", bg="white", font=("times new roman", 24, "bold"))
        wltitle.pack(side=TOP, fill=BOTH, padx=20, pady=10)

    # Frame for canvas and scrollbar
        canvas_frame = Frame(new_window, bg="lavender")
        canvas_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    # Create a canvas
        canvas = Canvas(canvas_frame, bg="rosy brown")
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Add a scrollbar
        scrollbar = Scrollbar(canvas_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas
        wframe = Frame(canvas, width=500, height=700, bg="rosy brown")
        canvas.create_window((0, 0), window=wframe, anchor=NW)

        df = pd.read_csv(r'dataset.csv', skipinitialspace=True)
        unique_outputs = df['Output'].unique()

        def add_list():
            for i, cloth_var in enumerate(cloth_vars):
                if cloth_var.get() != 0:
                    clothlist.append(unique_outputs[i])
            new_window.destroy()

        cloth_vars = [tk.IntVar(value=0) for _ in unique_outputs]

        for i, output in enumerate(unique_outputs):
            tk.Checkbutton(wframe, text=output, variable=cloth_vars[i], bg="rosy brown", font=("times new roman", 12)).grid(row=i, column=0, sticky=W, padx=10, pady=5)

        add_button = Button(new_window, text="ADD", fg="brown", bg="lavender blush", font=("times new roman", 16, "bold"), command=add_list)
        add_button.pack(pady=10)

    # Configure the canvas scroll region
        wframe.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))


    def list_display():
        disp_window = Toplevel(root)
        disp_window.title("My Wardrobe")
        disp_window.geometry("500x500+600+200")
        disp_window.configure(bg='lavender blush')
        disp_window.resizable(False, False)
        
        mwltitle = Label(disp_window, bd=0, relief=GROOVE, text="MY WARDROBE", fg="brown", bg="white", font=("times new roman", 24, "bold"))
        mwltitle.pack(side=TOP, fill=BOTH, padx=20, pady=10)

        
        
        listbox = Listbox(disp_window, height=20)
        for i, item in enumerate(clothlist):
            listbox.insert(i, item)
        listbox.pack(side=TOP,fill=BOTH, padx=20, pady=10)    

        close_button = Button(disp_window, text="Close", bg="lavender", font=("times new roman", 14, "bold"), command=disp_window.destroy)
        close_button.place(x=220,y=430)
    

        # Add a button to create wardrobe
    create_wardrobe_button = Button(frame, text="   Create Wardrobe   ", bg="gainsboro", font=("times new roman", 14, "bold"), command=open_wardrobe_window)
    create_wardrobe_button.place(x=285, y=310)


    display_button = Button(frame, text=" Display my wardrobe ", bg="gainsboro", font=("times new roman", 14, "bold"), command=list_display)
    display_button.place(x=30, y=310)


    get_wardrobe_button = Button(frame, text="Suggestion from My Wardrobe", bg="gainsboro", font=("times new roman", 14, "bold"), command=lambda:wardrobe(clothlist))
    get_wardrobe_button.place(x=10, y=245)
            

    root.mainloop()

create()