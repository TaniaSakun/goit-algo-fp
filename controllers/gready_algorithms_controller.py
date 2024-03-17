from models.item import Item
from models.greedy import GreedyAlgorithm
from models.dynamic import DynamicProgramming


def gready_algorithms_task():
    items_data = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    items = [
        Item(name, data["cost"], data["calories"]) for name, data in items_data.items()
    ]
    limit = 100

    greedy = GreedyAlgorithm()
    greedy_selected_items, greedy_total_cost, greedy_total_calories = (
        greedy.select_items(items, limit)
    )
    print(
        f"Using greedy algorithm, we can buy these items with total calories {greedy_total_calories} by {limit} limit:"
    )
    print(",".join(item.name for item in greedy_selected_items))

    dp = DynamicProgramming()
    dynamic_total_calories, dynamic_selected_items = dp.knapsack(items, limit)
    print(
        f"Using dynamic programming, we can buy these items with total calories {dynamic_total_calories} by {limit} limit:"
    )
    print(",".join(dynamic_selected_items))
