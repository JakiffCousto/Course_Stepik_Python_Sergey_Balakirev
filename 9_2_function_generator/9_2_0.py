'''
Подвиг 1.
Вводится натуральное число N.
Необходимо определить функцию-генератор с именем get_sum,
которая бы возвращала текущую сумму чисел последовательности
длины N в диапазоне целых чисел [1; N]. Например:
- для первого числа 1 сумма равна 1;
- для второго числа 2 сумма равна 1+2 = 3
....
- для N-го числа сумма равна 1+2+...+(N-1)+N
Реализовать функцию-генератор get_sum без использования коллекций. Вызывать ее не нужно, только определить.
Sample Input:
5
Sample Output:
1 3 6 10 15
'''


def find_word(f, word):
    g_index = 0
    for line in f:
        indx = 0
        while(indx != -1):
            indx = line.find(word, indx)
            if indx > -1:
                yield g_index + indx
                indx = indx + 1
        g_index = g_index + len(line)


try:
    with open('file_name.txt', encoding='utf-8') as file:
        a = find_word(file, "генератор")
        print(list(a))
except FileNotFoundError:
    print("Файл не найден")
except:
    print("Ошибка обработки файла")