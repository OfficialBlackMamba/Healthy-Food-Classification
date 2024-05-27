def food_check():
    food = input("Enter the food: ").lower()

    healthy_fruits = ["apple", "banana", "grapes", "mango", "guava", "kiwi", "watermelon"]
    unhealthy_foods = ["expiry food", "packaging food"]

    if food in healthy_fruits:
        print(f"{food.title()} is healthy!")
    elif food in unhealthy_foods:
        print(f"{food.title()} is unhealthy!")
    else:
        print("Food status unknown.")