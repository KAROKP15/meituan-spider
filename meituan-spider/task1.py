# save 120 stores' infomation in data.csv

from log_in import log_in
import csv
import json
import codecs

def trans(path):
    #transform data from json to csv
    jsonData = codecs.open(path+'.json', 'r+', 'utf-8')
    datalist = json.load(jsonData)

    csvfile = open(path+'.csv', 'a', newline = '', encoding = 'utf-8')
    writer = csv.writer(csvfile, delimiter = '\t', quoting = csv.QUOTE_ALL)

    # keys = ['poiId', 'title', 'avgScore', 'allCommentNum', 'address', 'avgPrice']
    # writer.writerow(keys)
    for item in datalist:
        list = [item['poiId'], item['title'], item['avgScore'], \
                item['allCommentNum'], item['address'], item['avgPrice']]
        writer.writerow(list)

    jsonData.close()
    csvfile.close()

if __name__ == '__main__':

    page = log_in()
    data = page.json()['data']['poiInfos']
    filename = 'data.json'

    with open (filename, 'w') as f_obj:
        json.dump(data, f_obj, ensure_ascii = False)
        f_obj.close()

    print('Save data into json file successfully!')

    trans('data')
