#!/usr/bin/python
# -*- coding: utf-8 -*-

""" import sys
reload(sys)
sys.setdefaultencoding("utf-8") """

import os
import json

cwd = os.getcwd()
os.chdir(cwd)

src_dir= 'completions/'
prompt_dir='prompts/'

def open_file(filepath):
    with open(filepath,'r',encoding='utf-8',errors='ignore') as infile:
        #infile = infile.read().decode(errors='replace')
        return infile.read()

if __name__ == '__main__':
    files = os.listdir(src_dir)
    print(files)
    data = list()
    print(data)
    for file in files:
        completion=open_file(src_dir + file)
        prompt=open_file(prompt_dir + file)
        info = {'prompt':prompt, 'completion':completion}
        data.append(info)
    with open ('agi_scenarios2.jsonl','w') as outfile:
        for i in data:
            json.dump(i, outfile)
            outfile.write('\n')
 

