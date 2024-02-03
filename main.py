import tkinter as tk
# from urllib import request

from PIL import ImageTk, Image

from inputcodes import lines_list
import webbrowser


class VitalsCheck(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.comment = None
        self.title('Check Your Vitals')
        self.commenttext = tk.StringVar()
        self.Nameval = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.Ageval = tk.IntVar()
        self.Heightval = tk.IntVar()
        self.Weightval = tk.IntVar()
        self.BP_level_val = tk.IntVar()
        self.HEART_BEAT = tk.IntVar()
        self.Tops = tk.Frame(self, width=1350, height=50, bd=8, relief="raised")
        self.Tops.pack(side='top')
        self.lbl_T1 = tk.Label(self.Tops, text="HEALTH TRACKING SYSTEM", padx=16, pady=16,
                               bd=16, fg='#000000', font=("Algerian", 48, 'bold'), bg="navajo white",
                               relief='raised', width=28, height=1)
        self.lbl_T1.pack()

        # this is for NAME
        self.x = tk.Label(self, text='Name :', bg="navajo white")
        self.x.pack(padx=15, pady=5)
        self.Name = tk.Entry(self, textvariable=self.Nameval, relief='raised')
        self.Name.pack(padx=15, pady=5)
        self.Nameval.set('xyz')  # default

        # this is for AGE
        self.y = tk.Label(self, text='age :', bg="navajo white")
        self.y.pack(padx=15, pady=5, anchor='center')
        self.Age = tk.Entry(self, textvariable=self.Ageval, relief='raised')
        self.Age.pack(padx=15, pady=5, anchor='center')

        # this is for HEIGHT
        self.p = tk.Label(self, text='Enter the Height in CM :', bg="navajo white")
        self.p.pack(padx=15, pady=5, anchor='center')
        self.Height = tk.Entry(self, textvariable=self.Heightval, relief='raised')
        self.Height.pack(padx=15, pady=5, anchor='center')

        # this is for WEIGHT
        self.q = tk.Label(self, text='Enter Weight in Kg :', bg="navajo white")
        self.q.pack(padx=15, pady=5, anchor='center')
        self.Weight = tk.Entry(self, textvariable=self.Weightval, relief='raised')
        self.Weight.pack(padx=15, pady=5, anchor='center')

        # this is for BP
        self.a = tk.Label(self, text='BP level :', bg="navajo white")
        self.a.pack(padx=15, pady=5, anchor='center')
        self.BP_level = tk.Entry(self, textvariable=self.BP_level_val, relief='raised')
        self.BP_level.pack(padx=15, pady=5, anchor='center')

        # this is for HEARTBEAT
        self.b = tk.Label(self, text='PRESENT HEART BEAT :', bg="navajo white")
        self.b.pack(padx=15, pady=5, anchor='center')
        self.HEARTBEAT_level = tk.Entry(self, textvariable=self.HEART_BEAT, relief='raised')
        self.HEARTBEAT_level.pack(padx=15, pady=5, anchor='center')

        # this is for MALE
        tk.Radiobutton(self, text='Male', variable=self.gender_var, value='Male',
                       bg="navajo white").pack(padx=15, pady=5, anchor='center')

        # this is for FEMALE
        tk.Radiobutton(self, text='Female', variable=self.gender_var, value='Female',
                       bg="navajo white").pack(padx=15, pady=5, anchor='center')

        self.gender_var.set('Male')  # default value

        # this is for SUBMIT ALL DETAILS
        self.submit = tk.Button(self, text='SUBMIT', command=self.submitdetails, bg="navajo white")
        self.submit.pack(padx=15, pady=5, anchor='center')

        # this is for getting BMI
        self.BMI_INDEX = tk.Button(self, text='GET BMI', command=self.BMICALUCLATOR, bg="navajo white")
        self.BMI_INDEX.pack(padx=15, pady=5, anchor='w')

        # this is for checking heart beat by TOPLEVEL
        self.HEARTBEAT_INDEX = tk.Button(self, text='CHECK HEART BEAT LEVELS :',
                                         command=self.HEARTBEATLEVELCALUCLATOR, bg="navajo white")
        self.HEARTBEAT_INDEX.pack(padx=15, pady=5, anchor='w')

        # this is also a TOPLEVEL to get DIET and BP
        self.HEALTH_RECOMMENDER = tk.Button(self, text='HEALTH RECOMMENDER',
                                            command=self.RECOMMENDER, bg="navajo white")

        self.HEALTH_RECOMMENDER.pack(padx=40, pady=10, anchor='w')
        # this is for presenting quote
        self.health = tk.Button(self, text='CLICK ME :-)', command=self.HEALTHQUOTE, bg="navajo white")
        self.health.pack(padx=15, pady=5, anchor='center')

    def submitdetails(self):
        print('DETAILS ARE:')
        print('NAME :', self.Nameval.get())
        print('GENDER :', self.gender_var.get())
        print('AGE :', self.Ageval.get())
        print('Height :', self.Heightval.get())
        print('Weight :', self.Weightval.get())
        print('BP level is :', self.BP_level_val.get())
        print('HEART BEAT is :', self.HEART_BEAT.get())

    def BMICALUCLATOR(self):
        global BMI
        User_Height = self.Heightval.get() / 100
        User_Weight = self.Weightval.get()
        BMI = ((User_Weight) / (User_Height ** 2))
        bmi_label = tk.Label(self, text=f'The BMI index of User is : {BMI}')
        bmi_label.pack()

    def BMIRECOMMENDER(self):
        if BMI < 18.5:
            print("Your BMI is very LOW that means you are in UNDERWEIGHT situation")
            print("Make PROPER DIET with :")
            print('->Eating at least 5 portions of a variety of fruit and vegetables every day.')
            print(
                '->Basing meals on potatoes, bread, rice, pasta or other starchy carbohydrates. ',
                'Choose wholegrain where possible.')
            print('->Choosing unsaturated oils and spreads, such as sunflower or rapeseed, and eating them in',
                  ' small amounts')
            print('->Drinking plenty of fluids. The government recommends 6 to 8 glasses a day.')
            print('->But try not to have drinks just before meals to avoid feeling too full to eat.')
            print("Do EXCERCISES daily...")
        elif 18.5 <= BMI <= 24.9:
            print("->Your BMI is VERYGOOD that means you are in HEALTHY situation")
            print("->Do EXCERCISES daily to keep your BMI healthy...")
        elif 25.0 <= BMI <= 29.9:
            print("Your BMI is HIGH that means you are in OVERWEIGHT situation")
            print(
                "The best way to achieve this is to swap unhealthy and high-energy food choices – such as fast food,",
                " processed food and sugary drinks (including alcohol)")
            print("Make PROPER DIET with :")
            print("->plenty of fruit and vegetables")
            print(
                "->plenty of potatoes, bread, rice, pasta and other starchy foods (ideally you should",
                " choose wholegrain varieties)")
            print("->some meat, fish, eggs, beans and other non-dairy sources of protein")
            print("->just small amounts of food and drinks that are high in fat and sugar")
            print("Do EXCERCISES daily which is very important...")
        else:
            print("Your BMI is HIGH that means you are in OBESE situation")
            print("CONSULT A DOCTOR FOR QUICK REACTION..")
            print("The best way to achieve this is to swap unhealthy and high-energy food choices – such as fast food,",
                  " processed food and sugary drinks (including alcohol)")
            print("Make PROPER DIET with :")
            print("->plenty of fruit and vegetables")
            print("->plenty of potatoes, bread, rice, pasta and other starchy foods ",
                  "(ideally you should choose wholegrain varieties)")
            print("->some meat, fish, eggs, beans and other non-dairy sources of protein")
            print("->just small amounts of food and drinks that are high in fat and sugar")
            print("Do EXCERCISES daily which is very important...")

    def BPLEVELCALUCLATOR(self):
        self.BP_level = self.BP_level_val.get()
        if self.BP_level <= 90:
            self.commenttext = "Your BP level is NOT good that is LOW BLOOD PRESSURE\n" \
                               "->Low blood pressure is less common.\n" \
                               "->Some medicines can cause low blood pressure as a side effect.\n" \
                               "->It can also be caused by a number of underlying conditions, including heart failure" \
                               " and dehydration."
            self.comment.pack()
        elif 90 <= self.BP_level <= 120:
            print("Your BP level is GOOD and HEALTHY")
        else:
            print("Your BP level is NOT good that is HIGH BLOOD PRESSURE")
            print(
                "->High blood pressure is often related to unhealthy lifestyle habits, such as smoking, drinking too",
                " much alcohol, being overweight and not exercising enough.")
            print(
                "->Left untreated, high blood pressure can increase your risk of developing a number of serious ",
                "long-term health conditions, such as coronary heart disease and kidney disease.")

    def HEARTBEATLEVELCALUCLATOR(self):
        global i
        s = tk.Toplevel()
        s.title('HEARTCHECKER')
        i = ImageTk.PhotoImage(Image.open(r"I:\Programmer\Python\HealthTrackerAndRecommenderSystem\HEARTRATECHECK.png"))
        lab = tk.Label(s, image=i)
        lab.pack()

    def HEALTHQUOTE(self):
        global j
        s1 = tk.Toplevel()
        s1.title('HEALTHY LIFE')
        j = ImageTk.PhotoImage(Image.open(r"I:\Programmer\Python\HealthTrackerAndRecommenderSystem\h2.jpg"))
        l1 = tk.Label(s1, image=j)
        l1.pack()

    def RECOMMENDER(self):
        global BMI_INDEX
        global BP_INDEX
        k = tk.Toplevel(self)
        k.config(bg='#358597')
        k.title("HEALTH RECOMMENDER")

        # this is for TOPLEVEL HEADING
        f1 = tk.Frame(k, width=1350, height=500, bd=8, relief="raised")
        f1.pack(side='top')
        lb1_f1 = tk.Label(f1, text=" HEALTH RECOMMENDER SYSTEM", padx=16, pady=16, bd=16, fg='#000000',
                          font=("Bell MT", 48, 'bold'), bg="#FFBFB9", relief='raised', width=28, height=1)
        lb1_f1.pack()

        # this is for Getting DIET as per BMI
        self.BMI_INDEX = tk.Button(k, text='BMI DIET RECOMMENDER', command=self.BMIRECOMMENDER,
                                   bg="navajo white")
        self.comment = tk.Label(k, textvariable=self.commenttext, padx=16, pady=16, bd=16, fg='#222222',
                                font=('Times', 20, 'italic'), bg='#FFBFB1', width=14, height=1)
        self.comment.pack()
        self.BMI_INDEX.pack(padx=15, pady=5, anchor='center')
        # this is for results of entered BP levels
        BP_INDEX = tk.Button(k, text='CHECK BP LEVELS', command=self.BPLEVELCALUCLATOR, bg="navajo white")
        BP_INDEX.pack(padx=15, pady=5, anchor='center')


class ShowDiseases(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('500x500')
        self.title('Possible Diseases')
        disease = tk.StringVar()
        diseasesL = lines_list("symptoms.json", "r", "vv", str(parent.symptom), str(parent.factor))
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.scroll = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.list = tk.Listbox(self.frame, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.list.yview)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.list.insert(0, *diseasesL)
        self.list.pack(side=tk.LEFT)
        self.choose_btn = tk.Button(self.frame, text="Search", command=lambda: (self.choose_disease()))
        self.choose_btn.pack(fill=tk.BOTH)
        self.disease_label = tk.Label(self.frame, textvariable=disease)

    def choose_disease(self):
        index = self.list.curselection()
        ShowDiseases.disease = self.list.get(index)
        self.disease_label.pack()
        urltext = (str(ShowDiseases.disease).strip(" "))
        print(urltext)
        webbrowser.open(f"https://www.google.com/search?q={urltext}")

    def show_treatment(self):
        index = self.list.curselection()
        ShowDiseases.disease = self.list.get(index)
        self.disease_label.pack()
        urltext = (str(ShowDiseases.disease).strip(" "))
        webbrowser.open(f"https://www.google.com/search?q={urltext}")


class DiseaseFinder(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.symptom = tk.StringVar()
        self.factor = tk.StringVar()
        self.disease = tk.StringVar()
        self.geometry('500x500')
        self.title('Find the Disease')

        symptomsL = lines_list("symptoms.json", "r", "k")
        self.frame1 = tk.Frame(self)
        self.frame1.pack()
        self.scroll1 = tk.Scrollbar(self.frame1, orient=tk.VERTICAL)
        self.list1 = tk.Listbox(self.frame1, yscrollcommand=self.scroll1.set)
        self.scroll1.config(command=self.list1.yview)
        self.scroll1.pack(side=tk.LEFT, fill=tk.Y)
        self.list1.insert(0, *symptomsL)
        self.list1.pack(side=tk.LEFT)
        self.choose_btn1 = tk.Button(self.frame1, text="Choose Symptom", command=lambda: (self.choose_symptom(),
                                                                                          self.factor_frame()))
        self.choose_btn1.pack(fill=tk.BOTH)

        self.frame2 = tk.Frame(self)
        self.scroll2 = tk.Scrollbar(self.frame2, orient=tk.VERTICAL)
        self.list2 = tk.Listbox(self.frame2, yscrollcommand=self.scroll2.set)
        self.choose_btn2 = tk.Button(self.frame2, text="Choose Factors", command=lambda: (self.choose_factor(),
                                                                                          self.sd()))

    def choose_symptom(self):
        index = self.list1.curselection()
        self.symptom = self.list1.get(index)
        print(str(self.symptom))
        return self.symptom

    def factor_frame(self):
        factorsL = lines_list("symptoms.json", "r", "vk", str(self.symptom))
        self.frame2.pack()
        self.scroll2.config(command=self.list2.yview)
        self.scroll2.pack(side=tk.LEFT, fill=tk.Y)
        self.list2.insert(0, *factorsL)
        self.list2.pack(side=tk.LEFT)
        self.choose_btn2.pack(fill=tk.BOTH)

    def choose_factor(self):
        index = self.list2.curselection()
        self.factor = self.list2.get(index)
        print(str(self.factor))

    def sd(self):
        sd = ShowDiseases(self)
        sd.grab_set()


class HTRS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('HEALTH TRACKER AND RECOMMENDER SYSTEM')
        self.geometry("700x300")
        self.configure(bg='#b0f4f5')
        self.Tops = tk.Frame(self, width=1350, height=50, bd=8, relief="raised")
        self.Tops.grid(row=0, column=1)
        self.welcome = tk.Label(self.Tops, text="Health Tracker and Recommender System !!!")
        self.welcome.configure(font='Times 20 bold')
        self.symptom: str = ''
        self.findDiseases = tk.Button(self, text='Disease Finder', width=30, command=self.df, pady=30, anchor="center")
        self.checkVitals = tk.Button(self, text='Vitals Check', width=30, command=self.vc, pady=10, anchor="center")
        self.exit = tk.Button(self, text="Quit", width=30, command=self.destroy)
        self.welcome.grid(row=1, column=1, padx=80)
        self.findDiseases.grid(row=2, column=1)
        self.checkVitals.grid(row=3, column=1)
        self.exit.grid(row=4, column=1)

    # df = Disease_Finder
    def df(self):
        df = DiseaseFinder(self)
        df.grab_set()

    # vc = Vitals_Checker
    def vc(self):
        vc = VitalsCheck(self)
        vc.grab_set()


def main():
    app = HTRS()
    app.mainloop()


if __name__ == "__main__":
    main()
