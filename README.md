# Project 4: Heart Disease Awareness Application


## Problem statement
The leading cause of death in America is heart disease, taking more than 800,000 people's lives each and every year. Our main goal we wanted to achieve here was to raise awareness for heart disease by creating a model that will classify the risk of heart disease for individuals through a free and accessible web application.

---

## Overview
With heart disease being such a prevalent killer in the U.S., we wanted to try and bring more awareness to the disease and allow people to possibly identify whether or not they could be at risk of cardiovascular disease. We aimed to do this by building models and applying them to a quick and easy to use survey via our web application which would, after all the information has been accurately filled in, could identify if the individual was at risk.



---

## Table of Contents
- **Data Folder** - Contains .csv file of the used dataset (link also below).
- **Models Folder** - Contains various models created.
- **Presentation.pdf** - Presentation explaining findings and work process.
- **[Application](https://typikal1-dsi-project-4-heart-disease-app-xtqo6y.streamlitapp.com)**

---

## Data Description
The data we used was a popular dataset that we found on Kaggle. Most of the data from the dataset had already been modified in one way or another. Some columns had been binarized and others had been normalized in some way that we paid close attention to. We validated the preprocessing process that was taken and that the data was cleaned by extensive EDA and making sure none of the data was incomplete or incorrect in any way. The data contains various risk factors which could be good indicators of someone having either heart disease or potentially at risk of having a heart attack. There are 22 features that are used in our models to predict whether the individual providing the information could be at risk of having heart disease or a heart attack.

- [Heart Disease Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/heart-disease-health-indicators-dataset)

### Data Dictionary
| Risk Factors | Type | Description | Notes |
|---|---|---|---|
|**HighBP**| *float* | High blood pressure | 0 = No / 1 = Yes |
|**GenHlth**|*float*| Overall general health status | 0 = Unhealthy / 1 = Healthy |
|**Age**|*float*| Masked age of individual | 18-24 years old = 1, in increments of 5 to 13, 14 being no response |
|**DiffWalk**|*float*| Do you have serious difficulty walking or climbing stairs? | 0 = No / 1 = Yes |
|**Stroke**|*float*| Ever Diagnosed with a Stroke | 0 = No / 1 = Yes |
|**PhysHlth**|*float*| How many days during the past 30 days was your physical health not good? | 1-30 |
|**HighChol**|*float*| Have been told by the doctor that you have high cholesterol| 0 = No / 1 = Yes |
|**Diabetes**|*float*| Ever told you have diabetes | 0 = No / 1 = Yes / 2 = Yes, but only while pregnant |
|**Smoker**|*float*| Adults who are current smokers |  0 = No / 1 = Yes  |
|**Sex**|*float*| Male or Female | Male = 1 and female = 0 |
|**MentHlth**|*float*| How many days during the past 30 days was your mental health not good? | 1-30 |
|**BMI**|*float*| Computed body mass index | 0 - 100 |
|**CholCheck**|*float*| Ever Had Blood Cholesterol Checked | 0 = No / 1 = Yes |
|**NoDocbcCost**|*float*| Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? | 0 = No / 1 = Yes |
|**AnyHealthcare**|*float*| Respondents aged 18-64 who have any form of health care coverage | 0 = No / 1 = Yes |
|**Fruits**|*float*| Have ate fruit in the last 30 days | 0 = No / 1 = Yes |
|**HvyAlcoholConsump**|*float*| Heavy drinkers (men having more than 14 drinks per week and women having more than 7 drinks per week)| 0 = No / 1 = Yes |
|**Veggies**|*float*| Have ate veggies in the last 30 days | 0 = No / 1 = Yes |
|**PhysActivity**|*float*| Did you do any physical activities in the last 30 days | 0 = No / 1 = Yes |
|**Education**|*float*| What is the highest grade or year of school you completed? | 1-6 |
|**Income**|*float*| Annual income level | 1-8 |


---

## Modeling Process  
Used a Neural Network as our main model in the streamlit app. Due to the imbalanced classifications (90% no heart disease and 10% heart disease), our first models predominantly predicted 0. We were getting scores of 90%, so we thought our model was working well. We realized that our model was faulty when we compared the true values with the predicted values through a confusion matrix. Our models were heavily predicting 0, "no heart disease". Our solution was to take a smaller sample of the majority class, "no heart disease", and fit our models on a 50/50 split of the data. Our overall performance decreased to just under 80%, but we now have balanced predictions and are more accurately classifying those at risk of heart disease.

---

### Software Requirements
- Pandas
- Scikit-learn
- TensorFlow/Keras



