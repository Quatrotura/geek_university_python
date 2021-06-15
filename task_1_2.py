
# 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. 
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, 
# сумма цифр которых делится нацело на 7. Внимание: новый список не создавать!!!

numbers = [] 								# пустой список для кубов нечетных чисел заданного числового ряда
third_power_number_1 = 0 					# куб нечетного числа
third_power_number_2 = 0 					# куб нечетного числа, копия
sum_3d_pow_num_fig_sum_div_7 = 0 			# сумма кубов нечетного числа, когда сумма цифр такого куба кратна 7
sum_3d_pow_num_plus_17_fig_sum_div_7 = 0 	# сумма (кубов нечетного числа + 17), когда сумма цифр такого куба кратна 7


for i in range(1001):
	if i % 2 != 0:
		# Задача 2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000

		third_power_number_1 = third_power_number_2 = i ** 3
		numbers.append(third_power_number_1) 

		# Задача 2-а: Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
		# расчехление куба нечетного числа до цифр и их суммирование
		
		third_power_number_figures_sum = 0 # сумма цифр куба нечетного числа
		
		while third_power_number_1 >= 1:
			third_power_number_figures_sum += third_power_number_1 % 10
			third_power_number_1 //= 10
		
		# проверка является ли полученная сумма цифр куба нечетного числа кратной 7. если истина, запись в соответств переменную
		
		if third_power_number_figures_sum % 7 == 0:
			sum_3d_pow_num_fig_sum_div_7 += third_power_number_2


		# Задача 2-б: К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, 
		# сумма цифр которых делится нацело на 7.

		third_power_number_2 += 17 #  используем изначальный набор переменных, чтобы не засорять код, добавляем 17 к полученному кубу
		third_power_number_1 = third_power_number_2 
		third_power_number_figures_sum = 0 # сумма цифр куба нечетного числа
		

		# расчехление куба нечетного числа плюс 17 до цифр и их суммирование
				
		while (third_power_number_1) >= 1:
			third_power_number_figures_sum += third_power_number_1 % 10
			third_power_number_1 //= 10

		# проверка является ли полученная сумма цифр (куба нечетного числа +17) кратной 7. если истина, запись в соответств переменную
		
		if third_power_number_figures_sum % 7 == 0:
			sum_3d_pow_num_plus_17_fig_sum_div_7 += third_power_number_2

print (sum_3d_pow_num_fig_sum_div_7) 				#  вывод значения для задачи 2-а
print (sum_3d_pow_num_plus_17_fig_sum_div_7) 		#  вывод значения для задачи 2-б