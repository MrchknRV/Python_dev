words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}
words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}
words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}


def choose_difficulty(user_choose):
    """Выбор уровня сложности"""
    if user_choose in ["легкий", "лёгкий"]:
        return words_easy
    elif user_choose == "средний":
        return words_medium
    elif user_choose in ["сложный", "тяжелый"]:
        return words_hard
    else:
        return words_medium


def play_game(words):
    """Основная функция приложения"""
    print(f"Выбран уровень сложности. Мы предложи {len(words)} слов, подберите перевод\n")
    answer = {}
    for key, value in words.items():
        print(f"{key}, {len(value)} букв, начинается на {value[0]}...")
        user_answer = input("Ваш ответ: ").lower()
        if user_answer!= value:
            print(f"Неверно. {key.title()} - это {value}.\n")
            answer[key] = False
        else:
            print(f"Верно. {key.title()} - это {user_answer}\n")
            answer[key] = True
    return answer


def display_results(answer):
    """Функция верных решений"""
    true_list = []
    false_list = []
    for key in answer:
        if answer[key] == True:
            true_list.append(key)
        else:
            false_list.append(key)
    print("Правильно отвечены слова:")
    if len(true_list) != 0:
        print(*true_list, sep="\n")
    else:
        print("0\nНе расстраивайся! В следующий раз будет лучше.")
    print()
    print("Неправильно отвечены слова:")
    if len(false_list) != 0:
        print(*false_list, sep="\n")
    else:
        print('Да ты большой молодец! Все отвечено верно.')


def calculate_rank(answer):
    """Ранговая оценка исходя из верных решений"""
    total = 0
    for key in answer:
        if answer[key] == True:
            total += 1
    print()
    return levels[total]


user_answer = input("Выберите уровень сложности.\n\n\
Легкий, средний, сложный.\n> ").lower()
level = choose_difficulty(user_answer)
answer = play_game(level)
display_results(answer)
results = calculate_rank(answer)
print(f"Ваш ранг:\n{results}")