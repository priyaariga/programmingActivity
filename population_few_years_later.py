# Write a program/function to caclulate a country’s population a few years from now. Take country name and number of years as inputs from user or from command line. Use the average growth rate in the last x years as the growth rate for the period. Let x be a constant defined in the program/function or in a property file. 


import pandas as pd

def population_high_low_grwth_per(cntry_name, inp_year):
    try:
        df = pd.read_csv("Programming Exercise Data - World Population Data.csv")
        
        li_values= list(df['Country Name'])
        indx_country = li_values.index(cntry_name)
        print("Index of the country is: ",indx_country)
        
        x= 10
        population_2020 = df['2020'][indx_country]
        print("population_2020: ", population_2020)
        
        population_x = df[str(2020-x)][indx_country]
        print("population_x: ", population_x)
        
        x_year_per = 100*((population_2020 - population_x)/population_x)
        print("x_year_per: ",x_year_per)
        
        one_year_per = (x_year_per)/x
        print("one_year_per: ", one_year_per)
        
        inp_year_per = (one_year_per) * int(inp_year)
        print("inp_year_per: ",inp_year_per)
        
        inp_year_population = int(((inp_year_per * population_2020) / 100) + population_2020)
        print("inp_year_population: ", inp_year_population)
        
        return inp_year_population

    except Exception as e:
        print('Error in the population_high_low function'+str(e.args))
        exit(1)
        
if __name__ == "__main__":
    try:
        inp_cntry_name = input("Enter the country name: ")
        print("The country name entered is : ",inp_cntry_name)
        inp_no_years = input("Enter the number of years: ")
        print("Number of years  entered is : ",inp_no_years)
        population_inp_year = population_high_low_grwth_per(inp_cntry_name, inp_no_years)
        print('POpulation of the given country in '+inp_no_years+' from now: ', population_inp_year)
    except Exception as e:
        print('Error in the main function'+str(e.args))
        exit(1)
        
        
# =========================================


        
            
            
        
        