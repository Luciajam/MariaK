list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle = len(list_players) // 2
left_team = list_players[:middle]
right_team = list_players[middle:]

print(left_team)
print(right_team)