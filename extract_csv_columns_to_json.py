import pandas as pd
import numpy as np
import json
import config as cfg

llm = cfg.llm

df = pd.read_csv('Crime_Data_from_2020_to_Present.csv')

df = df.replace(np.nan,0)

dict_ = {}
for c in df.columns:
# storing the column name, data type and content
  dict_[c] = {'column_name':c,'type':str(type(df[c].iloc[0]))}
# After looping storing the information as a json dump that can be loaded 
with open("dataframe.json", "w") as fp:
    json.dump(dict_ ,fp) 

documents = json.loads(input_file='dataframe.json')
