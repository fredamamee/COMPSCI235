class Recipe:
    def __init__(self, idd, name, author, images, ingredients, date, rating,
                 ingredients_quantities, preparation_time, instructions,
                 category, cook_time, recipe_yield, servings, description, reviews):
        self.__name = name
        self.__ingredients = ingredients
        self.__id = idd
        self.__author = author
        self.__images = images
        self.__date = date
        self.__rating = rating
        self.__ingredients_quantities = ingredients_quantities
        self.__preparation_time = preparation_time
        self.__category = category
        self.__instructions = instructions
        self.__cook_time = cook_time
        self.__recipe_yield = recipe_yield
        self.__reviews = reviews
        self.__servings = servings
        self.__description = description
