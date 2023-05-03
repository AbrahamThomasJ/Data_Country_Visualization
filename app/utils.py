import re

# This function returns the population of a country in the form of a key value.
def population_country(data):
    regex = re.compile('^\d+ Population$')
    
    fl = {re.findall('\d+', k)[0]: int(v) for k, v in data.items() if regex.match(k)} 
    
    
    labels = fl.keys()
    values = fl.values()
    
    return labels,values


# this function returns the percentage or percentages of the requested country or countries.
def world_percentage(data):
    wpp = {}
    for i in data:
        for k,v in i.items():
            if k == 'World Population Percentage':
                name_country = i['Country/Territory']
                wpp[f'{name_country} %'] = v
    return wpp.keys(),wpp.values()                    


# This function returns the data of the searched country.
def population_by_country(data,country):
    result = list(filter(lambda items: items['Country/Territory'] == country,data))
    return result



    
