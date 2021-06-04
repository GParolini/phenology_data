#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import os
from pathlib import Path
import glob



cwd =os.getcwd()
p_cwd = Path(cwd).parent.absolute()
data_dir = os.path.join(p_cwd, "data","de_phen_data")
data_dir_list = glob.glob(data_dir + '/*.csv')

phen_data = pd.DataFrame()
for file in data_dir_list:
    x = pd.read_csv(file, sep=';', low_memory=False)
    phen_data = pd.concat([phen_data,x],axis=0)

print(phen_data.head())

phen_data.to_csv(os.path.join(p_cwd, "data", "phen_data.csv"), index=False)





