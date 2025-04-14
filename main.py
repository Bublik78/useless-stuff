import time

print('Эта программа позволяет делать записи в дневнике.')
print('Дневник - файл "swag.txt"')

with open('swag.txt', 'a', encoding='utf-8') as swag:
    swag.write(f'{time.asctime()} \n')
    print('Вводи свой стафф. А чтобы выйти введи "выход"')
    user_input = input('')

    while user_input.lower() != 'выход':
        swag.write(f'{user_input} \n')
        user_input = input('')

    swag.write('\n--- Конец записи ---\n')
