from models.item import Item


class GreedyAlgorithm:
    @staticmethod
    def get_efficiency(items):
        efficiency = {}
        for item in items:
            efficiency[item.name] = item.calories / item.cost
        return efficiency

    @staticmethod
    def select_items(items, limit):
        efficiency = GreedyAlgorithm.get_efficiency(items)
        sorted_items = sorted(items, key=lambda x: efficiency[x.name], reverse=True)
        selected_items = []
        total_cost = 0
        total_calories = 0
        for item in sorted_items:
            if total_cost + item.cost <= limit:
                selected_items.append(item)
                total_cost += item.cost
                total_calories += item.calories
        return selected_items, total_cost, total_calories
