import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
#from sklearn.metrics import accuracy_score

def red_wine(test_frame):
    # TRAINING THE MODEL - RED WINE
    red_wine = pd.read_csv('winequality-red.csv', delimiter=";")
    #train_X = red_wine.drop(labels='quality',axis=1)
    #train_y = red_wine['quality']

    # Split categories:
    # 1 - 4  --> POOR WINE    --> Category 0
    # 5 - 6  --> AVERAGE WINE --> Category 1
    # 7 - 10 --> GREAT WINE   --> Category 2
    bins = [1,4,6,10]
    quality_labels = [0,1,2]
    red_wine['quality_categorical'] = pd.cut(red_wine['quality'], bins=bins, labels=quality_labels, include_lowest=True)


    # Input features - all columns, except the two related to quality
    train_X = red_wine.drop(['quality', 'quality_categorical'], axis=1)
    # Output feature - categorical quality column
    train_y = red_wine['quality_categorical']

    # Selecting the model to fit the training set
    model = RandomForestClassifier(n_estimators=30,min_samples_leaf=30, random_state=0, n_jobs=1)
    model.fit(train_X, train_y)

    # Making predictions on new data set - supplied by the user
    prediction = model.predict(test_frame)
    print("Predicted quality for wine is: " + str(prediction))
    #print(prediction)
    print("[0] -- Poor Wine\n[1] -- Average Wine\n[2] -- Great Wine")


def white_wine(test_frame):
    '''Yet to fill'''