# -*- coding: utf-8 -*-
"""Covid Data Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cu7hynG6fPloY52uyemeRp6fluKXjKr9
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

data=pd.read_csv("Covid Dataset.csv")

data.info()

data.describe().T

data.isnull().sum()

data.duplicated().count()

data.drop_duplicates(inplace=True)
data.reset_index(drop=True, inplace=True)

data.duplicated().any()

print(data[data['COVID-19'] == 'Yes'].count())

print(data[data['COVID-19'] == 'No'].count())

data.head()

sns.countplot(x='COVID-19', data=data)

plt.title('Number of Confirmed Covid-19 Infection Cases')
plt.xlabel('Covid-19 PCR Test Result')
plt.ylabel('No. of Patients')

data["COVID-19"].value_counts().plot.pie(explode=[0.1,0.1],autopct='%1.1f%%',shadow=True)
plt.title('Pie Chart of the Number of Patients by Covid-19 PCR Result');

sns.countplot(x='Breathing Problem',data=data)

plt.title('Number of Patients with Breathing Problem')
plt.xlabel('Breathing Problem')
plt.ylabel('No. of Patients')

sns.countplot(x='Breathing Problem',hue='COVID-19',data=data)

sns.countplot(x='Fever',hue='COVID-19',data=data)

sns.countplot(x='Dry Cough',hue='COVID-19',data=data)

sns.countplot(x='Sore throat',hue='COVID-19',data=data)

sns.countplot(x='Running Nose',hue='COVID-19',data=data)

sns.countplot(x='Asthma',hue='COVID-19',data=data)

sns.countplot(x='Chronic Lung Disease',hue='COVID-19',data=data)

sns.countplot(x='Headache',hue='COVID-19',data=data)

sns.countplot(x='Heart Disease',hue='COVID-19',data=data)

sns.countplot(x='Diabetes',hue='COVID-19',data=data)

sns.countplot(x='Hyper Tension',hue='COVID-19',data=data)

sns.countplot(x='Abroad travel',hue='COVID-19',data=data)

sns.countplot(x='Contact with COVID Patient',hue='COVID-19',data=data)

sns.countplot(x='Attended Large Gathering',hue='COVID-19',data=data)

sns.countplot(x='Visited Public Exposed Places',hue='COVID-19',data=data)

sns.countplot(x='Family working in Public Exposed Places',hue='COVID-19',data=data)

sns.countplot(x='Wearing Masks',hue='COVID-19',data=data)

sns.countplot(x='Sanitization from Market',hue='COVID-19',data=data)

sns.countplot(x='Gastrointestinal ',hue='COVID-19',data=data)

sns.countplot(x='Fatigue ',hue='COVID-19',data=data)



"""OBSERVATIONS:

Symptoms that show a high cahnce of being affected by Covid :
1. Breathing Problem
2. Fever
3. Dry Cough
4. Sore throat


Symptoms that do not clearly show a particular trend :
1. Running Nose
2. Asthma
3. Chronic Lung Disease
4. Headache
5. Heart Disease
6. Diabetes
7. Hyper Tension
8. Contact with COVID Patient
9. Attended Large Gathering
10. Visited Public Exposed Places
11. Family working in Public Exposed Places
12. Gastrointestinal
13. Fatigue

People travelling abroad has a 100% record of getting affected by Covid.(But in this model we tend to use physical attributes)


Columns like - Wearing Masks, Sanitization from Market
have only one value, So makes no sense to include them in model.
"""

