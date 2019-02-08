from winePred import red_wine
from winePred import white_wine
import pandas as pd
import numpy as np

print("\n---WINE QUALITY PREDICTOR---\n")
test_list = list()


wine_type = raw_input(str("Please select the type of wine ([R]ed or [W]hite): "))
fx_acd = test_list.append(raw_input("Fixed acidity: "))
vol_acd = test_list.append(raw_input("Volatile acidity: "))
ctrc_acd = test_list.append(raw_input("Citric acid: "))
res_sgr = test_list.append(raw_input("Residual sugar: "))
chlr = test_list.append(raw_input("Chlorides: "))
f_slfr = test_list.append(raw_input("Free sulfur dioxide: "))
t_slfr = test_list.append(raw_input("Total sulfur dioxide: "))
dsty = test_list.append(raw_input("Density: "))
pH = test_list.append(raw_input("pH value: "))
slpht = test_list.append(raw_input("Sulphates: "))
alc = test_list.append(raw_input("Alcohol volume: "))


test_frame = pd.DataFrame(np.array(test_list).reshape(1,len(test_list)))
if wine_type == "R":
    print(" --- RED WINE --- ")
    red_wine(test_frame)
elif wine_type == "W":
    print(" --- WHITE WINE --- ")
    white_wine(test_frame) 






'''
Useful for testing RED
data = [[10.3,0.32,0.45,6.4,0.073,5,13,0.9976,3.23,0.82,12.6], ---> [2]
        [7.8,0.57,0.31,1.8,0.069,26,120,0.99625,3.29,0.53,9.3], ---> [1]
        [6.9,1.09,0.06,2.1,0.061,12,31,0.9948,3.51,0.43,11.4]] ---> [0]

Useful for testing WHITE
data = [[7.2,0.43,0.24,6.7,0.058,40,163,0.995,3.2,0.41,9.9], -- [1]
        [5,0.55,0.14,8.3,0.032,35,164,0.9918,3.53,0.51,12.5], -- [2]
        [6.9,0.39,0.4,4.6,0.022,5,19,0.9915,3.31,0.37,12.6]] -- [0]

frame = pd.DataFrame(np.array(data).reshape(3,len(data[0])))'''

