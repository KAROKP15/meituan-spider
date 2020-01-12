# get each store's comments' wordcloud in ''

from wordcloud import WordCloud
import os
import jieba

def chinese_jieba(txtfile):
    # seperate txt into list
    wordlist_jieba = jieba.cut(txtfile)
    # joint list into string disconnected by space
    txt_jieba = " ".join(wordlist_jieba)
    return txt_jieba

def get_wordcloud(id):
    filename = '/Users/karo/Desktop/crawl_task/comment_txt/' + id + '.txt'
    stopwords = []

    with open (filename) as f_obj:
        txt = f_obj.read()
        txt = chinese_jieba(txt)
        try:
            wordcloud = WordCloud(font_path = 'STHeiti Medium.ttc',
                                  background_color = 'white',
                                  max_words = 30,
                                  max_font_size = 60,
                                  stopwords = stopwords
                                  ).generate(txt)
        except ValueError:
            return
        else:
            # image = wordcloud.to_image()
            # image.show()
            wordcloud.to_file('comment_wordcloud/' + id + '.jpg')
