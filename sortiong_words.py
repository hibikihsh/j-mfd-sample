import re

dictionary = {
    "01": 0,
    "02": 0,
    "03": 0,
    "04": 0,
    "05": 0,
    "06": 0,
    "07": 0,
    "08": 0,
    "09": 0,
    "10": 0,
    "11": 0
}

if __name__ == '__main__':
    with open('./data/J-MFD.csv', encoding='shift-jis') as f:
        with open('./data/j_mfd_text_counts.csv', encoding='utf-8') as f2:
            for i, line in enumerate(f):
                for j, line2 in enumerate(f2):
                    if line.split(",")[0] == line2.split(",")[0]:
                        # dictionary[line.split(",")[0]] = int(line2.split(",")[1])
                        print(line.split(",")[1])

    # Output:   
