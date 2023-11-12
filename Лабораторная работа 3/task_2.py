# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, divide=","):
    list_participants_1 = str_1.split(divide)
    list_participants_2 = str_2.split(divide)
    common_participants = list(set(list_participants_1).intersection(list_participants_2))
    common_participants.sort()
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))
# TODO Провеьте работу функции с разделителем отличным от запятой
