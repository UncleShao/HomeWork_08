import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding="utf-8")
name = "newsafr.xml"
tree = ET.parse(name, parser)
root = tree.getroot()


def top10_word():

    word_value = {}
    xml_data = root.findall("channel/item")
    for xmli in xml_data:
        news_word = xmli.find("description").text.split()
        for word in news_word:
            if len(word) > 6:
                if word in word_value.keys():
                    word_value[word] += 1
                else:
                    word_value[word] = 1
    words_len_list = []
    for key, value in word_value.items():
        word_tuple = (value, key)
        words_len_list.append(word_tuple)

    words_len_list_sorted = sorted(words_len_list)

    print('Топ 10 самых часто встречаюшихся слов длиннее 6 символов: ')
    n = 10
    for key, value in words_len_list_sorted[-10:]:
        print('{} место. Слово "{}". Количество повторов - {}.'.format(n, value, key))
        n -= 1


top10_word()