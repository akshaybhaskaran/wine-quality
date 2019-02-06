import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# TRAINING THE MODEL - RED WINE
red_wine = pd.read_csv('winequality-red.csv', delimiter=";")
#train_X = red_wine.drop(labels='quality',axis=1)
#train_y = red_wine['quality']

#       Split categories:
#       1 - 4  --> POOR WINE    --> Category 0
#       5 - 6  --> AVERAGE WINE --> Category 1
#       7 - 10 --> GREAT WINE   --> Category 2
bins = [1,4,6,10]
quality_labels = [0,1,2]
red_wine['quality_categorical'] = pd.cut(red_wine['quality'], bins=bins, labels=quality_labels, include_lowest=True)


# Input features - all columns, except the two related to quality
input_features = red_wine.drop(['quality', 'quality_categorical'], axis=1)
# Output feature - categorical quality column
output_features = red_wine['quality_categorical']

# Splitting the data into training and testing sets
train_X, test_X, train_y, test_y = train_test_split(input_features, output_features, test_size=0.2, random_state=0)
print(train_X.shape)

model = RandomForestClassifier(n_estimators=30,min_samples_leaf=30,
                               random_state=0, n_jobs=1)
model.fit(train_X, train_y)




frame = pd.DataFrame(np.array(data).reshape(3,len(data[0])))

prediction = model.predict(frame)

print(prediction)


#accuracy = accuracy_score(test_y, prediction)
#print("Accuracy: {:.2f}".format(accuracy*100))
