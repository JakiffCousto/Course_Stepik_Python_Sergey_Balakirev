'''
Подвиг 6.
Вводится список книг книжного магазина в формате:
<автор 1>:<название 1>
...
<автор N>:<название N>
Авторы с названиями могут повторяться. Необходимо, используя генераторы, сформировать словарь с именем d вида:
{'автор 1': {'название 1', 'название 2', ..., 'название M'}, ..., 'автор K': {'название 1', 'название 2', ..., 'название S'}}
То есть, ключами выступают уникальные авторы, а значениями - множества с уникальными названиями книг соответствующего автора.
На экран ничего выводить не нужно, только сформировать словарь обязательно с именем d - он, далее будет проверяться в тестах!
P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
Sample Input:
Пушкин: Сказака о рыбаке и рыбке
Есенин: Письмо к женщине
Тургенев: Муму
Пушкин: Евгений Онегин
Есенин: Русь
Sample Output:
True
'''
lst_test = ["Пушкин: Сказака о рыбаке и рыбке",
            "Есенин: Письмо к женщине",
            "Тургенев: Муму",
            "Пушкин: Евгений Онегин",
            "Есенин: Русь"]
d = {x: {j.split(": ")[1] for j in lst_test if j.split(": ")[0] == x} for x in {y.split(": ")[0] for y in lst_test}}
print(lst_test)
print(d)