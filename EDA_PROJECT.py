#EDA PROJECT ON TELCOM

#step 1: import libararies

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Step 2: Load the Data
file_path = ('C:\\Customer_Churn.csv')  # Fixed path
df = pd.read_csv(file_path)
print(df.head())
"""file_path = 'C:\Customer_Churn.csv'
print("File exists:", os.path.exists(file_path))"""

#step 3: inspect data
df.info()

#replacing the blank with 0 & and changed the data type.
df["TotalCharges"] = df["TotalCharges"].replace(" ","0")
df["TotalCharges"] = df["TotalCharges"].astype("float")
df.info()

#check null values
print(df.isnull().sum().sum())

print(df.describe())

#check for duplicates
"""print(df.duplicated().sum()) """
print(df["customerID"].duplicated().sum()) 

#covert values for seniorcitizen (0 & 1) to ( no & yes) resp.

def conv(values):
    if values ==1:
        return "Yes"
    else:
        return "No"
    
df["SeniorCitizen"] = df["SeniorCitizen"].apply(conv)
print(df.head())


#step : Analaysies

#to analysize churn how many customer are in service or not

ax = sns.countplot(x = "Churn",data =df)    #to get count assign it inside ax

ax.bar_label(ax.containers[0])
plt.title("Count Of Customer By Churn")
plt.show()

#to above in percentage
plt.figure(figsize = (3,4))
gb = df.groupby("Churn").agg({'Churn':'count'})                                      #values are in string why using group by function
plt.pie(gb['Churn'], labels = gb.index, autopct = "%1.2f%%")
plt.title("Percentage Of Churned Customer")
plt.show()

"""##From the given pie chart we can conclude that 26.54% of our customer churn out."""

# by gender
plt.figure(figsize = (4,4))
sns.countplot(x = "gender",data =df , hue = "Churn")
plt.title("Churn By Gender")
plt.show() 

"""##"""
#by snior citizen

plt.figure(figsize = (4,4))
ax = sns.countplot(x = "SeniorCitizen", data = df)
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Senior Citizen")
plt.show()

""""""""""""""""Stacked Bar Chart"""

total_counts = df.groupby('SeniorCitizen')['Churn'].value_counts(normalize=True).unstack() * 100

# Plot
fig, ax = plt.subplots(figsize=(4, 4))  # Adjust figsize for better visualization

# Plot the bars
total_counts.plot(kind='bar', stacked=True, ax=ax, color=['#1f77b4', '#ff7f0e'])  # Customize colors if desired

# Add percentage labels on the bars
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy()
    ax.text(x + width / 2, y + height / 2, f'{height:.1f}%', ha='center', va='center')

plt.title('Churn by Senior Citizen (Stacked Bar Chart)')
plt.xlabel('SeniorCitizen')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.legend(title='Churn', bbox_to_anchor = (0.9,0.9))  # Customize legend location

plt.show()

"""##comparaively a greated percentage of people in senior citizen
have churned"""

#by tenure churn count:
plt.figure(figsize = (9,4))
sns.histplot(x = "tenure", data = df, bins = 72, hue = "Churn")
plt.show()

"""##peolpe who have sed our services for a long time stayed and peolpe who have used
our services for 1 or 2  have churned"""

# count of customer by contract

plt.figure(figsize = (4,4))
ax = sns.countplot(x = "Contract", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Contract")
plt.show()


"""##People who have month to month contract are likelyto churn then
from those who have 1 or 2 year of contract"""

#subplots :
print(df.columns.values)

columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 
           'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

# Number of columns for the subplot grid (you can change this)
n_cols = 3
n_rows = (len(columns) + n_cols - 1) // n_cols  # Calculate number of rows needed

# Create subplots
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 4))  # Adjust figsize as needed

# Flatten the axes array for easy iteration (handles both 1D and 2D arrays)
axes = axes.flatten()

# Iterate over columns and plot count plots
for i, col in enumerate(columns):
    sns.countplot(x=col, data=df, ax=axes[i], hue = df["Churn"])
    axes[i].set_title(f'Count Plot of {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Count')

# Remove empty subplots (if any)
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

"""##The majority of customers who do not churn tend to have services like PhoneService, 
InternetService (particularly DSL), and OnlineSecurity enabled. 
For services like OnlineBackup, TechSupport, and StreamingTV, 
churn rates are noticeably higher when these services are not used or are unavailable."""

# count by payment method

plt.figure(figsize = (6,4))
ax = sns.countplot(x = "PaymentMethod", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churned Customers by Payment Method")
plt.xticks(rotation = 45)
plt.show()

"""##customer is likely to churn when he is using electronic check as a payment method."""

plt.figure(figsize = (6,4))
ax = sns.countplot(x = "PaperlessBilling", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churned Customers by PaperlessBilling")
plt.xticks(rotation = 45)
plt.show()

"""##customer is likely to churn when they are not using paperless billing"""




