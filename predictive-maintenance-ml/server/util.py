import pickle
import json
import numpy as np


__type = None
__data_columns = None
__model = None

def get_estimated_failure(type, air_T, process_T, rotational_speed, torque, tool_wear):
    try:
         type_index = __data_columns.index(type.lower())
    except:
         type_index = -1
    x = np.zeros(len(__data_columns))
    x[2]= air_T
    x[3]= process_T
    x[4]= rotational_speed
    x[5]= torque
    x[6]= tool_wear
    if type_index >= 0:
         x[type_index]=1
    return __model.predict([x])[0]

def load_saved_artifacts():
    print("loadig saved artifacts...start")
    global __data_columns
    global __type
    global __model
    with open("./artifacts/columns.json","r") as f:
           __data_columns = json.load(f)['data_columns']
    
    if __model is None:
        with open("./artifacts/failure_prediction.pickle","rb") as f:
             __model = pickle.load(f)
print("loading saved artifacts... done")
def get_dat_columns():
     return __data_columns
if __name__ == '__main__':
     load_saved_artifacts()