import json
import xml.etree.ElementTree as ET
import sys


# Функция получения текста из json-файла
def json_news(f):
    with open(f, 'r', encoding='utf-8') as file:
        data = json.load(file)
        sp = []
        for i in data['rss']['channel']['items']:
            sp.extend(i['description'].lower().split())
    return sp


# Функция получения текста из xml-файла
def xml_news(f):
    tree = ET.parse(f)
    root = tree.getroot()
    sp = []
    for tag in root.findall('channel/item/description'):
        sp.extend(tag.text.lower().split())
    return sp


# Функция обработки текста
def sp_proc(sp):
    l6 = {}
    for i in sp:
        if len(i) > 6 and i not in l6:
            l6.setdefault(i, sp.count(i))
    l6_sorted = [i[0] for i in sorted(l6.items(), key=lambda item: item[1], reverse=True)]
    for i in range(10):
        print(f"{l6_sorted[i]} - {l6[l6_sorted[i]]} раз(а)")
    print()


temp1 = sys.stdout
# Вызов функции обработки текста полученного из json
sp_proc(json_news('newsafr.json'))
sys.stdout = temp1

temp2 = sys.stdout
# Вызов функции обработки текста полученного из xml
sp_proc(xml_news('newsafr.xml'))
sys.stdout = temp2

# Проверка идентичности обоих выборок
print("Обе выборки идентичны" if temp1 == temp2 else "Выборки не равны")
