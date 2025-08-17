import random

def return_num():
    choice_int = ""
    for x in range(12):
        choice_int = choice_int + random.choice(list("123456789"))
    return (choice_int)

# Сделать рандом усложненный рандом, установить время ответа сайта в милисекундах
# num_random = random.randint(1, 100)
# return num_random