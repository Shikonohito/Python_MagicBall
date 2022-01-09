import random

def choice(list_answers):
    print(random.choice(list_answers))

def begin(list_answers):
    print('Задай свой вопрос.')
    question = input()
    while question != '':
        choice(list_answers)
        question = input()

def magic_ball():
    list_answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 
                    'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 
                    'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 
                    'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 
                    'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 
                    'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
    begin(list_answers)

magic_ball()