digit = lambda num: '{:,}'.format(num).replace(',', '.')
class UserDate():
	balance = 15000


print('mq')

def rulette():
	exit = 0

	while exit == 0:
		try:

			stavka = input('Введите ставку: ')

			import random

			if UserDate.balance >= int(stavka):
				x = random.randint(1, 100)

				if x in ['1', '3', '5', '10', '15', '20', '30', '50', '100']:
					win = int(stavka) * x
					UserDate.balance += win
					print(f'Вы выйграли {digit(win)}! Ваш баланс: {digit(UserDate.balance)}')

				else:
					UserDate.balance -= int(stavka)
					print(f"Вы проиграли! Ваш баланс: {digit(UserDate.balance)}")
					


				u = int(input(f'Будите ещё играть? 1 = да / 2 = нет: '))

			else:
				print(f'У вас нету столько денег!')

			if u == 1:
				exit = 0

			elif u == 2:
				exit = 1

			else:
				exit = 1

		except Exception as error:
			print(error)


		


rulette()
