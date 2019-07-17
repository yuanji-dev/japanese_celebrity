# coding: utf-8

import json
import re
import csv

RE_YOMI = re.compile('■(?P<name>.*)（(?P<yomi>.*)）') 
RE_NAME = re.compile('■(?P<name>.*)') 

def clean_intro(i):
    start_flag = '■'
    end_flag = '関連項目'
    start_idx = i.find(start_flag)
    if start_idx:
        i = i[start_idx:]
        end_idx = i.find(end_flag)
        if end_idx:
            i = i[:end_idx]
    return i.strip()

def get_name(i):
    m = RE_NAME.match(i)
    return m.group('name') if m else ''

def get_yomi(i):
    m = RE_YOMI.match(i)
    return m.group('yomi') if m else ''

def main():
    result = []
    with open('celebrity.json') as f:
        celebrities = json.load(f)
        for c in celebrities:
            intro = clean_intro(c['intro'])
            name = c['name']
            if not c['name']:
                name = get_name(intro)
            yomi = get_yomi(intro)
            if yomi or name:
                print(name, yomi)
                result.append(dict(name=name, yomi=yomi, intro=intro, image=c['image']))

    with open('celebrity_clean.json', 'w') as f:
        json.dump(result, f)

    with open('celebrity_yomi.csv', 'w') as f:
        csv_writer = csv.writer(f)
        for c in result:
            name = c['name']
            yomi = c['yomi']
            row = name, yomi, '<img src="%s_%s.jpg" />' % (name, yomi)
            csv_writer.writerow(row)

    with open('celebrity_yomi_intro.csv', 'w') as f:
        csv_writer = csv.writer(f)
        for c in result:
            name = c['name']
            yomi = c['yomi']
            intro = c['intro']
            row = name, yomi, '<img src="%s_%s.jpg" />' % (name, yomi), intro
            csv_writer.writerow(row)

if __name__ == '__main__':
    main()
