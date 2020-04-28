import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

schema = pd.read_csv(filepath_or_buffer='Waterbase_v2018_1_T_WISE4_DisaggregatedData_Schema.csv')

def get_description(column_name, schema=schema):
    '''
    INPUT:
        schema - pandas dataframe with the schema of the developers survey
        column_name - string - the name of the column you would like to know about
    OUTPUT:
        desc - string - the description of the column
    '''
    desc = list(schema[schema.Column == column_name]['Question'])[0]
    return desc


def categorical_profile(category_list, top_categ, normalize=True)
    '''
    INPUT:
        category_list - list of categorical variables to profile
        top_categ - top number of categories to show
        normalize - False to include Nulls or NAN
    OUTPUT:
        pandas dataframe with the list of categorical variables and respective percentage
            for each category in ascending order with top10 categories if more than 10
    '''
    # Create an empty DataFrame for the profile table
    profile = pd.DataFrame()
    
    # Create a DataFrame with the percentage for each category 
    for i in catg:
        if normalize=True:
            catg_perc= df[i].value_counts(normalize=True).sort_values(ascending=False)*100 # Relative, No nulls
        #catg_perc= df[i].value_counts().sort_values(ascending=False)/df.shape[0]*100 # Overall
        else
            catg_perc= df[i].value_counts().sort_values(ascending=False)

        # Select the top in categories to display
        catg_top = catg_perc[:top_categ].sort_values(ascending=False)
        catg_topi = catg_top.index
        

        #Create a dataframe with multiple index:
        catg_list = [i]*10
        tuples = list(zip(catg_list, catg_topi))
        catg_df = pd.DataFrame({'Percentage(%)' : catg_top.values}, 
                               index = pd.MultiIndex.from_tuples(tuples, names=['Group', 'Sub-Group']))
        

        profile = profile.append(catg_df).round(2)
    
    return profile