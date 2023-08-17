import os
import pandas as pd
import numpy as np
import glob

input = 'Input//'
output = 'Output//'
rawdata = 'Input//Rawdata//'
adjust_rawdata = 'Input//Adjust_rawdata//'
# os.mkdir(input)
# os.mkdir(output)
# os.mkdir(rawdata)
# os.mkdir(adjust_rawdata)

def r_data():
        rdata = glob.glob(rawdata+"*.xlsx")
        df_list = []
        for f in rdata:
                df = pd.read_excel(f)
                df_list.append(df)
        A_data = pd.concat(df_list)
        A_data.drop_duplicates(subset=['appl No','bslevel Credit'],inplace=True)
        A_data.reset_index(drop=True,inplace=True) 
        A_data.drop(columns=['Row No'],inplace=True)
        return A_data

os.chdir("D:/630039/test_Dev_A-score")
df = r_data()
# df.to_csv(adjust_rawdata+'rawdata.csv',encoding='TIS-620')