# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 23:54:16 2023

@author: umarm
"""

import numpy as np
import pickle
import streamlit as st

loadedmodel=pickle.load(open('C:/Users/umarm/MLprojectsFolder/CholeraPredictionModel/cholera_model.sav','rb'))

def cholera_prediction(input_data):
    input_data_np_array= np.asarray(input_data)
    input_reshape=input_data_np_array.reshape(1,-1)
    prediction=loadedmodel.predict(input_reshape)
    print(prediction)

    if (prediction[0]==1):
      return"YOU HAVE CHOLERA! PLEASE TAKE  'doxycycline', 'azithromycin' and 'ciprofloxacin' AS INITIAL MEDICATION AND CONSULT A DOCTOR IMMEDIATELY!"
    else:
      return "YOU DON'T HAVE CHOLERA!"
  
    
def main():
    st.title("DO YOU HAVE CHOLERA?")
    
    
    fever=st.text_input("DO YOU HAVE A FEVER?")
    
    headaches_and_nausea=st.text_input("DO YOU FEEL NAUSEOUS AND DO YOU HAVE A HEADACHE?")
    
    vomiting=st.text_input("DID YOU VOMIT RECENTLY?")
    
    fatigue=st.text_input("ARE YOU FEELING FATIGUED?")
    
    severe_dehydration=st.text_input("ARE YOU DEHYDRATED?")
    
    diarrhea=st.text_input("DIARRHEA?")
    
    pain_in_abdomen=st.text_input("ANY PAIN IN ABDOMEN SIR?")
    
    
    diagnosis=''
    
    if st.button("SIR YOU'RE RESULT!"):
        diagnosis=cholera_prediction([fever,headaches_and_nausea,vomiting,fatigue,severe_dehydration,diarrhea,pain_in_abdomen])
        
    st.success(diagnosis)
        
if __name__=='__main__':
    main()