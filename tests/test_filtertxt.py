import pytest
import filtertxt
import os

@pytest.fixture
def test_files():
    test_input = "test_input.txt"
    test_output = "test_output.txt"
    
    with open(test_input, "w", encoding="utf-8") as f:
        f.write("Це тестовий рядок.\n")
        f.write("Цей рядок не містить ключове слово.\n")
        f.write("Ще один тестовий рядок.\n")
    
    yield test_input, test_output
    
    os.remove(test_input)
    os.remove(test_output)

@pytest.mark.parametrize("keyword, expected", [
    ("тест", ["Це тестовий рядок.\n", "Ще один тестовий рядок.\n"]),
    ("рядок", ["Це тестовий рядок.\n", "Цей рядок не містить ключове слово.\n", "Ще один тестовий рядок.\n"]),
    ("немає", [])
])
def test_filter_lines(test_files, keyword, expected):
    test_input, test_output = test_files
    
    filtertxt.filter_lines(test_input, keyword, test_output)
    
    with open(test_output, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    assert lines == expected, f"Фільтрація для ключового слова '{keyword}' працює неправильно"

if __name__ == "__main__":
    pytest.main()
