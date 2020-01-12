from datetime import datetime
import zlib
import base64

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
headers = {'User-Agent':user_agent}

def decode_token(token):
    # base64解码
    token_decode = base64.b64decode(token.encode())
    # 二进制解压
    token_string = zlib.decompress(token_decode)
    return token_string

def encode_token(pagen):
    # ts是token的时间戳
    ts = int(datetime.now().timestamp()*1000)
    token_dict = {
        "rId":100900,
        "ver":"1.0.6",
        "ts":ts,
        "cts":ts + 100 * 1000,
        "brVD":[150,600],
        "brR":[[1280,720],[1280,680],24,24],
        "bI":["https://wh.meituan.com/meishi/pn%s/" % pagen, "https://wh.meituan.com/meishi/"],
        "mT":[],
        "kT":[],
        "aT":[],
        "tT":[],
        "aM":[],
        "sign":"eJwljTkOwjAQRe9C4S5kxSySC0SFhOg4gOMMZERsR+MxiCNwEToKLpVzYEH1n77+MtMEet+pQhjN8Afkx1FbUNP7NX2eokPngHY+Ot4yU8oIPzLaGHa+A1UWwhNe0J1oUD3zGDZ5fu/nFpCjdnPjbZ449JiLUV9SIQlxmlRlJcU4aD57sskmDNcD3GBIHDyxEjHA7y9G7NTalPIMK5NBXa+ypqlltjZVk0GrpVkuWllCO/sCYLNIrQ=="
    }
    encode = str(token_dict).encode()
    compress = zlib.compress(encode)
    b_encode = base64.b64encode(compress)
    token = str(b_encode, encoding = 'utf-8')
    token = str(decode_token(token))
    token = token.replace('\"', '-') \
                 .replace('\'', '\"') \
                 .replace('-', '\'') \
                 .replace(' ','')
    length = len(token)
    token = token[2:length-1]
    encode = token.encode()
    compress = zlib.compress(encode)
    b_encode = base64.b64encode(compress)
    token = str(b_encode, encoding = 'utf-8')
    return token

if __name__ == '__main__':
    token = [
        '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'
        ]
    for i in range(0, len(token)):
        temp = decode_token(token[i])
        print(temp)
