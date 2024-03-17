# goit-algo-fp
The repository for the final GoItNeo Basic Algorithms project

### To run the project please complete the following steps:

pip install -r requirements.txt or pip3 install -r requirements.txt

python main.py or python3 main.py

## Task 1: Data structures. Sorting. Work with a singly linked list

Results

Current Linked List:            [2, 3, 3, 1, 2, 3, 4]
Sorted Linked List (inplace):   [1, 2, 2, 3, 3, 3, 4]
Reversed Linked List (new Linked List):  [4, 3, 3, 3, 2, 2, 1]
Reversed Linked List (inplace): None
Sorted Linked List (inplace):   [1, 2, 2, 3, 3, 3, 4]
Second Linked List (sorted):    [0, 1, 2, 5]
Merge sorted Linked List:       [0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5]

## Task 3: Trees, Dijkstra's algorithm

The shortest path from "Hauptbahnhof (U1)" to itself is simply the station "Hauptbahnhof (U1)" with a path length of 0, which is expected.
For nearby stations on the same line, such as "Stiglmaierplatz (U1)" and "Sendlinger Tor (U1)", the shortest paths have a relatively short path length of 2 and 1, respectively.
Some stations require transferring to other lines to reach the destination. For example, to reach "Hauptbahnhof (U2)" or "Hauptbahnhof (U4)", passengers need to transfer lines once, resulting in a path length of 1.
Longer paths are observed for stations further away or requiring multiple transfers. For instance, reaching "Messestadt West (U2)" or "Garching-Forschungszentrum (U6)" involves multiple transfers and results in longer path lengths of 21 and 28, respectively.
Overall, the script effectively computes the shortest paths from "Hauptbahnhof (U1)" to all other stations in the Munich metro network, providing valuable insights into the network's connectivity and travel distances.

## Task 6: Greedy algorithms and dynamic programming

Results

Using greedy algorithm, we can buy these items with total calories 870 by 100 limit:
cola,potato,pepsi,hot-dog
Using dynamic programming, we can buy these items with total calories 970 by 100 limit:
potato,cola,pepsi,pizza

## Task 7: Using the Monte Carlo method

Monte Carlo, 100000 iterations
+----------+-------------+-----------+---------+
|   Result |   Math prob |   MC prob |   Error |
+==========+=============+===========+=========+
|        2 |        2.78 |     2.771 |   0.009 |
+----------+-------------+-----------+---------+
|        3 |        5.56 |     5.572 |   0.012 |
+----------+-------------+-----------+---------+
|        4 |        8.33 |     8.332 |   0.002 |
+----------+-------------+-----------+---------+
|        5 |       11.11 |    11.12  |   0.01  |
+----------+-------------+-----------+---------+
|        6 |       13.89 |    13.865 |   0.025 |
+----------+-------------+-----------+---------+
|        7 |       16.67 |    16.745 |   0.075 |
+----------+-------------+-----------+---------+
|        8 |       13.89 |    13.847 |   0.043 |
+----------+-------------+-----------+---------+
|        9 |       11.11 |    11.111 |   0.001 |
+----------+-------------+-----------+---------+
|       10 |        8.33 |     8.199 |   0.131 |
+----------+-------------+-----------+---------+
|       11 |        5.56 |     5.629 |   0.069 |
+----------+-------------+-----------+---------+
|       12 |        2.78 |     2.809 |   0.029 |
+----------+-------------+-----------+---------+

From the Monte Carlo simulation with 100,000 iterations, we can observe the following:

The probabilities calculated through the Monte Carlo simulation (MC prob) are generally close to the theoretical probabilities (Math prob) for each possible result.

The errors between the Monte Carlo probabilities and the theoretical probabilities are relatively small for most results. The largest error is observed for the result "10", with an error of 0.131, indicating a slightly higher deviation from the theoretical probability.

Overall, the Monte Carlo simulation provides a reasonable estimation of the probabilities of different outcomes of rolling two dice, with errors typically within acceptable bounds. However, for more accurate results, especially for rare events, a larger number of iterations may be required.