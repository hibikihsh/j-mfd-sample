import MeCab
import re
import argparse
import ipadic
import csv
from collections import defaultdict

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

# 辞書をソート
def sort_dict(d):
  sorted_items = sorted(d.items(), key=lambda x: x[0])
  sorted_dict = {key: value for key, value in sorted_items}
  return sorted_dict

def group_objects_by_value_frequency(data):
    for number, texts in data.items():
        aggregated_dict = {}
        for value_dict in texts:
            for key in value_dict:
                if key in aggregated_dict:
                    aggregated_dict[key] += value_dict[key]
                else:
                    aggregated_dict[key] = value_dict[key]
    return aggregated_dict

if __name__ == '__main__':
    m = MeCab.Tagger(ipadic.MECAB_ARGS)
    segmented_str = ''
    arr_group_by_number = defaultdict(list)
    arr_group_by_number_for_dic = defaultdict(list)

    # J-MFD_2018r1.dicの単語のみの配列を作成
    with open(file_path, encoding="shift-jis") as f:
        for i, line in enumerate(f):
            cells = line.split(",")
            cell = cells[0]
            line = re.sub('\*', '', cell)
            j_mfd_2018_texts.append(line)

    #  numberごとに分類後、MeCabを使って記述を形態素解析
    with open(fpath, encoding='shift-jis') as f:
        reader = csv.reader(f)
        for row in reader:
            text = row[0]
            number = row[1]
            arr_group_by_number[number].append(text)

        arr_group_by_number = sort_dict(arr_group_by_number)
        for number, texts in arr_group_by_number.items():
                
            total_word_count = 0

            for text in texts:
                segmented_str = execute_Mecab('', text)
                total_word_count += len(re.findall(r'\w+', segmented_str))

                j_mfd_text_counts = {}
                for word in j_mfd_2018_texts:
                    count = text.count(word)
                    if count > 0:
                        if word not in j_mfd_text_counts:
                            j_mfd_text_counts[word] = count
                        else:
                            j_mfd_text_counts[word] += count
                arr_group_by_number_for_dic[number].append(j_mfd_text_counts)

            print(number, total_word_count)
            summarized_data = group_objects_by_value_frequency(arr_group_by_number_for_dic)
