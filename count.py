import csv

def count_word_in_column(csv_file, column_name, target_word):
    count = 0

    with open(csv_file, 'r', encoding='cp949') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # 특정 컬럼에서 단어 검색
            cell_value = row[column_name]
            target_word = target_word

            # 단어가 존재하면 카운트 증가
            if target_word in cell_value:
                count += 1

    return count
