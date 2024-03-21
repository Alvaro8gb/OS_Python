from sklearn import datasets # pip install scikit-learn
import pandas as pd # pip install pandas
import threading
 
dataset = datasets.load_breast_cancer()
 
# Convert the data to a Pandas DataFrame
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target

#print(dataset.DESCR)

print(dataset.feature_names)
print(df['radius error'][0]) # Acces to row 0

df_numeric = df.select_dtypes(include=['number'])

print(df_numeric.columns)

