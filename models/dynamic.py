from models.item import Item


class DynamicProgramming:
    @staticmethod
    def knapsack(items, limit):
        n = len(items)
        K = [[0 for _ in range(limit + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(limit + 1):
                if items[i - 1].cost <= j:
                    K[i][j] = max(
                        K[i - 1][j],
                        items[i - 1].calories + K[i - 1][j - items[i - 1].cost],
                    )
                else:
                    K[i][j] = K[i - 1][j]

        selected_items = []
        j = limit
        for i in range(n, 0, -1):
            if K[i][j] != K[i - 1][j]:
                selected_items.append(items[i - 1].name)
                j -= items[i - 1].cost

        return K[n][limit], selected_items
