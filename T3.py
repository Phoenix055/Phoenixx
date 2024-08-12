words = []
palindrome_words = []

while True:
    menu = input("1.Введите слово прописными буквами\n"
                 "2.Слова палиндромы\n"
                 '3.Список слов\n').lower()
    if menu == "1":
        word = input('Введите слово ')
        if word == word[::-1]:
            palindrome_words.append(word)
            words.append(word)
            print("Слово - палиндром и добавлено в список")
        else:
            words.append(word)
            print("Слово не палиндром, но добавлено в список")

    elif menu == '2':
        print(palindrome_words)

    elif menu == '3':
        print(words)
