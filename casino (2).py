digit = lambda num: '{:,}'.format(num).replace(',', '.')
class UserDate():
	balance = 15000


print('mq')
exit = 0

def rulette():
	stavka = input('Введите ставку: ')

	import random

	x = random.randint(1, 100)

	if x in ['1', '3', '5', '10']:
		win = int(stavka) * x
		UserDate.balance += win
		print(f'Вы выйграли {digit(win)}! Ваш баланс: {digit(UserDate.balance)}')

	else:
		print(f"Вы проиграли! Ваш баланс: {digit(UserDate.balance)}")
		UserDate.balance -= int(stavka)


	u = input(f'Будите ещё играть? y/n: ')

	if u == 'y':
		exit == 0
	else:
		exit == 1


def main():
	while exit == 0:
		rulette()


if 1 == 1:
	main()

