def filter_lines(input_file, keyword, output_file="filtered.txt"):
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            lines = infile.readlines()
        
        filtered_lines = [line for line in lines if keyword in line]
        
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.writelines(filtered_lines)
        
        print(f"Фільтрування завершено. Результат записаний у {output_file}")
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
