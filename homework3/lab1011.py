#Dumkele Osegi #PSID 1894081
class FoodItem:

    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
    # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':

    food_item1 = FoodItem()

    item_name = input()
    measure_fat = float(input())
    measure_carbs = float(input())
    measure_protein = float(input())

    food_item2 = FoodItem(item_name, measure_fat, measure_carbs, measure_protein)

    num_servings = float(input())

    food_item1.print_info()
    print("Number of calories for {:.2f} serving(s): "
          "{:.2f}".format(num_servings, food_item1.get_calories(num_servings)))
    print()
    food_item2.print_info()
    print("Number of calories for {:.2f} serving(s): "
          "{:.2f}".format(num_servings, food_item2.get_calories(num_servings)))
