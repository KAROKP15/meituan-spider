import csv

def get_id(filename):
    extra = '/Users/karo/Desktop/crawl_task/'
    filename = extra + filename
    with open (filename, 'r') as f_obj:
        reader = csv.reader(f_obj)
        id_list = [row[0] for row in reader]
        for i in range(0,len(id_list)):
            end = id_list[i].index('"')
            id_list[i] = id_list[i][:end-1]
    return id_list
