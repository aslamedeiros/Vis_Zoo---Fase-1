# imports 
import numpy as np
import pandas as pd
from collections import defaultdict


# function to treat Persons Names
def treat_names(name, pos='first'):
    '''
    Treat names keeping NaN as such.
    
    Arguments: 
        - name (str): name to be treated. 
        - pos (str): name position. One of ['first', 'last']
    '''
    if type(name) == str and pos == 'first':     # first name
        
        if len(name.split(' ')) > 1:             # treats composite names (+ 1 name)
            return str(name).strip().split(' ')[0].capitalize()
        else:
            return str(name).strip().capitalize()
    
    elif type(name) == str and pos == 'last':    # last name
        
        if len(name.split(' ')) > 1:             # treats composite last name (+ 1 surname)
            return str(name).strip().split(' ')[-1].capitalize()
        else:
            return str(name).strip().capitalize()   
    else:
        return name
    

# function to treat taxonomy columns
def treat_taxon_columns(df, columns, inplace=True):
    temp = df[columns].copy()
    
    if inplace:
        for col in columns:
            print(f'Adjusting column {col}')
            
            if 'especie' in col.lower():
                df[col] = df[col].apply(lambda x:str(x).lower().strip())
            else:
                df[col] = df[col].apply(lambda x:str(x).lower().strip().capitalize())
                
        return None
    else:
        for col in columns:
            print(f'Adjusting column {col}')
            
            if 'especie' in col.lower():
                temp[col] = temp[col].apply(lambda x:str(x).lower().strip())
            else:
                temp[col] = temp[col].apply(lambda x:str(x).lower().strip().capitalize())
                
        return temp    

    
# trying to catch year from string "dd/mm/YYYY"
def catch_year(row):
    if not str(row).find('/')==-1:
        dates_values = str(row).split("/")
        year = int(dates_values[-1])
        month = int(dates_values[1])
        return year
    else:
        return np.NaN
    
    
def str_with_nan2int(string):
    if not np.isnan(string):
        return int(string)
    else:
        return np.NAN