import random
# Варианты игры
options = ["камень", "ножницы", "бумага"]

# Получить выбор игрока
player_choice = input("камень, ножницы, бумага: ")

# Получить случайный выбор компьютера
player2_choice = random.choice(options)

# Определить победителя
if player_choice == player2_choice:
    print("Ничья!")
elif (player_choice == "камень" and player2_choice== "ножницы") or (
    player_choice == "ножницы" and player2_choice == "бумага"
) or (player_choice == "бумага" and player2_choice == "камень"):
    print("Победил игрок!")
else:
    print("Победил игрок 2!")