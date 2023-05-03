import csv


def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile,delimiter=',') 
        
        header = next(reader) 
        
        
        data_list = []
        for i in reader:
            iterable = list(zip(header,i))
            dict_country = {k:v for k,v in iterable}
            data_list.append(dict_country)

        return data_list    
         

if __name__ == '__main__':
    pass
