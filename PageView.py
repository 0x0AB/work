# This is a sample Python script.

import string
import os
import time
# import concurrent.futures
import pandas as pd
import numpy as np

class PageView:

    def __init__(self, path='https://public.wiwdata.com/engineering-challenge/data/'):
        self.path = path
        self.file_type = '.csv'
        self.output_file = 'output.csv'
        self.merged_data = 'merge.csv'

    def create_name_list(self):
        # Create a string of all lowercase letters
        alphabet_string = string.ascii_lowercase
        # print("alphabet_string : ", alphabet_string)
        # Create a list of all lowercase letters
        alphabet_list = list(alphabet_string)
        # print("alphabet_list : ", alphabet_list)
        # print(len(alphabet_list))
        return alphabet_list

    def generate_file_name(self):
        file_list = []
        alpha_list = self.create_name_list()
        for file_name in alpha_list:
            file = self.path + file_name + self.file_type
            file_list.append(file)
        # print(file_list)
        return file_list

    def merge_files(self,file_list):
        # t1 = time.perf_counter()
        df = pd.concat(map(pd.read_csv, file_list), ignore_index=True)
        # print(df)
        # write a func to save file to disc
        # and make into a thread like threading.Thread(target=saveFile )
        df.to_csv(os.getcwd()+'/'+self.merged_data)
        # t2 = time.perf_counter()
        # print(f'Finished in {t2 - t1} seconds')
        m_table = pd.pivot_table(df, values='length', index='user_id', columns='path')
        m_table.to_csv(os.getcwd()+'/'+self.output_file)
        return self.output_file

    def run(self):
        pv = PageView()
        pv.create_name_list()
        files = pv.generate_file_name()
        pv.merge_files(files)


# if __name__ == '__main__':x
#
#     pv = PageView()
#     pv.create_name_list()
#     files = pv.generate_file_name()
#     pv.merge_files(files)
#
