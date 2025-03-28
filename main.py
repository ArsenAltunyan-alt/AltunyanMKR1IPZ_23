import filtertxt

if __name__ == "__main__":
    input_filename = input("Введіть шлях до файлу: ")
    keyword_to_filter = input("Введіть ключове слово: ")
    filtertxt.filter_lines(input_filename, keyword_to_filter)