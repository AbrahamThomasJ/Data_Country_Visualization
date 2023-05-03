import utils # The utils module contains the functions for data processing.
import read_csv #the read module contains the function for reading the csv file.
import charts # In the charts module you will find the functions to process the graphs and display them as a graphical interface.


def get_data_by_country():
    # data is read from the csv file
    data = read_csv.read_csv('data.csv')
    country = input('Type Country => ')
    result = utils.population_by_country(data,country)
    
    if len(result) > 0:
       country = result[0]
        
       labels, values = utils.population_country(country)
       charts.generate_bar_chart(country['Country/Territory'],labels,values)


def get_data_by_percentage(all_or_continent):
    # data is read from the csv file
    data = read_csv.read_csv('data.csv')

    continent = ['North America','South America','Asia','Europe','Africa','Oceania']

    if int(all_or_continent) > 2: 
        data = list(filter(lambda item : item['Continent'] == continent[int(all_or_continent)-3], data))
   
    country_labels, country_values = utils.world_percentage(data)
    
    charts.generate_pie_chart(continent[int(all_or_continent)-3],country_labels,country_values)

  

if __name__ == '__main__':

    # We ask the user what data he/she wants to obtain
    while True:
        option = input('Que datos quieres observar?\n 1. World Population of one country.\n 2. Population Percentage of all countries.\n 3. North American population percentage.\n 4. South America population percentage.\n 5. Asian population percentage.\n 6. Europe population percentage.\n 7. Africa population percentage\n 8. Oceania population percentage\n: ').lower()
        
        if option == 'c': break
    # Depending on the option, we will call the respective function to obtain the data
        if option == '1' or option == 'world population of one country':
            get_data_by_country()
            
        elif option == '2' or option == 'world population percentage':
            get_data_by_percentage(option)
            
        elif option == '3' or option == 'north america population percentage ':
            get_data_by_percentage(option)
            
        elif option == '4' or option == 'south america population percentage':
            get_data_by_percentage(option)
            
        elif option == '5' or option == 'asian population percentage by ':
            get_data_by_percentage(option)
            
            
        elif option == '6' or option == 'europe population percentage by ':
            get_data_by_percentage(option)
            
        elif option == '7' or option == 'africa population percentage by ':
            get_data_by_percentage(option)
            
        elif option == '8' or option == 'oceania population percentage by ':
            get_data_by_percentage(option)
            
        else:
            print('\n"" You must choose one of the options or leave by pressing "c" ""\n')
            
