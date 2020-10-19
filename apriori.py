import csv
import math
import time
import pandas as pd
from itertools import chain, combinations

def clean_data(csv): #clean the data generate by IBM #data_10^4trans
    df = pd.read_csv('./'+csv+'.csv')
    print(df)
    print(df.index)
    print(df.shape)
    df['customer'] = ""
    df['transaction'] = ""
    df['item'] = ""
    df.rename(columns={"         1          1         42":"tmp"}, inplace = True)
    df["tmp"][0] = "         1          1         42"

    for i in range(df.shape[0]):
        tmp = df["tmp"][i].split()
        df['customer'][i] = tmp[0]
        df['transaction'][i] = tmp[1]
        df['item'][i] = tmp[2]
        print(i)

    df.drop(["tmp"], inplace = True, axis = 1)
    print(df)
    df.to_csv('./clean_data.csv')

if __name__ == "__main__":
    df = pd.read_csv('./clean_data.csv')
    df.drop(['customer'], axis = 1, inplace = True)
    items = df.groupby("transaction")
    #print(items.groups) #0-962 kinds of items appear in which transaction
    item_dict = items.groups
    trans_list = [] #size = 962, each ele is a list contain the transaction that item appear
    set_num = 0
    for key in item_dict:
        item_list = []
        for i in list(item_dict[key]): # The item exist in the transaction
            item = df['item'][i]
            item_list.append(item) # The list of item of #key transaction
        print(item_list)
        time.sleep(3)
        for l in range(len(item_list)):
            if l > 0:
                for ele in combinations(item_list, l):
                    print(ele)
                    set_num += 1
        print(set_num)
        time.sleep(3)
    print(set_num)
    min_conf = 0.75
    min_sup = 0.5
    #Right now there exists a list of set which represents the transaction number that  item which number is the number of ele appears