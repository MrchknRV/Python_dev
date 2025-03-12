import time

start_time = time.perf_counter()

# n = int(input())
# count_try = 0
# my_set = set()
#
# for i in range(n):
#     student, result = input().split(': ')
#     if result == 'Correct':
#         count_try += 1
#         my_set.add(f'{student}: {result}')
#
# if len(my_set) == 0:
#     print('Вы можете стать первым, кто решит эту задачу')
# else:
#     print(f'Верно решили {len(my_set)} учащихся')
#     print(f'Из всех попыток {int((count_try / n) * 100 + 0.5)}% верных')
n = int(input())
correct_counter = 0
people_correct = 0
my_set = set()
my_list = []
if n == 0:
    print("Вы можете стать первым, кто решит эту задачу")
else:
    for _ in range(n):
        cur_answer = tuple(input().lower().split(":"))
        my_set.add(cur_answer)
        my_list.append(cur_answer)

    for object in my_list:
        for answer in object:
            if 'correct' in answer:
                correct_counter += 1
    for object in my_set:
        for answer in object:
            if 'correct' in answer:
                people_correct += 1

    all_answers = len(my_list)
    precent_responses = correct_counter / all_answers * 100
    if correct_counter == 0:
        print("Вы можете стать первым, кто решит эту задачу")
    else:
        print(f'Верно решили {people_correct} учащихся\nИз всех \
попыток {int(precent_responses + 0.5)}% верных')




end_time = time.perf_counter()
execution_time = end_time - start_time
print(f'Время вполнения {execution_time:.5f}')
