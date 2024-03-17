from controllers.linked_list_controller import list_task
from controllers.pythagorean_tree_drawer import draw_pythagorean_tree_task
from controllers.dijkstra_algorithm import print_shortest_path_table
from controllers.tree_visualizator import draw_tree_task, draw_color_tree_task
from controllers.gready_algorithms_controller import gready_algorithms_task
from controllers.monte_carlo_controller import monte_carlo_task


class App:
    def final_task():
        print("Task 1: Data structures. Sorting. Work with a singly linked list")
        list_task()
        print("\n")

        print(
            "Task 2: Recursion. Creation of the 'Pythagoras tree' fractal using recursion"
        )
        draw_pythagorean_tree_task()
        print("\n")

        print("Task 3: Trees, Dijkstra's algorithm")
        print_shortest_path_table()
        print("\n")

        print("Task 4: Visualization of the pyramid")
        draw_tree_task()
        print("\n")

        print("Task 5: Binary tree traversal visualization")
        draw_color_tree_task()
        print("\n")

        print("Task 6: Greedy algorithms and dynamic programming")
        gready_algorithms_task()
        print("\n")

        print("Task 7: Using the Monte Carlo method")
        monte_carlo_task()
        print("\n")
