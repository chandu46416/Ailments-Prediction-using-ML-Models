#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import numpy as np
import pandas as pd
#import tkinter as tk




# from gui_stuff import *

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

# print(df.head())

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
# ------------------------------------------------------------------------------------------------------

def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   
    clf3 = clf3.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")

# gui_stuff------------------------------------------------------------------------------------



root = Tk()
root.configure(background='black')



#canvas = Canvas(root, width = 20, height = 20)
#canvas.pack()
#img = PhotoImage(file="\\Users\\Dell\\Desktop\\anu\\Disease-prediction-using-Machine-Learning-master\\pic.png")
#canvas.create_image(920,920, anchor=NW, image=img)
#mainloop()









#my_frame = tk.Frame(parent_widget,borderwidth = 2)
#root.geometry("200*120")



#photo = PhotoImage(file="pic.png")
#imgLabel = Label(root,image=photo)
#imgLabel.pack(side=LEFT)
# entry variables
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)

Name = StringVar()

# Heading
w2 = Label(root, justify=LEFT, text=" AILMENTS  PREDICTION  USING  MACHINE  LEARNING  ALGORITHMS", fg="white", bg="black")
w2.config(font=("Elephant", 20))
w2.grid(row=1, column=0, columnspan=6, padx=100)
w3 = Label(root, justify=LEFT, text=" [ Nothing is more important than your health , We are just better at making you feel better  ] ", fg="white", bg="black")
w3.config(font=("italic",19))
w3.grid(row=3, column=0, columnspan=6, padx=100)




#websites

NameLbw1 = Label(root, text="TOP MOST HOSPITALS WEBSITES", fg="black", bg="grey")
NameLbw1.grid(row=7, column=0, pady=15, sticky=W)
NameLbw1a = Label(root, text=" https://www.manipalhospitals.com/", fg="red", bg="black")
NameLbw1a.grid(row=8, column=0, pady=15, sticky=W)
NameLbw1b = Label(root, text="http://kimscommunitymedicine.org/", fg="red", bg="black")
NameLbw1b.grid(row=9, column=0, pady=15, sticky=W)
NameLbw2 = Label(root, text="BLOOD BANK WEBSITES", fg="black", bg="grey")
NameLbw2.grid(row=10, column=0, pady=15, sticky=W)
NameLbw2a = Label(root, text="https://blood.kar.in/Home1.aspx", fg="red", bg="black")
NameLbw2a.grid(row=11, column=0, pady=15, sticky=W)
NameLbw3 = Label(root, text="APTAMITRA HELPLINE", fg="black", bg="grey")
NameLbw3.grid(row=12, column=0, pady=15, sticky=W)
NameLbw3a = Label(root, text="https://covid19.karnataka.gov.in", fg="red", bg="black")
NameLbw3a.grid(row=13, column=0, pady=15, sticky=W)


# labels
NameLb = Label(root, text="Name of the Patient ->", fg="yellow", bg="black")
NameLb.grid(row=7, column=1, pady=15, sticky=W)

#NameLb1 = Label(root, text="Patient Address", fg="yellow", bg="black")
#NameLb1.grid(row=6, column=1, pady=15, sticky=W)

#NameLb2 = Label(root, text="ph no", fg="yellow", bg="black")
#NameLb2.grid(row=7, column=1, pady=15, sticky=W)

S1Lb = Label(root, text="Symptom 1 ->", fg="yellow", bg="black")
S1Lb.grid(row=8, column=1, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2 ->", fg="yellow", bg="black")
S2Lb.grid(row=9, column=1, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3 ->", fg="yellow", bg="black")
S3Lb.grid(row=10, column=1, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4 ->", fg="yellow", bg="black")
S4Lb.grid(row=11, column=1, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5 ->", fg="yellow", bg="black")
S5Lb.grid(row=12, column=1, pady=10, sticky=W)


lrLb = Label(root, text="DecisionTree Result", fg="white", bg="red")
lrLb.grid(row=13, column=1, pady=10,sticky=W)

destreeLb = Label(root, text="RandomForest Result", fg="white", bg="red")
destreeLb.grid(row=14, column=1, pady=10, sticky=W)

ranfLb = Label(root, text="NaiveBayes Result", fg="white", bg="red")
ranfLb.grid(row=15, column=1, pady=10, sticky=W)



w4 = Label(root, justify=LEFT, text="DOCTORS DESCRIPTIONS ARE GIVEN BELOW", fg="black", bg="white")
w4.config(font=("Elephant", 12))
w4.grid(row=16, column=0, columnspan=2, padx=100)
#NameLb1 = Label(root, text="Doctor description", fg="white", bg="black")
#NameLb1.grid(row=18, column=1, pady=10, sticky=W)
#S1En9 = OptionMenu(root, Symptom6,*OPTIONS)
#S1En9.grid(row=20, column=1)
NameLb2 = Label(root, text=" * Dr. Ashok kumar", fg="black", bg="grey")
NameLb2.grid(row=17, column=0, pady=10, sticky=W)
NameLb3 = Label(root, text=" * M.D (Int.Medicine),Physician" , fg="black", bg="grey")
NameLb3.grid(row=18, column=0, pady=10, sticky=W)
NameLb4 = Label(root, text="*  Address: #1683/1,Near stadium", fg="black", bg="grey")
NameLb4.grid(row=19, column=0, pady=10, sticky=W)
NameLb5 = Label(root, text="*  Aaraike Hospital", fg="black", bg="grey")
NameLb5.grid(row=20, column=0, pady=10, sticky=W)
NameLb6 = Label(root, text="*  phno-233446", fg="black", bg="grey")
NameLb6.grid(row=21, column=0, pady=10, sticky=W)
#NameLb7 = Label(root, text="Hadadi Road,Davanagere", fg="yellow", bg="black")
#NameLb7.grid(row=22, column=0, pady=10, sticky=W)

NameLb9 = Label(root, text="*   Dr. Ravi kumar", fg="black", bg="grey")
NameLb9.grid(row=17, column=1, pady=10, sticky=W)
NameLb10 = Label(root, text="*  M.B.B.S, M.S,General  Surgeon", fg="black", bg="grey")
NameLb10.grid(row=18, column=1, pady=10, sticky=W)
NameLb11 = Label(root, text="*  Address: #1245/17,Behind church road        ", fg="black", bg="grey")
NameLb11.grid(row=19, column=1, pady=10, sticky=W)
NameLb12 = Label(root, text="*  RamaKrishna Hospital", fg="black", bg="grey")
NameLb12.grid(row=20, column=1, pady=10, sticky=W)
NameLb13 = Label(root, text="*  Phno-224466", fg="black", bg="grey")
NameLb13.grid(row=21, column=1, pady=10, sticky=W)
#NameLb14 = Label(root, text="Hadadi Road,Davanagere", fg="yellow", bg="black")
#NameLb14.grid(row=22, column=1, pady=10, sticky=W)

NameLb15 = Label(root, text="*  Dr. Mahesh", fg="black", bg="grey")
NameLb15.grid(row=17, column=2, pady=10, sticky=W)
NameLb16 = Label(root, text="*  M.B.B.S", fg="black", bg="grey")
NameLb16.grid(row=18, column=2, pady=10, sticky=W)
NameLb17 = Label(root, text="*  Consultant Physician and Nephrologist", fg="black", bg="grey")
NameLb17.grid(row=19, column=2, pady=10, sticky=W)
NameLb18 = Label(root, text="*  Address: Bapuji Hospital", fg="black", bg="grey")
NameLb18.grid(row=20, column=2, pady=10, sticky=W)
NameLb19 = Label(root, text="*  Phno-8496092259", fg="black", bg="grey")
NameLb19.grid(row=21, column=2, pady=10, sticky=W)
#NameLb20 = Label(root, text="Hadadi Road,Davanagere", fg="yellow", bg="black")
#NameLb20.grid(row=22, column=2, pady=10, sticky=W)






# entries
OPTIONS = sorted(l1)

NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=7, column=1)

#NameEn1 = Entry(root, textvariable=Name)
#NameEn1.grid(row=6, column=1)

#NameEn2 = Entry(root, textvariable=Name)
#NameEn2.grid(row=7, column=1)
S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=8, column=1)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=9, column=1)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=10, column=1)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=11, column=1)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=12, column=1)







Names = Label(root, text="Choose algorithm here -->", fg="white", bg="green")
Names.grid(row=9, column=2, pady=18, sticky=W)
dst = Button(root, text="DecisionTree", command=DecisionTree,bg="green",fg="white")
dst.grid(row=10, column=2,padx=18)

rnf = Button(root, text="Randomforest", command=randomforest,bg="green",fg="white")
rnf.grid(row=11, column=2,padx=18)

lr = Button(root, text="NaiveBayes", command=NaiveBayes,bg="green",fg="white")
lr.grid(row=12, column=2,padx=18)








#textfileds
t1 = Text(root, height=1, width=32,bg="white",fg="black")
t1.grid(row=13, column=2, padx=12)

t2 = Text(root, height=1, width=32,bg="white",fg="black")
t2.grid(row=14, column=2 , padx=10)

t3 = Text(root, height=1, width=32,bg="white",fg="black")
t3.grid(row=15, column=2 , padx=10)




w5 = Label(root, justify=LEFT, text="HELPLINE", fg="black", bg="white")
w5.config(font=("Elephant", 12))
w5.grid(row=8, column=5, columnspan=2, padx=100)
NameLb20 = Label(root, text="Helpline", fg="black", bg="white")
NameLb20.grid(row=9, column=5, pady=10, sticky=W)
NameLb21 = Label(root, text="9980299802", fg="blue", bg="white")
NameLb21.grid(row=9, column=6, pady=10, sticky=W)
NameLb22 = Label(root, text="Health and Family welfare", fg="black", bg="white")
NameLb22.grid(row=10, column=5, pady=10, sticky=W)
NameLb23 = Label(root, text="104", fg="blue", bg="white")
NameLb23.grid(row=10, column=6, pady=10, sticky=W)
NameLb24 = Label(root, text="Food and civil suppliers", fg="black", bg="white")
NameLb24.grid(row=11, column=5, pady=10, sticky=W)
NameLb25 = Label(root, text="18000-425-9339/1967", fg="blue", bg="white")
NameLb25.grid(row=11, column=6, pady=10, sticky=W)
NameLb26 = Label(root, text="covid emergency numbers", fg="black", bg="white")
NameLb26.grid(row=12, column=5, pady=10, sticky=W)
NameLb27 = Label(root, text="9745697456", fg="blue", bg="white")
NameLb27.grid(row=12, column=6, pady=10, sticky=W)

w6 = Label(root, justify=LEFT, text="COVID GUIDELINES", fg="black", bg="white")
w6.config(font=("Elephant", 12))
w6.grid(row=14, column=5, columnspan=2, padx=100)
w7 = Label(root, justify=LEFT, text="** Wash your hands often", fg="red", bg="black")
w7.config(font=("Elephant", 10))
w7.grid(row=15, column=5, columnspan=2, padx=100)
w8 = Label(root, justify=LEFT, text="** Avoid close contact", fg="red", bg="black")
w8.config(font=("Elephant", 12))
w8.grid(row=16, column=5, columnspan=2, padx=100)
w9 = Label(root, justify=LEFT, text="** Cover your mouth and nose with mask", fg="red", bg="black")
w9.config(font=("Elephant", 12))
w9.grid(row=17, column=5, columnspan=2, padx=100)
w10 = Label(root, justify=LEFT, text="** Clean and disinfect", fg="red", bg="black")
w10.config(font=("Elephant", 12))
w10.grid(row=18, column=5, columnspan=2, padx=100)
w11 = Label(root, justify=LEFT, text="** Monitor your health daily", fg="red", bg="black")
w11.config(font=("Elephant", 12))
w11.grid(row=19, column=5, columnspan=2, padx=100)
w12 = Label(root, justify=LEFT, text="** Be alert of symptoms", fg="red", bg="black")
w12.config(font=("Elephant", 12))
w12.grid(row=20, column=5, columnspan=2, padx=100)
w13 = Label(root, justify=LEFT, text="** Check temperature", fg="red", bg="black")
w13.config(font=("Elephant", 12))
w13.grid(row=21, column=5, columnspan=2, padx=100)













root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




