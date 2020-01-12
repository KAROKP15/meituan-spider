import pandas as pd
import jieba
from sklearn.model_selection import train_test_split
# 文本特征提取
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import classification_report
from get_id import get_id

# 根据每条评论的评分确定其情感标签
def make_label(star):
    if star >= 30:
        return 1
    else:
        return 0

# 对每条评论进行中文分词确定其分词标签
def chinese_word_cut(comment):
    return " ".join(jieba.cut(comment))

def Bayes(id_list):
    data = pd.read_csv('/Users/karo/Desktop/crawl_task/comments/' + id_list[0] + '.csv')
    data['cut_comment'] = data.comment.apply(chinese_word_cut)
    id_list = id_list[1:]
    for id in id_list:
        try:
            df = pd.read_csv('/Users/karo/Desktop/crawl_task/comments/' + id + '.csv')
        except pd.errors.ParserError:
            continue
        else:
            try:
                df['cut_comment'] = df.comment.apply(chinese_word_cut)
            except AttributeError:
                df['cut_comment'] = ''
            else:
                data = pd.concat([data, df], ignore_index = True)
            #data['cut_comment'] = data.comment.apply(chinese_word_cut)

    #print(data)
    # 添加new type感情栏
    data['sentiment'] = data.star.apply(make_label)
    # 添加new type分词栏
    #data['cut_comment'] = data.comment.apply(chinese_word_cut)

    # 划分数据集
    X = data['cut_comment']
    Y = data['sentiment']

    # 按照Y特征（sentiment）将X进行8:2划分为训练集和测试集
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)
    vec = CountVectorizer()
    X_train = vec.fit_transform(X_train)
    X_test = vec.transform(X_test)

    mnb = MultinomialNB()
    mnb.fit(X_train, Y_train)
    Y_predict = mnb.predict(X_test)
    print(Y_predict)

    print('准确率：', mnb.score(X_test, Y_test))

    print(classification_report(Y_test, Y_predict))

if __name__ == '__main__':
    id_list = get_id('data.csv')[1:]
    Bayes(id_list)
