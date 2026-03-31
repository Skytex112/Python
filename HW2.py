class Shoes:
    def __init__(self, gender, kind, color, price, manufacturer, size):
        self.gender = gender              
        self.kind = kind                  
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def show_info(self):
        print(f"Тип: {self.gender}")
        print(f"Вид: {self.kind}")
        print(f"Колір: {self.color}")
        print(f"Ціна: {self.price}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Розмір: {self.size}")

    def change_price(self, new_price):
        self.price = new_price

    def change_size(self, new_size):
        self.size = new_size


shoe = Shoes("чоловіче", "кросівки", "чорний", 2500, "Nike", 42)
shoe.show_info()

shoe.change_price(2300)
print("\nПісля зміни ціни:")
shoe.show_info()

class Recipe:
    def __init__(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients 
        self.cuisine = cuisine

    def show_info(self):
        print(f"Назва: {self.name}")
        print(f"Автор: {self.author}")
        print(f"Тип: {self.recipe_type}")
        print(f"Опис: {self.description}")
        print(f"Відео: {self.video_link}")
        print(f"Кухня: {self.cuisine}")
        print("Інгредієнти:")
        for item in self.ingredients:
            print(f"- {item}")

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def change_description(self, new_description):
        self.description = new_description


recipe = Recipe(
    "Борщ",
    "Микола",
    "перша страва",
    "Традиційний український борщ",
    "https://youtube.com/example",
    ["буряк", "капуста", "картопля"],
    "українська"
)

recipe.show_info()

recipe.add_ingredient("морква")
print("\nПісля додавання інгредієнта:")
recipe.show_info()