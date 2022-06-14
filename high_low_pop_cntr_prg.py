# Write a program/function to find the country/region with the highest and lowest population in a given year. Take the year as input from the user or from the command line. 

import pandas as pd

def population_high_low(year):
    try:
        df = pd.read_csv("Programming Exercise Data - World Population Data.csv")
        
        indx_high_pop_cntry= 0
        indx_low_pop_cntry= 0
        
        len_year = len(df[year])
        li_year = list(df[year])
        
        for indx in range(1,len_year):
            if li_year[indx]> li_year[indx_high_pop_cntry]:
                indx_high_pop_cntry = indx
            if li_year[indx]<li_year[indx_low_pop_cntry]:
                indx_low_pop_cntry = indx
                
        return df['Country Name'][indx_high_pop_cntry],li_year[indx_high_pop_cntry],df['Country Name'][indx_low_pop_cntry],li_year[indx_low_pop_cntry]
    
    except Exception as e:
        print('Error in the population_high_low function'+str(e.args))
        exit(1)
        
if __name__ == "__main__":
    try:
        inp_year = input("Enter the year: ")
        print("The value entered for the year is : ",inp_year)
        cntry_high_pop,high_pop,cntry_low_pop,low_pop = population_high_low(inp_year)
        print('Highest populated country is ',cntry_high_pop,' with population of ',high_pop)
        print('Lowest populated country is ', cntry_low_pop ,' with population of ', low_pop)
    except Exception as e:
        print('Error in the main function'+str(e.args))
        exit(1)
        
        
# =========================================

# df['Country Name'][df[year].argmax()]
# df['Country Name'][df[year].argmin()]
        
            
            
        
        