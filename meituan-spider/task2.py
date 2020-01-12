# save each store's comment infomation in 'poiId.csv'

from log_in import log_in, log_in2
from get_id import get_id
from get_wordcloud import get_wordcloud
import urllib
import json
import csv
import codecs
import pandas as pd

def transUrl(originUrl):
    originUrl = urllib.parse.quote(originUrl)
    originUrl = originUrl.replace('/','%2F')
    return originUrl

def getUrl(uuid, originUrl, id, pageSize):
    originUrl = transUrl(originUrl)
    url = 'https://www.meituan.com/meishi/api/poi/getMerchantComment?' \
          'uuid' + uuid + \
          '&platform=1' \
          '&partner=126' \
          '&originUrl=' + originUrl + \
          '&riskLevel=1' \
          '&optimusCode=10' \
          '&id=' + str(id) + \
          '&userId=' \
          '&offset=0' \
          '&pageSize=10' \
          '&sortType=1'
    return url

def get_comment(page):
    # get comment info
    # saved in json file
    data = page.json()['data']
    filename = 'comment.json'
    with open (filename, 'w') as f_obj:
        json.dump(data, f_obj, ensure_ascii = False)
        f_obj.close()

def trans(path, cpath):
    # transform data from json to csv
    extra = '/Users/karo/Desktop/crawl_task/'
    jsonData = codecs.open(path+'.json', 'rb+', encoding = 'utf-8')
    data = json.load(jsonData)
    data = data['comments']

    csvpath = extra + 'comments/' + cpath + '.csv'
    comment_list = []
    star_list = []
    if data != None:
        for item in data:
            comment_list.append(item['comment'])
            star_list.append(item['star'])
        dataframe = pd.DataFrame({'comment':comment_list, 'star':star_list})
        dataframe.to_csv(csvpath, index=False, sep=',')

    jsonData.close()

def trans_txt(path, cpath):
    # save comments in txt
    extra = '/Users/karo/Desktop/crawl_task/'
    jsonData = codecs.open(extra + path + '.json','rb+', encoding = 'utf-8')
    data = json.load(jsonData)
    data = data['comments']

    txtfile = open(extra + 'comment_txt/' + cpath + '.txt', 'a', newline = '', encoding = 'utf-8')

    if data != None:
        for item in data:
            txtfile.write(item['comment'])
            txtfile.write('\n')

    jsonData.close()
    txtfile.close()


if __name__ == '__main__':
    pageSize = 10
    uuid = '8c0098e3-0781-4329-b0fd-3c3137cb9d93'
    page_list = []
    id_list = get_id('data.csv')
    for i in range(1, len(id_list)):
        print(i)
        originUrl = 'https://www.meituan.com/meishi/' + str(id_list[i]) + '/'
        url = getUrl(uuid, originUrl, id_list[i], pageSize)
        page = log_in2(url)
        get_comment(page)
        trans('comment', str(id_list[i]))
        #trans_txt('comment', str(id_list[i]))
        #get_wordcloud(id_list[i])
    print('Save comments into csv file successfully.')
