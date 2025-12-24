# Insurance_cost_prediction
This project focuses on actual implementation of a machine learning model to predict the premium price.

## Project Overview and Objectives
   
### Problem Statement

Insurance companies need to accurately predict the cost of health insurance for individuals to set premiums appropriately. However, traditional methods of cost prediction often rely on broad actuarial tables and historical averages, which may not account for the nuanced differences among individuals. By leveraging machine learning techniques, insurers can predict more accurately the insurance costs tailored to individual profiles, leading to more competitive pricing and better risk management.

The objectives are twofold:

•	Descriptive Analysis: Discover patterns and correlations among the variables in the dataset.

•	Predictive Modeling: Implement a simple machine learning model (Decision Tree) to determine how well these factors can predict individual medical charges.

## Dataset Description

The dataset comprises the following 11 attributes:
1.	Age: Numeric, ranging from 18 to 66 years.
2.	Diabetes: Binary (0 or 1), where 1 indicates the presence of diabetes.
3.	Blood Pressure Problems: Binary (0 or 1), indicating the presence of blood pressure-related issues.
4.	Any Transplants: Binary (0 or 1), where 1 indicates the person has had a transplant.
5.	Any Chronic Diseases: Binary (0 or 1), indicating the presence of any chronic diseases.
6.	Height: Numeric, measured in centimeters, ranging from 145 cm to 188 cm.
7.	Weight: Numeric, measured in kilograms, ranging from 51 kg to 132 kg.
8.	Known Allergies: Binary (0 or 1), where 1 indicates known allergies.
9.	History Of Cancer InFamily: Binary (0 or 1), indicating a family history of cancer.
10.	Number Of Major Surgeries: Numeric, counting the number of major surgeries, ranging from 0 to 3 surgeries.
11.	Premium Price: Numeric, representing the premium price in currency, ranging from 15,000 to 40,000.

## Project Components

### 1. Data Exploration and Visualization

Basic data analysis (shape, data types, summary statistics)
Checking for missing values
Creating visualizations to understand the relationships between variables
Analyzing the distribution of premium prices
Exploring correlations between features

### 2. Hypothesis Testing
   
Whether premium costs differ significantly based on diabetes status
Whether premium costs differ significantly based on chronic disease status
Whether premium costs differ significantly based on the number of major surgeries
Whether age is a significant predictor of premium price
Whether BMI is a significant predictor of premium price
Whether multiple factors together significantly predict premium price

### 3. Machine Learning Modeling

Feature engineering (e.g., calculating BMI)
Data splitting into training and testing sets
Feature scaling
Training multiple regression models:
Linear Regression
Ridge Regression
Lasso Regression
Decision Tree
Random Forest
Gradient Boosting
Model evaluation using metrics like RMSE, MAE, and R²
Hyperparameter tuning for the best-performing model
Saving the trained models for later use

### 4. Web-Based Application
The web application (webapp.py) is built using Streamlit and provides:

A user-friendly interface for inputting personal health data
Real-time premium cost prediction using the trained model
Risk factors analysis based on feature importance
Personalized recommendations based on the user's health profile


Calculates BMI and creates BMI categories
Creates age groups
Creates premium price categories
Calculates a risk score based on health conditions
Creates risk categories

# How to Run the Project:

## 1. Data Exploration and Visualization , Hypothesis Testing and Machine learning modelling:
   
   run the Google colab notebook 'INSURANCE_COST_PREDICTION.ipynb'

## 2. Run the webapplication:
   
   streamlit run code/webapp.py

# Conclusion

This project demonstrates how machine learning can be used to predict insurance premium costs based on individual health profiles. The insights gained from this analysis can help insurance companies set premiums more accurately and provide personalized recommendations to policyholders.
