import random

symbols = {
    0: "0123456789",
    1: "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    2: "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
    3: "abcdefghijklmnopqrstuvwxyz",
    4: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    5: ",./\[]{}<>?!|&$#@-+="
}


#
def get_collection_intervals(password_len, collection_symbols):
    collection_len = len(collection_symbols)
    elapsed_intervals = collection_len

    if collection_len > password_len:
        return None, f"Длина пароля не может быть меньше {collection_len}"

    max_range = password_len - collection_len + 1
    elements_in_sequence = []

    for i in range(collection_len):
        if elapsed_intervals == 1:
            elements_in_sequence.append(max_range)
            return elements_in_sequence, None

        interval = random.randint(1, max_range)
        elements_in_sequence.append(interval)
        elapsed_intervals -= 1

        if interval == max_range:
            elapsed_intervals = collection_len - len(elements_in_sequence)
            return add_closing_intervals(elements_in_sequence, elapsed_intervals), None

        max_range -= interval - 1


def add_closing_intervals(intervals, intervals_count):
    for i in range(intervals_count):
        intervals.append(1)
    return intervals


def get_elements_by_intervals(intervals, collection_symbols):
    elements = []
    for i, value in enumerate(intervals):
        seq = random.choices(collection_symbols[i], k=value)
        elements.extend(seq)
    return elements


def get_filtered_collection_symbols(items_filter):
    result = {}
    max_collection_index = len(symbols) - 1
    unique_filter = set(items_filter)
    for i, value in enumerate(unique_filter):
        if value > max_collection_index:
            return None, f"Индекс интервала в фильтре не может быть больше {max_collection_index}"
        result[i] = symbols[value]
    return result, None


def get_password(password_len, collection_symbols):
    intervals, error = get_collection_intervals(password_len, collection_symbols)
    if intervals is None:
        # print(error)
        return None, error
    elements = get_elements_by_intervals(intervals, collection_symbols)
    random.shuffle(elements)
    return elements, None


def run_generate_password(password_len, repeat_count, items_filter):
    collection_symbols, error = get_filtered_collection_symbols(items_filter)
    if collection_symbols is None:
        print(error)
        return None

    for i in range(repeat_count):
        password, error = get_password(password_len, collection_symbols)
        if password is None:
            print(error)
            return None
        print(*password, sep="")