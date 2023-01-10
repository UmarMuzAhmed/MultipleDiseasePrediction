# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:32:26 2023

@author: umarm
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

cholera_model=pickle.load(open('C:/Users/umarm/MLprojectsFolder/MultipleDiseasePrediction/savedmodels/cholera_model.sav','rb'))


jaundice_model=pickle.load(open('C:/Users/umarm/MLprojectsFolder/MultipleDiseasePrediction/savedmodels/jaundice_model.sav','rb'))


thyphoid_model=pickle.load(open('C:/Users/umarm/MLprojectsFolder/MultipleDiseasePrediction/savedmodels/thyphoid_model.sav','rb'))


heart_model=pickle.load(open('C:/Users/umarm/MLprojectsFolder/MultipleDiseasePrediction/savedmodels/heart_model.sav','rb'))


diabetes_model=pickle.load(open('C:/Users/umarm/MLprojectsFolder/MultipleDiseasePrediction/savedmodels/diabetes_model.sav','rb'))

with st.sidebar:
    selected=option_menu("MULTIPLE DISEASE PREDICTION",
                         ['CHOLERA PREDICTION',
                          'JAUNDICE PREDICTION',
                          'THYPHOID PREDICTION',
                          'HEART DISEASE PREDICTION',
                          'DIABETES PREDICTION'],
                         icons=['droplet half','file-medical','heart','activity','person'],
                         default_index=0)
    
if (selected=='CHOLERA PREDICTION'):
    st.title("CHECK IF YOU THINK YOU HAVE CHOLERA?")
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        fever=st.text_input("DO YOU HAVE A FEVER?")
    with col2:
        headaches_and_nausea=st.text_input("DO YOU FEEL NAUSEOUS?")
    with col3:
        vomiting=st.text_input("DID YOU VOMIT RECENTLY?")
    with col1:     
        fatigue=st.text_input("ARE YOU FEELING FATIGUED?")
    with col2: 
        severe_dehydration=st.text_input("ARE YOU DEHYDRATED?")
    with col3: 
        diarrhea=st.text_input("DIARRHEA?")
    with col1:
        pain_in_abdomen=st.text_input("ANY PAIN IN ABDOMEN SIR?")    
    
    diagnosis=''
    
    if st.button("SIR YOU'RE RESULT!"):
        diagnosis_result=cholera_model.predict([[fever,headaches_and_nausea,vomiting,fatigue,severe_dehydration,diarrhea,pain_in_abdomen]])
        if (diagnosis_result[0]==1):
           diagnosis ="YOU HAVE CHOLERA! PLEASE TAKE  'doxycycline', 'azithromycin' and 'ciprofloxacin' AS INITIAL MEDICATION AND PLEASE CONSULT A DOCTOR IMMEDIATELY"
        else:
          diagnosis= "YOU DON'T HAVE CHOLERA!"
    st.success(diagnosis)
    
if (selected=='JAUNDICE PREDICTION'):
    st.title("CHECK IF YOU THINK YOU HAVE JAUNDICE?")
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input('HOW OLD ARE YOU?')
    with col2:
        fever=st.text_input('DO YOU HAVE HIGH FEVER?')
    with col3:
        chills=st.text_input('ARE YOU GETTING CHILLS?')
    with col1:
        abdominal_pain=st.text_input('ARE YOU FEELING ANY ABDOMINAL PAIN?')
    with col2:
        yellowing_of_skin=st.text_input('YELLOWING OF SKIN?')
    with col3:
        yellowing_of_eyes=st.text_input('YELLOWING OF EYES?')
    with col1:
        dark_colored_urine=st.text_input('DID YOU HAD DARK COLOURED URINE?')
    
    jaun_diagnosis=''
    
    if st.button("SIR YOU'RE RESULT!"):
        diagnosis_result=jaundice_model.predict([[age,fever,chills,abdominal_pain,yellowing_of_skin,yellowing_of_eyes,dark_colored_urine]])
        if (diagnosis_result[0]==1):
           jaun_diagnosis ="YOU HAVE JAUNDICE! PLEASE TAKE  'cholestyramine (Questran®)' AS INITIAL MEDICATION AND PLEASE CONSULT A DOCTOR IMMEDIATELY"
        else:
          jaun_diagnosis= "YOU DON'T HAVE JAUNDICE!"
    st.success(jaun_diagnosis)
    
    
if (selected=='THYPHOID PREDICTION'):
    st.title("CHECK IF YOU THINK YOU HAVE THYPHOID?")
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input('HOW OLD ARE YOU?')
    with col2:
        fever=st.text_input('DO YOU HAVE HIGH FEVER?')
    with col3:
        chills=st.text_input('ARE YOU GETTING CHILLS?')
    with col1:
        bloating=st.text_input("DO YOU HAVE A BLOATED STOMACH?")
    with col2:
        red_dots_on_skin=st.text_input('DO YOU HAVE RED DOTS ON YOUR SKIN?')
    with col3:
        loss_of_appetite=st.text_input('HOW IS YOUR APPETITE?')
    
    
    diagnosis=''
    
    if st.button("SIR YOU'RE RESULT!"):
        diagnosis_result=thyphoid_model.predict([[age,fever,chills,bloating,red_dots_on_skin,loss_of_appetite]])
        if (diagnosis_result[0]==1):
           diagnosis ="YOU HAVE THYPHOID! PLEASE TAKE  'Ciprofloxacin (Cipro)' AS INITIAL MEDICATION AND PLEASE CONSULT A DOCTOR IMMEDIATELY"
        else:
          diagnosis= "YOU DON'T HAVE THYPHOID!"
    st.success(diagnosis)
    
    
if (selected=='HEART DISEASE PREDICTION'):
    st.title("CHECK IF YOU THINK YOU HAVE ANY HEART PROBLEM?")
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.text_input("HOW OLD ARE YOU?")        
    with col2:
        sex=st.text_input("MALE/FEMALE/X")        
    with col3:
        cp =st.text_input('ANY CHEST PAIN?')       
    with col1:
        trestbps=st.text_input('resting blood pressure')   
    with col2:
        chol=st.text_input('serum cholestoral in mg/dl')
    with col3:
        fbs=st.text_input('fasting blood sugar > 120 mg/dl')  
    with col1:
        restecg=st.text_input('resting electrocardiographic results')    
    with col2:
        thalach=st.text_input('maximum heart rate achieved')   
    with col3:
        exang=st.text_input('exercise induced angina') 
    with col1:
        oldpeak=st.text_input('ST depression induced by exercise relative to rest')    
    with col2:
        slope=st.text_input('the slope of the peak exercise ST segment') 
    with col3:
        ca=st.text_input('number of major vessels (0-3) colored by flourosopy')
    with col1:
        thal=st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    
    diagnosis=''
    
    if st.button("SIR YOU'RE RESULT!"):
        diagnosis_result=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (diagnosis_result[0]==1):
           diagnosis ="YOU HAVE HEART DISEASES! PLEASE CONSULT A DOCTOR IMMEDIATELY"
        else:
          diagnosis= "YOU DON'T HAVE HEART DISEASES!"
    st.success(diagnosis)
    
    
    
    
if (selected=='DIABETES PREDICTION'):
    st.title("CHECK IF YOU THINK YOU HAVE DIABETES?")
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Glucose=st.text_input("WHAT WERE YOUR GLUCOSE LEVEL BEFORE THE MEAL?")
    with col2:
        BloodPressure=st.text_input('WHAT IS YOUR BLOOD PRESSURE?')
    with col3:
        SkinThickness=st.text_input("WHAT IS YOUR FAT PERCENTAGE?")
    with col1:
        Insulin=st.text_input('WHAT ARE YOUR INSULIN LEVELS?')
    with col2:
        BMI=st.text_input('WHAT IS YOUR BODY MASS INDEX?')
    with col3:
        DiabetesPedigreeFunction=st.text_input('*likelihood of diabetes based on family history*')
    with col1:
        Age=st.text_input('WHAT IS YOUR AGE?')
    
    
    diagnosis=''
    
    if st.button("SIR YOU'RE RESULT!"):
        diagnosis_result=diabetes_model.predict([[Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (diagnosis_result[0]==1):
           diagnosis ="YOU HAVE DIABETES! PLEASE TAKE  'Metformin' AS INITIAL MEDICATION AND PLEASE CONSULT A DOCTOR IMMEDIATELY"
        else:
          diagnosis= "YOU DON'T HAVE DIABETES!"
    st.success(diagnosis)
    