# a.	Откройте и прочитайте файл(если его нет необходимо вывести ошибку).

# rating = open("data_hw5/ratings.list", 'r')
# rating.close()



# b.	Найдите ТОП250 фильмов и извлеките заголовки.

with open("data_hw5/ratings.list", 'r') as rating:

    rating_list = rating.readlines()
    my_list = rating_list[28:278]

    for i in my_list:
        x = i.strip('\n')
        lst = x.split()
        print(" ".join(lst[3:-1]))

# c.	Программа создает 3 файла
#  top250_movies.txt – названия файлов,
#  ratings.txt – гистограмма рейтингов,
#  years.txt – гистограмма годов.
import json

with open("data_hw5/ratings.list", 'r') as rating:

    rating_list = rating.readlines()
    my_list = rating_list[28:32]

#  top250_movies.txt – названия файлов,
with open("data_hw5/top250_movies.txt", 'w') as top250_movies:
    for i in my_list:
        # x = i.strip('\n')
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
    # print(set(ratings_num))

    my_list_2 = []
    for i in my_list:
        my_list_2.append(i.split())
    print(my_list_2)




