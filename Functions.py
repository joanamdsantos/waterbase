import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

schema = pd.read_csv(filepath_or_buffer='Waterbase_v2018_1_T_WISE4_DisaggregatedData_Schema.csv')

def get_description(column_name, schema=schema):
    '''
    INPUT - schema - pandas dataframe with the schema of the developers survey
            column_name - string - the name of the column you would like to know about
    OUTPUT - 
            desc - string - the description of the column
    '''
    desc = list(schema[schema.Column == column_name]['Question'])[0]
    return desc


