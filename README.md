# Project 4: Heart Disease Awareness Application


## Problem statement
The leading cause of death in America is heart disease, taking more than 800,000 people's lives each and every year. Our main goal we wanted to achieve here was to raise awareness for heart disease by creating a model that will classify the risk of heart disease for individuals through a free and accesible web application.

---

## Overview
With heart disease being such a previlent killer in the U.S., we wanted to try and bring more awareness to the disease and allow people to possibly identify whether or not they could be at risk of cardiovasular disease. We aimed to do this by building models and applying them to a quick and easy to use survey via our web application which would, after all the information has been accurately filled in, could identify if the individual was at risk.



---

## Table of Contents
-
-
-
-

---

## Data Description
The data we used was a popular dataset that we found on Kaggle. Most of the data from the dataset had already been modified in one way or another. Some columns had been binarized and others had been normalized in some way that we payed close attention to. We validated the preproccessing process that was taken and that the data was cleaned by extensive EDA and making sure none of the data was incomplete or incorrect in any way. The data contains various risk factors which show could be good indicators of someone having either heart disease or potentially at risk of having a heart attack. There are 22 features that are used in our models to predict whether the individual providing the information could be at risk of having heart disease or a heart attack.

- [Heart Disease Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/heart-disease-health-indicators-dataset)

### Data Dictionary
| Risk Factors | Type | Description | Notes |
|---|---|---|---|
|**HighBP**| *float* | High blood pressure | 0 = No / 1 = Yes |
|**GenHlth**|*float*|||
|**Age**|*float*| Masked age of individual | 18-24 years old = 1, in incrments of 5 to 13, 14 being no response |
|**DiffWalk**|*float*|||
|**Stroke**|*float*|||
|**PhysHlth**|*float*|||
|**HighChol**|*float*|||
|**Diabetes**|*float*|||
|**Smoker**|*float*|||
|**Sex**|*float*| Male of Female | Male = 1 and female = 0 |
|**MentHlth**|*float*|||
|**BMI**|*float*|||
|**CholCheck**|*float*|||
|**NoDocbcCost**|*float*|||
|**AnyHealthcare**|*float*|||
|**Fruits**|*float*|||
|**HvyAlcoholConsump**|*float*|||
|**Veggies**|*float*|||
|**PhysActivity**|*float*|||
|**Education**|*float*|||
|**Income**|*float*|||

---

## Modeling Process
Our best models we ended up with were a XGBoost and neural network that ended up performing each around  
-dont know which models were going with so hard to answer this part 
-oversampling make sure to mention 

---

### Software Requirements
- Pandas
- Scikit-learn
- TensorFlow
not sure how specific we need to get here


