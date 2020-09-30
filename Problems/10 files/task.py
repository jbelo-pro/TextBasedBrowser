for number in range(1, 11):
    with open(f"file{number}.txt", 'w', encoding='utf-8') as f:
        f.write(str(number))
