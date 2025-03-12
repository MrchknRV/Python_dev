#Список вопросов с ответами
questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
def is_valid(ans):
    """Функция проверяющая валидность ответа для старта"""
    if ans.lower() != 'ready':
        print("Кажется, вы не хотите играть. Очень жаль.")
        return False
    else:
        return True

def begin_answer(questions, answer):
    """Программа теста вопрос-ответ"""
    counter, score = 0, 0
    #Цикл вопросов
    for i in range(len(questions)):
        print(questions[i])
        user_answer = input('Ваш ответ: ')

        if user_answer != answer[i]: #Проверка правильности ответов
            print(f'Неправильно.\nПравильный ответ: {answer[i]}')
            print()
        else:
            print('Ответ верный!\nВы получаете 10 баллов!')
            print()
            counter += 1
            score += 10

    precent_responses = counter / len(questions) * 100
    return end_test(counter, score, precent_responses)

def end_test(counter, score, precent_responses):
    """Подсчет итогов"""
    print(f"""Вот и всё. \
Вы ответили на {counter} вопросов из 3 верно.
Вы заработали {score} баллов.
Это {round(precent_responses,2)} процентов.""")
#Приветственное слово
print("""Привет!
Предлагаю проверить свои знания английского!
""")
#Запуск программы
start = input('Наберите "ready", чтобы начать!\n> ')
if is_valid(start) == True:
    begin_answer(questions, answers)

