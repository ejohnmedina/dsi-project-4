import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn
import xgboost


if __name__ == '__main__':
    st.title('Heart Disease Prediction ')
    st.write('''This web site is provided for educational and informational purposes only 
    and does not constitute providing medical advice or professional services. 
    The information provided should not be used for diagnosing or treating a health problem or disease, 
    and those seeking personal medical advice should consult with a licensed physician. 
    Always seek the advice of your doctor or other qualified health provider regarding a medical condition. 
    Never disregard professional medical advice or delay in seeking it because of something you have read on 
    this streamlit app. If you think you may have a medical emergency, call 911 or go to the nearest 
    emergency room immediately. No physician-patient relationship is created by this web site or its use.
     No contributor to this web site, makes any representations, 
     express or implied, with respect to the information provided herein or to its use.
     (This disclaimer was adapted from https://www.uwmedicine.org/about/compliance/disclaimer)''')
    st.write('''Please modify the questions below to predict your likelihood for heart disease.''')

    with open('models/nn_focus.pkl', 'rb') as pickle_in:
        pipe = pickle.load(pickle_in)

    highBP = st.radio(
    "Have you ever been told that you have high blood pressure by a doctor?",
    ('Yes', 'No'), index=1)
    if highBP == 'Yes':
        highBP = 1
    else:
        highBP = 0



    highChol = st.radio(
    "Have you ever been told that you have high cholesterol by a doctor?",
    ('Yes', 'No'), index=1)
    if highChol == 'Yes':
        highChol = 1
    else:
        highChol = 0

    chol_check = st.radio(
    "Have you ever had your cholesterol checked?",
    ('Yes', 'No'), index=1)
    if chol_check == 'Yes':
        chol_check = 1
    else:
        chol_check = 0

    smoker = st.radio(
    "Are you a current smoker?",
    ('Yes', 'No'), index=1)
    if smoker == 'Yes':
        smoker = 1
    else:
        smoker = 0

    stroke = st.radio(
    '''Have you ever been diagnosed with a stroke?''',
    ('Yes', 'No'), index=1)
    if stroke == 'Yes':
        stroke = 1
    else:
        stroke = 0

    diabetes = st.radio(
    "Do you have diabetes?",
    ('Yes', 'No','Only while pregnant'), index=1)
    if diabetes == 'Yes':
        diabetes = 1
    elif diabetes == 'No':
        diabetes = 0
    else:
        diabetes = 2

    exercise = st.radio(
    '''During the past month, other than your regular job, did you participate in any physical 
    activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise?''',
    ('Yes', 'No'), index=0)
    if exercise == 'Yes':
        exercise = 1
    else:
        exercise = 0


    fruits = st.radio(
    "Do you eat fruits regularly?",
    ('Yes', 'No'), index=0)
    if fruits == 'Yes':
        fruits = 1
    else:
        fruits = 0

    veggies = st.radio(
    "Do you eat vegetables regularly?",
    ('Yes', 'No'), index=0)
    if veggies == 'Yes':
        veggies = 1
    else:
        veggies = 0


    alcohol = st.radio(
    "Do you drink alcohol frequently?",
    ('Yes', 'No'), index=1)
    if alcohol == 'Yes':
        alcohol = 1
    else:
        alcohol = 0

    healthcare = st.radio(
    "Do you have healthcare?",
    ('Yes', 'No'), index=0)
    if healthcare == 'Yes':
        healthcare = 1
    else:
        healthcare = 0

    noDocbcCost = st.radio(
    "Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?",
    ('Yes', 'No'), index=1)
    if noDocbcCost == 'Yes':
        noDocbcCost = 1
    else:
        noDocbcCost = 0

    gen_health = st.radio(
    "Would you say that in general your health is:?",
    ('Excellent', 'Very good','Good', 'Fair', 'Dont know'), index=1)
    if gen_health == 'Excellent':
        gen_health = 1
    elif gen_health == 'Very good':
        gen_health = 2
    elif gen_health == 'Good':
        gen_health = 3
    elif gen_health == 'Fair':
        gen_health = 4
    elif gen_health == 'Dont know':
        gen_health = 5



    mental_health = st.slider(
    '''Now thinking about your mental health, which includes stress, depression, and problems with emotions, 
    for how many days during the past 30 days was your mental health not good?''',0,30,0)


    phys_health = st.slider(
    '''Now thinking about your physical health, which includes physical illness and injury, 
    for how many days during the past 30 days was your physical health not good?''',0,30,0)

    diff_walk = st.radio(         
    "Do you serious difficulty walking or climbing stairs?",
    ('Yes', 'No'), index=1)
    if diff_walk == 'Yes':
        diff_walk = 1
    else:
        diff_walk = 0


# DOUBLE CHECK MALE = 1, FEMALE = 0
    sex = st.radio(         
    "Gender?",
    ('Male', 'Female'), index=1)
    if sex == 'Male':
        sex = 1
    else:
        sex = 0

    age = st.slider('How old are you?', 18, 130, 25)
    if age <= 24:
        age = 1
    elif age > 80:
        age = 13
    else:
        age = (age - 25)//5 + 2
    # st.write('''Calculated age value = ''', age)

    weight = st.slider('How much do you weigh in pounds?', 70, 400, 150)
    height = st.slider('What is your height in inches?', 36, 96, 69)
    bmi = (weight*703) / (height **2)
    st.write("Your bmi = ", round(bmi,2))


    ed = st.radio(         
    "What is the highest grade or year of school you completed??",
    ('Never attended school or only kindergarten', 
    'Grades 1 through 8 (elementary)',
    'Grades 9 through 11 (Some high school)',
    'Grades 12 or GED (High school graduate)',
    'College 1 year to 3 years (Some college or technical school)',
    'College 4 years or more (College graduate)'), index=5)
    if ed == 'Never attended school or only kindergarten':
        ed = 1
    elif ed == 'Grades 1 through 8 (elementary)':
        ed = 2
    elif ed == 'Grades 9 through 11 (Some high school)':
        ed = 3
    elif ed == 'Grades 12 or GED (High school graduate)':
        ed = 4
    elif ed == 'College 1 year to 3 years (Some college or technical school)':
        ed = 5
    else:
        ed = 6

    income = st.selectbox("What is your annual income?",
    ("Less than $10,000", "Between $10,000 and $15,000",  "Between $15,000 and $20,000",
     "Between $20,000 and $25,000",  "Between $25,000 and $35,000",  "Between $35,000 and $50,000",
      "Between $50,000 and $75,000",  "Greater than $75,000"), index = 7)
    if income == 'Less than $10,000':
        income = 1
    elif income == 'Between $10,000 and $15,000':
        income = 2
    elif income == 'Between $15,000 and $20,000':
        income = 3
    elif income == 'Between $20,000 and $25,000':
        income = 4
    elif income == 'Between $25,000 and $35,000':
        income = 5
    elif income == 'Between $35,000 and $50,000':
        income = 6
    elif income == 'Between $50,000 and $75,000':
        income = 7
    else:
        income = 8


    x = pd.DataFrame([[highBP, highChol, chol_check, bmi,
        smoker, stroke, diabetes, exercise, fruits, veggies,
        alcohol, healthcare, noDocbcCost, gen_health,
        mental_health, phys_health, diff_walk, sex, age, ed,
        income]], columns = ['HighBP', 'HighChol', 'CholCheck', 'BMI',
        'Smoker', 'Stroke', 'Diabetes', 'PhysActivity', 'Fruits', 'Veggies',
        'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth',
        'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education',
        'Income'])
    pred = pipe.predict(x) # nn test
    st.write('''The neural model predicts that your risk for heart disease is.... ''', round(100 * pred[0][0], 3), '%')

    st.write('''** This prediction is based on the model's training data and is not intended to be taken as medical advice or recommendation. As always, please see a qualified healthcare professional if you're experiencing any symptoms or have any concerns about your health.''')
    
    # if using classifier, comment out the above and uncomment the code below
    # pred = pipe.predict_proba(x)  -- classifier
    # st.write('''The model pridicts that your risk for heart disease is.... ''', 100*round(pred[0][1],3), '%') # boosting classifier models
