class Item:
    def __init__(self, name, cost, calories):
        self.name = name
        self.cost = cost
        self.calories = calories

    def __str__(self):
        return f"{self.name} - Cost: {self.cost}, Calories: {self.calories}"
