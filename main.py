# def average_list(list1):
#     avr_num = sum(list1) // len(list1)
#     avr_list = [num for num in list1 if num < avr_num]
#
#     return avr_list
#
#
# print(average_list([1, 2, 3, 4, 5]))
#
# def only_unique_strings(list1):
#     return list(set(list1))
#
#
# print(only_unique_strings(['apple', 'banana', 'orange', 'apple']))
#
# def sorted_by_descending_price(my_list):
#     return sorted(my_list, key=lambda x: x[1], reverse=True)
#
#
# print(sorted_by_descending_price([("apple", 2.5), ("banana", 3.5), ("orange", 1.5), ("cherry", 2), ("melon", 2.7)]))
#

def filter_genre(my_list, genre):
    new_list = [elem for elem in my_list if elem["genre"] == genre]
    return new_list


films =[
    {"title": 'The Shawshank Redemption', "genre": 'Drama', "director": 'Frank Darabont'},
    {"title": 'The Godfather', "genre": 'Crime', "director": 'Francis Ford Coppola'},
    {"title": 'The Dark Knight', "genre": 'Action', "director": 'Christopher Nolan'}
]

genre = 'Drama'
print(filter_genre(films, genre))
