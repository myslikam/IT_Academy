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












# rating = open("data_hw5/ratings.list", 'r')
# c = rating.readlines()[29:30]
# # c.split()
# print(c)
# rating.close()


# pip install IMDbPY
# import imdb
#
# film = imdb.IMDb()
#
# # Поиск ТОП250 фильмов
# search = film.get_top250_movies()
#
# # Извлечение 250 заголовков
# for i in range(250):
#     print(search[i]['title'])


# c.	Программа создает 3 файла  top250_movies.txt – названия файлов,
# ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.

# def movies(*args):
#     for i in args:
#         movies = open(f"data_hw5/{i}", 'w')
#         movies.close()
#
# movies('top250_movies.txt', 'ratings.txt', 'years.txt')
