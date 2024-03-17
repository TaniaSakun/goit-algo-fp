from numpy import random
from collections import Counter
from tabulate import tabulate

MATH_PROB = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}


def dice_rolls_try(num=10000):
    rolls = random.randint(1, 7, (num, 2))
    sums = rolls.sum(axis=1)
    return Counter(sums)


def calc_monte_carlo_probabilities(data):
    total = sum(data.values())
    return {k: v / total * 100 for k, v in data.items()}


def monte_carlo_task():
    for n in (1000, 10000, 100000):
        data = dice_rolls_try(n)
        mc_prob = calc_monte_carlo_probabilities(data)

    print(f"\nMonte Carlo, {n} iterations")
    print(
        tabulate(
            [
                (k, MATH_PROB[k], mc_prob[k], abs(MATH_PROB[k] - mc_prob[k]))
                for k in MATH_PROB
            ],
            headers=["Result", "Math prob", "MC prob", "Error"],
            tablefmt="grid",
        )
    )
