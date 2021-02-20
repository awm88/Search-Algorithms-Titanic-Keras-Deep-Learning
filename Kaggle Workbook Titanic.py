#Titanic Assignment Kaggle #Kaggle Username: Awmnah Asad #Name of Project: FINAL PROJECT
#Step 1: Importing:
    
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import style

from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.metrics import roc_curve, auc


from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import GaussianNB

  
import string

#importing testing and training data 
csv_test_path = 'C:/Users/awmna/Downloads/test.csv'
csv_train_path = 'C:/Users/awmna/Downloads/train.csv'

train_df = pd.read_csv(csv_train_path)
train_df.head()

test_df = pd.read_csv(csv_test_path)
test_df.head()

# %% [markdown]
# Step 2: DEFINING VARIABLES
# 
# Survived = 1, Did not Survive = 0 
# Pclass =1,2 or 3,(first class, second class, third class) 
# Sex = male, female 
# SibSp= siblings or spouse
# 
# PassengerId and Ticket # are random values that do not affect survival because they are random but will keep in analysis for now and exclude after checking correlation.

# %% [markdown]
# Step 3: Exploring the Data

# %% [code]
train_data = pd.read_csv(csv_train_path)
train_data.head()

# %% [code]
train_data.shape

# %% [code]
test_data = pd.read_csv(csv_test_path)
test_data.head()

# %% [code]
test_data.shape

# %% [code]
test_df = test_data
train_df = train_data

# %% [markdown]
# Put data into dataframes to easily select columns and rows and go through each factor affecting survival

# %% [code]
print(train_data.columns.values)

# %% [code]
print(train_data.info())

# %% [code]
print(test_data.info())

# %% [code]
train_data.head()

# %% [markdown]
# Step 4: PRE PROCCESS DATA

# %% [code]
train_df.info()

# %% [markdown]
#IDENTIFYING MISSING VALUES
# from the info, we see that age, cabin, and embarked have missing values, age has 177 missing values, cabin has 687 missing values, and embarked has 2 missing values 


# %% [code]
test_df.info()

# %% [markdown]
# from the info we see that age, fare, and cabin have missing values, age has 86 missing values, fare has 1 missing value, and cabin has 327 missing values

# %% [code]
train_df.describe()
#DESCRIPTIVE STATISTICS
#shows the mean, stdev, min, and max of each category
#DATA ANALYSIS
# # On average, 38.38% (approx 38%) of passengers survived based on training data

# %% [code]
men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)

print("% of men who survived:", rate_men)
#approx 19% of men survived
# %% [code]
women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived:", rate_women)
#approx 74% of women survived
# %% [code]
#shows correlation to find useful variables
train_df.corr()
# %% [markdown]
# Passenger ID is weakly correlated (under 10% correlation with every factor) to to the other factors
#fare (26% correlation) and class (34% correlation) have large impacts on survival
#We also see age is correlated mostly with class (37%)
#We also see fare is correlated mostly with class (55%)

# %% [code]
#class and fare affect chances of survival


print(train_df.corr())
# %% [code]
train_data[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)

# Exploratory Data Analysis

# %% [code]
def bar_chart(feature):
    survived=train_data[train_data['Survived']==1][feature].value_counts()
    dead=train_data[train_data['Survived']==0][feature].value_counts()
    df=pd.DataFrame([survived,dead])
    df.index=['Survived','Dead']
    df.plot(kind='bar',stacked=True,figsize=(15,5))


# %% [code]
bar_chart('Sex')
#this chart shows what we already know, more women survive than men 

# %% [markdown]
# Females are much more likely to survive than men

# %% [code]
train_data[["Age", "Survived"]].groupby(['Age'], as_index=False).mean().sort_values(by='Survived', ascending=False)


# %% [code]
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

f,ax=plt.subplots(figsize=(18,8))

sns.violinplot("Sex","Pclass", hue="Survived", data=train_df,split=True,ax=ax)

ax.set_title('Sex and Pclass vs Survived')

ax.set_yticks(range(1,4,1)) 

plt.show()

# %% [markdown]
# This graph shows that both males and females in the 3rd class were more likely to die compared to being in first or second class. The number of females who did not survive in the first class is very low. This graph shows the 2 most highly correlated factors with survival so its an important graph.

# %% [code]
f,ax=plt.subplots(figsize=(20,10))


sns.violinplot("Pclass","Age", hue="Survived", data=train_df,split=True,ax=ax)

ax.set_title('Pclass and Age vs Survived')

ax.set_yticks(range(0,110,10)) 

plt.show()

# %% [markdown]
# There are more kids overall in the second and third class and they have a pretty good survival rate in class 1 and 2. There are not that many passengers over the age of 70 overall.

# %% [code]
train_df

# %% [code]
f,ax=plt.subplots(figsize=(18,8))

sns.violinplot("Sex","Age", hue="Survived", data=train_df,split=True,ax=ax)

ax.set_title('Sex and Age vs Survived')

ax.set_yticks(range(0,110,10)) 

plt.show()

# %% [markdown]
# This graph shows that females are more likely to survive than men overall, and that there were some elderly males who survived and not elderly women.

# %% [markdown]
# Now we have to figure out the missing values for age. The correlation for age with class is the largest (36.92%) as opposed to other factors as shown in the correlation table above.


# %% [code]
sns.factorplot('Embarked','Survived',data=train_df)
fig=plt.gcf() # pyplot. gcf() is primarily used to get the current figure. 
fig.set_size_inches(5,3)
plt.show()

# %% [code]
f,ax=plt.subplots(figsize=(18,8))

sns.violinplot("Embarked","Pclass", hue="Survived", data=train_df,split=True,ax=ax)

ax.set_title('Embarked and Class vs Survived')

ax.set_yticks(range(1,4,1)) 

plt.show()

# %% [markdown]
# This shows that most people who embarked from C survive, with Q being second and S being third. I chose to fill in with C because there are more upper class people from C and the missing values are upper class people.


# %% [code]
FacetGrid = sns.FacetGrid(train_df, size=3, aspect=1.5)

FacetGrid.map(sns.pointplot, 'Pclass', 'Survived', 'Sex')

FacetGrid.add_legend()

# %% [markdown]
# We already know class has correlation with survival. Now its clear that females are more likely to survive in every class compared to males, and both genders are more likely to survive in first class, and then second class, and then third class.

# %% [code]
data1=train_df.copy() 
data1['Family_size'] = data1['SibSp'] + data1['Parch'] +1
# 1 means they are by themselves

data1['Family_size'].value_counts().sort_values(ascending=False)

# %% [code]
bar_chart('Parch')

# %% [code]
#someone who boarded alone is more likely dead than someone who boarded with 2 family members.
#we wont use this in the final analysis because of low correlation with survival
# %% [code]
bar_chart('SibSp')

# %% [markdown]
# By looking at this graph, it is clear that someone with no siblings and or no spouse is more likely to not survive.
#we wont use this in final analysis because of low correlation with survival
# %% [markdown]
# For cabin, there are 687 missing values out of 891 values in the training set. Since 77.1% of the values are missing, this will be excluded from the analysis to avoid generalizations with the data.

# %% [code]
bar_chart('Embarked')

# %% [code]
#Someone who boarded from S is more likely to be dead. Someone who boarded from C is more likely to live.

# %% [code]
bar_chart('Fare')

# %% [markdown]
# checking the survival rate for different fare ranges. People who paid higher fares were more likely to survive.

# %% [code]
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler

#Instead I decided to change it manually into integer values
# %% [markdown]
# Building the Model with Feature Engineering

# %% [code]
train_df.drop('Name',axis=1,inplace=True)
train_df.drop('Ticket',axis=1, inplace=True)
train_df.drop('Cabin',axis=1, inplace=True)
train_df.drop('PassengerId',axis=1, inplace=True)

# %% [code]
test_df.drop('Name',axis=1,inplace=True)
test_df.drop('Ticket',axis=1, inplace=True)
test_df.drop('Cabin',axis=1, inplace=True)

#dropped these values because name, ticket number are random and irrelevant features, and also dropped cabin because correlation is low to survival
# %% [code]
age_by_pclass_sex = train_df.groupby(['Sex', 'Pclass']).median()['Age']

for pclass in range(1, 4):
    for sex in ['female', 'male']:
        print('Median age of Pclass {} {}s: {} '.format(pclass, sex, age_by_pclass_sex[sex][pclass].astype(int)))


train_df['Age'] = train_df.groupby(['Sex', 'Pclass'])['Age'].apply(lambda x: x.fillna(x.median()))
#This was used to fill in the missing values for age based on class as age and class were correlated (37%)
# %% [code]
train_df.info()

# %% [code]
age_by_pclass_sex = test_df.groupby(['Sex', 'Pclass']).median()['Age']

for pclass in range(1, 4):
    for sex in ['female', 'male']:
        print('Median age of Pclass {} {}s: {} '.format(pclass, sex, age_by_pclass_sex[sex][pclass].astype(int)))


test_df['Age'] = test_df.groupby(['Sex', 'Pclass'])['Age'].apply(lambda x: x.fillna(x.median()))
# Filled the missing values of age with the median values of the Sex and Pclass groups
# %% [code]
filter1=train_df['Sex'] == 'male'
male_index=train_df[filter1].index
female_index=train_df[~filter1].index

train_df['Sex'].iloc[male_index] = 0
train_df['Sex'].iloc[female_index] = 1

train_df.corr()

train_df['Sex'] = train_df['Sex'].astype(int)

train_df.info

train_df.info()
#changing sex to an integer to prepare for data analysis
#male=0 and female =1

# %% [code]
test_df['Sex'].drop_duplicates()

filter1=test_df['Sex'] == 'male'
male_index=test_df[filter1].index
female_index=test_df[~filter1].index

test_df['Sex'].iloc[male_index] = 0
test_df['Sex'].iloc[female_index] = 1

test_df.corr()

test_df['Sex'] = test_df['Sex'].astype(int)

test_df.info()
#changing sex to an integer to prepare for data analysis
#male=0 and female =1
# %% [code]
train_df.loc[train_df['Age'] < 15, 'Age'] = 1
train_df.loc[(train_df['Age'] > 15) & (train_df['Age'] <= 25), 'Age'] = 2
train_df.loc[(train_df['Age'] > 25) & (train_df['Age'] <= 35), 'Age'] = 3
train_df.loc[(train_df['Age'] > 35) & (train_df['Age'] <= 65), 'Age'] = 4
train_df.loc[train_df['Age'] > 65, 'Age'] = 5
#by grouping the ages into different categories we can use them for data analysis

# %% [code]
#child=1, young adult=2, adult=3, middle aged=4, old person=5

# %% [code]
train_df.head()

# %% [code]
test_df.loc[test_df['Age'] < 15, 'Age'] = 1
test_df.loc[(test_df['Age'] > 15) & (test_df['Age'] <= 25), 'Age'] = 2
test_df.loc[(test_df['Age'] > 25) & (test_df['Age'] <= 35), 'Age'] = 3
test_df.loc[(test_df['Age'] > 35) & (test_df['Age'] <= 65), 'Age'] = 4
test_df.loc[test_df['Age'] > 65, 'Age'] = 5
#by grouping the ages into different categories we can use them for data analysis
# %% [code]
#child=1, young adult=2, adult=3, middle aged=4, old person=5

# %% [code]
test_df.head()
test_df.info()

# %% [code]
train_df[train_df['Embarked'].isnull()]

# %% [code]
#The 2 missing values are first class women and according to the previous graphs, first class women are more likely to depart from C

# %% [code]
Pclass1 = train_df[train_df['Pclass']==1]['Embarked'].value_counts()
Pclass2 = train_df[train_df['Pclass']==2]['Embarked'].value_counts()
Pclass3 = train_df[train_df['Pclass']==3]['Embarked'].value_counts()
df = pd.DataFrame([Pclass1, Pclass2, Pclass3])
df.index = ['1st class','2nd class', '3rd class']

Pclass1 = test_df[test_df['Pclass']==1]['Embarked'].value_counts()
Pclass2 = test_df[test_df['Pclass']==2]['Embarked'].value_counts()
Pclass3 = test_df[test_df['Pclass']==3]['Embarked'].value_counts()
df = pd.DataFrame([Pclass1, Pclass2, Pclass3])
df.index = ['1st class','2nd class', '3rd class']

train_df['Embarked'] = train_df['Embarked'].fillna('C')
train_df.info()
#I chose to fill the missing embarked value with C as this was the most common place for a first class female.

# %% [code]
embarked_mapping = {"S": 0, "C": 1, "Q": 2}
train_df['Embarked'] = train_df['Embarked'].map(embarked_mapping)
#giving embarked an integer value for data analysis
# %% [code]
embarked_mapping = {"S": 0, "C": 1, "Q": 2}
test_df['Embarked'] = test_df['Embarked'].map(embarked_mapping)
#giving embarked an integer value for data analysis
# %% [code]
train_df.head()

# %% [code]
test_df.info()

# %% [code]
test_df["Fare"].fillna(test_df.groupby("Pclass")["Fare"].transform("median"), inplace=True)
test_df["Fare"].fillna(test_df.groupby("Pclass")["Fare"].transform("median"), inplace=True)
train_df.info()
#Replacing the missing fare values with the median fare values per class
# %% [code]

train_df.loc[train_df['Fare'] <= 15, 'Fare'] = 0
train_df.loc[(train_df['Fare'] > 15) & (train_df['Fare'] <= 35), 'Fare'] = 1
train_df.loc[(train_df['Fare'] > 35) & (train_df['Fare'] <= 85), 'Fare'] = 2
train_df.loc[train_df['Fare'] > 85, 'Fare'] = 3
#changing fare values to categories for data analysis
# %% [code]
test_df.loc[test_df['Fare'] <= 15, 'Fare'] = 0
test_df.loc[(test_df['Fare'] > 15) & (test_df['Fare'] <= 35), 'Fare'] = 1
test_df.loc[(test_df['Fare'] > 35) & (test_df['Fare'] <= 85), 'Fare'] = 2
#changing fare values to categories for data analysis
# %% [code]
features_drop = ['SibSp','Parch']
train_df = train_df.drop(features_drop, axis=1)
test_df = test_df.drop(features_drop, axis=1)

train_data = train_df.drop('Survived', axis=1)
target = train_df['Survived']

train_data.shape, target.shape
#dropping SibSp and Parch because they are not correlated highly with survival compared to other factors.
#however, i still used age which has a low correlation to survival because its highly correlated with class (37%) and class is highly correlated to survival.
# %% [code]
train_df.info()

# %% [code]
#FIT MODELS 
#PARTITION DATA USING KFOLD 
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
k_fold = KFold(n_splits=10, shuffle=True, random_state=0)

# %% [code]
clf = KNeighborsClassifier(n_neighbors = 13)
scoring = 'accuracy'
score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
print(score)

# %% [code]
round(np.mean(score)*100, 2)

# %% [code]
clf = RandomForestClassifier(n_estimators=13)
scoring = 'accuracy'
score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
print(score)

# %% [code]
round(np.mean(score)*100, 2)

# %% [code]
clf = DecisionTreeClassifier()
scoring = 'accuracy'
score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
print(score)

# %% [code]
round(np.mean(score)*100, 2)
# %% [code]
clf = GaussianNB()
scoring = 'accuracy'
score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
print(score)
round(np.mean(score)*100, 2)

# %% [code]
clf = SVC()
scoring = 'accuracy'
score = cross_val_score(clf, train_data, target, cv=k_fold, n_jobs=1, scoring=scoring)
print(score)
round(np.mean(score)*100,2)

test_df

random_forest=RandomForestClassifier(n_estimators=100)
X_train=StandardScaler().fit_transform(train_data)
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
predictions=cross_val_predict(random_forest, X_train, train_df['Survived'])
from sklearn.metrics import f1_score
print(f1_score(train_df['Survived'], predictions))
#The F1 score for random forest classifier is 73%

decision_tree=DecisionTreeClassifier()
X_train=StandardScaler().fit_transform(train_data)
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix
predictions=cross_val_predict(decision_tree, X_train, train_df['Survived'])
from sklearn.metrics import f1_score
print(f1_score(train_df['Survived'], predictions))
#FIT score of 72%, lower than randomforest, but accuracy of this is higher

#DECISION TREE CLASSIFIER HAS THE HIGHEST accuracy score OF 81.84% SO WE WILL USE THIS (although its score is close to the random forest tree, i will go with the one with higher accuracy)
# %% [code]
test_df.info()
train_df.info()

# %% [code]
test_data = test_df.drop("PassengerId", axis=1).copy()

# %% [code]
test_df.info()

# %% [code]
train_df.info()

# %% [code]
clf = DecisionTreeClassifier()
clf.fit(train_data, target)

prediction = clf.predict(test_data)

submission = pd.DataFrame({
        "PassengerId": test_df["PassengerId"],
        "Survived": prediction
    })

# %% [code]
submission.to_csv('submission.csv', index=False)

# %% [code]
submission = pd.read_csv('submission.csv')
print(submission.head())
print(submission)
# %% [code]

from sklearn.metrics import roc_auc_score
decision_tree=DecisionTreeClassifier()
X_train=StandardScaler().fit_transform(train_data)
predictions=cross_val_predict(decision_tree, X_train, train_df['Survived'])
print(roc_auc_score(train_df['Survived'], predictions))
# the AUC score of my decision tree is 77.5%
