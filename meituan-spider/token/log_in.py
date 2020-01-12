import get_token
import requests
import urllib

def log_in(pagen):
    #Ä£ÄâµÇÂ¼
    token = get_token.encode_token(pagen)
    originUrl = 'https://wh.meituan.com/meishi/pn%s/' % pagen

    #URL±àÂë
    token = urllib.parse.quote(token)
    token = token.replace('/', '%2F')
    originUrl = urllib.parse.quote(token)
    originUrl = originUrl.replace('/', '%2F')

    url = 'https://wh.meituan.com/meishi/api/poi/getPoiList?' + \
          'cityName=%%E6%%AD%%A6%%E6%%B1%%89' \
          '&cateId=0'  \
          '&areaId=0'  \
          '&sort=' \
          '&dinnerCountAttrId=' \
          '&page=%s' % pagen + \
          '&userId=' \
          '&uuid=9c16fe8c-e338-4436-9c24-eba6c75b61eb' \
          '&platform=1' \
          '&partner=126' \
          '&originUrl=' + originUrl + \
          '&riskLevel=1' \
          '&optimusCode=10' \
          '&_token=' + token

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    accpet = '*/*'
    accept_encoding = 'gzip, deflate, br'
    accpet_language = 'zh-CN,zh;q=0.9'
    connection = 'keep-alive'
    host = 'wh.meituan.com'
    referer = 'https://wh.meituan.com/meishi/pn%s/' % pagen

    headers = { 'User-Agent':user_agent,
                'Accept':accpet,
                'Accept-Encoding':accept_encoding,
                'Accept-Language':accpet_language,
                'Connection':connection,
                'Host': host,
                'Referer':referer
              }
    page = requests.get(url = url, headers = headers, allow_redirects = False)
    return page

log_in(1)
