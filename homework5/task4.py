# =====================================================
# a.	Откройте и прочитайте файл(если его нет необходимо вывести ошибку).

rating = open("data_hw5/ratings.list", 'r')
rating.close()


# =====================================================
# b.	Найдите ТОП250 фильмов и извлеките заголовки.

with open("data_hw5/ratings.list", 'r') as rating:

    rating_list = rating.readlines()
    my_list = rating_list[28:278]

    for i in my_list:
        x = i.strip('\n')
        lst = x.split()
        print(" ".join(lst[3:-1]))


# =====================================================
# c.	Программа создает 3 файла

import json

with open("data_hw5/ratings.list", 'r') as rating:

    rating_list = rating.readlines()
    my_list = rating_list[28:278]


 # top250_movies.txt – названия фильмов,
with open("data_hw5/top250_movies.txt", 'w') as top250_movies:
    for i in my_list:
        lst = i.split()
        # Запись в файл названий фильмов
        json.dump(" ".join(lst[3:-1]), top250_movies, indent=' ')


#  ratings.txt – гистограмма рейтингов
with open("data_hw5/ratings.txt", 'w') as ratings:
    # Создание множетва со значениями рейтингов
    ratings_num = set([])
    for i in my_list:
        lst_set = i.split()
        ratings_num.add(lst_set[2])

    my_list_2 = []
    for i in my_list:
        my_list_2.append(i.split())

    ratings_dct = {}
    for key in ratings_num:
        for value in my_list_2:
            if key == value[2]:
                ratings_dct[key] = ratings_dct.get(key, 0)+1

    json.dump(ratings_dct, ratings, indent=' ')



# years.txt – гистограмма годов
with open("data_hw5/years.txt", 'w') as years:
    # Создание множетва со значениями годов
    ratings_years = set([])
    for i in my_list:
        lst_set = i.split()
        ratings_years.add(lst_set[-1])

    my_list_3 = []
    for i in my_list:
        my_list_3.append(i.split())

    ratings_years_dct = {}
    for key in ratings_years:
        for value in my_list_3:
            if key == value[-1]:
                ratings_years_dct[key] = ratings_years_dct.get(key, 0)+1

    json.dump(ratings_years_dct, years, indent=' ')
