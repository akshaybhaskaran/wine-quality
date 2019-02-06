from winePred import red_wine
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
if wine_type == 'R' or 'r':
     red_wine(test_frame)
else:
    white_wine(test_frame) -- yet to write this code


# frame = pd.DataFrame(np.array(data).reshape(3,len(data[0])))'''




'''
Useful for testing
data = [[10.3,0.32,0.45,6.4,0.073,5,13,0.9976,3.23,0.82,12.6], ---> [2]
        [7.8,0.57,0.31,1.8,0.069,26,120,0.99625,3.29,0.53,9.3], ---> [1]
        [6.9,1.09,0.06,2.1,0.061,12,31,0.9948,3.51,0.43,11.4]] ---> [0]
'''
