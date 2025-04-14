import time

print('Эта программа позволяет делать записи в дневнике.')
print('Дневник - файл "swag.txt"')

swag = open('swag.txt', 'a')
swag.write(f'{time.asctime()} \n')
print('Вводи сюда.')
user_input = input('')
swag.write(f'{user_input} \n\n')
