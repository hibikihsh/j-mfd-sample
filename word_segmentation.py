# coding:utf-8
# word_segmentation.py
# by Yasuhiro Taguchi and Kazutoshi Sasahara
# Last update: 2018.08.26 Released under the MIT license

# This program segments Japanese sentences into words.
# This preprosessing is required before using J-MFD.
# Fist, install Anaconda (Python3.6) https://www.anaconda.com/
# Second, install MeCab related packages:
# In the case of Ubuntu: sudo apt-get install mecab libmecab-dev mecab-ipadic-utf8; pip install mecab-python3
# In the case of Mac (Homebrew): brew install mecab mecab-ipadic; pip install mecab-python3
# Then, type
# python word_segmentation.py -f input.txt

import MeCab
import re
import argparse
import ipadic

parser = argparse.ArgumentParser(description='')
parser.add_argument('-f','--file',required=True)
fpath = parser.parse_args().file # 引数で指定したファイルをfpathに格納
opath = './data/segmented.txt'
ipadic_path = '/opt/homebrew/lib/mecab/dic/ipadic'
file_path = "./data/J-MFD.csv"
j_mfd_2018_texts = []

# 形態素解析
def execute_Mecab(segmented_str, text):
    m.parse('')
    node = m.parseToNode(text)
    while node:
        word = node.surface

        if word != '':
            segmented_str += word + ' '
        node = node.next

    return segmented_str

if __name__ == '__main__':
    m = MeCab.Tagger(ipadic.MECAB_ARGS)
    segmented_str = ''

    # J-MFD_2018r1.dicの単語のみの配列を作成
    with open(file_path, encoding="shift-jis") as f:
        for i, line in enumerate(f):
            cells = line.split(",")
            cell = cells[0]
            line = re.sub('\*', '', cell)
            j_mfd_2018_texts.append(line)

    #  MeCabを使って記述を形態素解析
    with open(fpath, encoding='utf-8') as f:
        for line in f:
            line = re.sub('[、,。]', '', line) # remove special characters
            segmented_str = execute_Mecab(segmented_str, line)
            segmented_str += '\n'
    # segmented.txtに書き込み
    with open(opath,'w', encoding='utf-8') as f:
        f.write(segmented_str)

    # 形態素解析したデータ（segmented.txt）からJ-MFD.csvを使って単語を集計
    j_mfd_text_counts = {}
    with open(opath, encoding='utf-8') as f:
        for i,text in enumerate(f):
            for word in j_mfd_2018_texts:
                count = text.count(word)
                if count > 0:
                    if word not in j_mfd_text_counts:
                        j_mfd_text_counts[word] = count
                    else:
                        j_mfd_text_counts[word] += count

    output = [f"{word},{count}" for word, count in j_mfd_text_counts.items()]

    # 単語の集計データをcsvに書き込み
    with open("./data/j_mfd_text_counts.csv", 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
