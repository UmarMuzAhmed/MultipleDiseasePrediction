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