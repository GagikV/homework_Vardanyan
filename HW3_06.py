def func():
    for word in input("Ввести слова строчными латинскими символами через пробел: ").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print((word.title()) if chars == len(word) else f"{word} - вводить можно только строчные латинские символы!")


func()
