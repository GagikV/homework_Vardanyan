with open('text1.txt', 'r', encoding='utf-8') as txt:
    num = [f'{count}. {line.strip()} - {len(line.split())} слов' for count, line in enumerate(txt, 1)]
    print(*num, f"Количество строк - {len(num)}", sep="\n")

