def read_files(name):
    'Читаем файл'
    import json

    with open(name, encoding='utf-8') as f:
        json_data = json.load(f)
        news_list = ''
        for items in json_data['rss']['channel']['items']:
            news_list += ' ' + items['description']
        return news_list


def count_word(news_list):
    "Считаем слова длиннее 6 символов"
    to_list = news_list.split(' ')
    word_value = {}
    for word in to_list:
        if len(word) > 6:
            if word in word_value:
                word_value[word] += 1
            else:
                word_value[word] = 1
    return word_value



def sort_top(word_value):
    'Сортируем и выводим ТОП10'
    l = lambda word_value: word_value[1]
    sort_list = sorted(word_value.items(), key=l, reverse=True)
    count = 1
    top_10 = {}
    for word in sort_list:
        top_10[count] = word
        count += 1
        if count == 10:
            break
    return top_10


def main(name):
    top_10 = sort_top(count_word(read_files(name)))
    print('Топ 10 самых часто встречаюшихся слов длиннее 6 символов: ')
    n = 1
    for i in top_10.values():
        print('{} место. Слово "{}". Количество повторов - {}'.format(n, i[0], i[1]))
        n += 1


main("newsafr.json")
