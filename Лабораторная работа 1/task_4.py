users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

user_dictionary = {
    "Общее количество" : 0,
    "Уникальные посещения" : 0
}
user_dictionary["Общее количество"] = len(users)
user_dictionary["Уникальные посещения"] = len(set(users))
print(user_dictionary)