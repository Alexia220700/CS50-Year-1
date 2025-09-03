class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):
        return f"Pizza with {', '.join(self.ingredients)}"

    @classmethod
    def margherita(cls):
        return cls(["tomato sauce", "mozzarella", "basil"])

    @classmethod
    def pepperoni(cls):
        return cls(["tomato sauce", "mozzarella", "pepperoni"])

    @staticmethod
    def cooking_time(size):
        if size == "small":
            return 10
        elif size == "medium":
            return 15
        else:
            return 20

# Using class methods as alternative constructors
margherita = Pizza.margherita()
pepperoni = Pizza.pepperoni()
print(margherita)
print(pepperoni)

# Using static method
print(f"Cooking time: {Pizza.cooking_time('medium')} minutes")
