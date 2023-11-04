import random
from front import *
# -------------------------------------
from pass_generator import run_generate_password

while True:
    password_len = int(input("Введите длину пароля: "))
    repeat_count = int(input("Введите кол-во паролей: "))
    checkbox_items = [0, 5, 1, 3, 4, 2]
    run_generate_password(password_len, repeat_count, checkbox_items)

    while True:
        print("Вы хотите продолжить? (y/n)")
        action = "".join(input().lower().split())
        if action == "y":
            break
        elif action == "n":
            exit()
        else:
            print("Значение некорректно!")


# -------------------------------------
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# rus_sm = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# rus_b = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#
# eng_sm = "abcdefghijklmnopqrstuvwxyz"
# eng_b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special = ",./\[]{}<>?!|&$#@-+="

# g = random.randint(0, 9)
#
# print(random.choices(num, k=10))  # random лист опр. длины
# print(random.sample(num, g))


# len_pass = int(input("Введите длину пароля: "))
# # lang = input("Если анг (1)")
# c = int(input("Введите кол-во паролей: "))



# def def_symbol(len_pass):
#     limit = len_pass-3
#     val_symbol = []
#     for i in range(3):
#         if i == 0:
#             v = random.randint(1, limit)
#         else:
#             if i == 1:
#                 limit += 1
#             v = random.randint(1, limit)
#
#         val_symbol.append(v)
#         if v == limit:
#             lenv = len(val_symbol)
#             if lenv != 3:
#                 for i in range(4-lenv):
#                     val_symbol.append(1)
#                 return val_symbol
#
#         limit -= v
#     else:
#         val_symbol.append(limit+2)
#     return val_symbol
#
# for i in range(c):
#     val_symbol = def_symbol(len_pass)
    # print(val_symbol)
    # print(sum(val_symbol))
    # if sum(val_symbol) != len_pass:
    #     print("-----------")
    #     print(val_symbol)
    #     print(sum(val_symbol))
    #     print("-----------")
    #     break

    #------
    # a = random.choices(num, k=val_symbol[0])
    # b = random.choices(rus_sm, k=val_symbol[1])
    # c = random.choices(rus_b, k=val_symbol[2])
    # d = random.choices(special, k=val_symbol[3])
    # # p = [random.choices() for _ in range(4)]
    #
    #
    # password = []
    # password.extend(a)
    # password.extend(b)
    # password.extend(c)
    # password.extend(d)
    # random.shuffle(password)
    # print(*password, sep="")














# if __name__ == "__main__":
    # app.run()


