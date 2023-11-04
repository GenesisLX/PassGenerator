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
