# Write a program/function to find the country/region with the highest and lowest population growth percentage from 1960 to 2020. 
# Formula: 100 * (2020 population - 1960 population) / 1960 population


import pandas as pd

def population_high_low_grwth_per():
    try:
        df = pd.read_csv("Programming Exercise Data - World Population Data.csv")
        
        li_values= []
        len_year = len(df['1960'])
        
        
        for indx in range(0, len_year):
            result = 100*((df['2020'][indx] - df['1960'][indx])/df['1960'][indx])
            li_values.append(result)
            
        indx_val_max = li_values.index(max(li_values))
        indx_val_min = li_values.index(min(li_values))
            
        return df['Country Name'][indx_val_max], df['Country Name'][indx_val_min]

    except Exception as e:
        print('Error in the population_high_low function'+str(e.args))
        exit(1)
        
if __name__ == "__main__":
    try:
        cntry_high_pop_grwth_per,cntry_low_pop_grwth_per =  population_high_low_grwth_per()
        print('High growth rate country ',cntry_high_pop_grwth_per)
        print('Low growth rate country: ',cntry_low_pop_grwth_per)
    except Exception as e:
        print('Error in the main function'+str(e.args))
        exit(1)
        
        
# =========================================


        
            
            
        
        