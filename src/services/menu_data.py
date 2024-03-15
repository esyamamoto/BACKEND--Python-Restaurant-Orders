import csv
from models.dish import Dish, Ingredient
# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set(self.read_csv(source_path).values())


    def read_csv(self, source_path: str):
        all_data = dict()

        with open(source_path, 'r') as file:
            reader_obj = csv.DictReader(file)

            for row in reader_obj:
                dish_name = row["dish"]
                dish_price = float(row["price"])
                dish_ingredients = row["ingredient"]
                dish_recipe = int(row["recipe_amount"])
                
                if dish_name not in all_data:
                    all_data[dish_name] = Dish(dish_name, dish_price)
                all_data[dish_name].add_ingredient_dependency(Ingredient(dish_ingredients), dish_recipe)

        return all_data
