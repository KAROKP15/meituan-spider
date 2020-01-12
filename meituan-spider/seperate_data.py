# 将文本分类数据集分为训练集和测试集

from queue import Queue
from func_tools import check_dir_exists
import glob
import os
import random
import shutil

THREADLOCK = Lock()

def copyfile(q):
    files_list = []
    train_list = []
    test_list = []
    while not q.empty():
        # divodd表示划分训练集与测试集的比例
        full_folder, train, test, divodd = q.get()
        # 获取各个文件的相对路径，保存在列表中
        files_list.append(full_folder)
        train_list.append(train)
        test_list.append(test)

    filenum = len(files_list)
    testnum = int(filenum * divodd)
    testls = random.sample(list(range(filenum)), testnum)

    for i in range(filenum):
        if i in testls:
            # 复制文件的内容以及权限
            shutil.copy(files_list[i], os.path.join(test_list[i], os.path.basename(files_list[i])))
        else:
            shutil.copy(files_list[i], os.path.join(train_list[i], os.path.basename(files_list[i])))

def data_divi(from_dir, to_dir, divodd = 0.2):
    train_folder = os.path.join(to_dir, "train")
    test_folder = os.path.join(to_dir, "test")
    check_dir_exists(train_folder)
    check_dir_exists(test_folder)

    q = Queue()

    for basefolder in os.listdir(from_dir):
        if basefolder.startswith('.DS'):
            continue
        full_folder = os.path.join(from_dir, basefolder)
        train = os.path.join(train_folder, basefolder)
        check_dir_exists(train)
        test = os.path.join(test_folder, basefolder)
        check_dir_exists(test)
        q.put((full_folder, train, test, divodd))

    copyfile(q)

if __name__ == "__main__":
    from_dir = '/Users/karo/Desktop/crawl_task/comment_txt'
    to_dir = '/Users/karo/Desktop/crawl_task'
    divodd = 0.2
    data_divi(from_dir, to_dir, divodd)
    print('Successfully divided data set into training set and testing set.')
