# Modify the above program/function to take the starting and ending years as inputs from the user or from the command line.


import pandas as pd

def population_high_low_grwth_per(strt_year, end_year):
    try:
        df = pd.read_csv("Programming Exercise Data - World Population Data.csv")
        
        li_values= []
        len_year = len(df[strt_year])
        
        for indx in range(0, len_year):
            result = 100*((df[end_year][indx] - df[strt_year][indx])/df[strt_year][indx])
            li_values.append(result)
        
        # print("list of growth percentage: ",li_values)
        indx_val_max = li_values.index(max(li_values))
        indx_val_min = li_values.index(min(li_values))
            
        return df['Country Name'][indx_val_max],li_values[indx_val_max], df['Country Name'][indx_val_min], li_values[indx_val_min]

    except Exception as e:
        print('Error in the population_high_low function'+str(e.args))
        exit(1)
        
if __name__ == "__main__":
    try:
        inp_year_strt = input("Enter the strt year which is smaller than end year : ")
        print("The first value entered for the start year is : ",inp_year_strt)
        inp_year_end = input("Enter the end year: ")
        print("The second value entered for the end year is : ",inp_year_end)
        cntry_high_pop_grwth_per,grwth_per_high,cntry_low_pop_grwth_per,grwth_per_low =  population_high_low_grwth_per(inp_year_strt, inp_year_end)
        print('High growth rate country is ',cntry_high_pop_grwth_per,' with highest growth percentage of ',grwth_per_high,' in the given year')
        print('Low growth rate country is ',cntry_low_pop_grwth_per,' with lowest growth percentage of ',grwth_per_low,' in the given year')
    except Exception as e:
        print('Error in the main function'+str(e.args))
        exit(1)
        
        
# =========================================


        
            
            
        
        