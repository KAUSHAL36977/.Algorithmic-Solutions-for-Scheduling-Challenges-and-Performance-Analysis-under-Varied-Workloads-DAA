import re

# Predefined dictionary to map keywords to algorithms
ALGORITHM_RECOMMENDATIONS = {
    'sorting': ['Merge Sort', 'Quick Sort', 'Heap Sort'],
    'searching': ['Binary Search', 'Depth-First Search (DFS)', 'Breadth-First Search (BFS)'],
    'shortest path': ['Dijkstra’s Algorithm', 'Bellman-Ford Algorithm', 'Floyd-Warshall Algorithm'],
    'graph': ['DFS', 'BFS', 'Kruskal’s Algorithm', 'Prim’s Algorithm'],
    'string matching': ['Knuth-Morris-Pratt (KMP) Algorithm', 'Rabin-Karp Algorithm', 'Boyer-Moore Algorithm'],
    'optimization': ['Dynamic Programming (DP)', 'Greedy Algorithm'],
    'knapsack': ['Dynamic Programming (Knapsack)', 'Branch and Bound (Knapsack)'],
    'primes': ['Sieve of Eratosthenes', 'Miller-Rabin Primality Test'],
    'matrix': ['Strassen’s Matrix Multiplication', 'Dynamic Programming'],
    'approximation': ['Approximation Algorithms (TSP)', 'Set Cover Approximation'],
    'pathfinding': ['A* Algorithm', 'Dijkstra’s Algorithm'],
    'minimum spanning tree': ['Kruskal’s Algorithm', 'Prim’s Algorithm'],
    'pattern': ['Dynamic Programming', 'Regular Expressions'],
    'backtracking': ['N-Queens Problem', 'Sudoku Solver', 'Graph Coloring'],
    'flow': ['Ford-Fulkerson Algorithm', 'Edmonds-Karp Algorithm']
}

def recommend_algorithms(description):
    # Convert the description to lowercase for case-insensitive matching
    description = description.lower()

    # Initialize a list to store matched algorithms
    recommendations = set()

    # Check for each keyword in the user's description
    for keyword, algorithms in ALGORITHM_RECOMMENDATIONS.items():
        if re.search(rf'\b{keyword}\b', description):
            recommendations.update(algorithms)

    # Return the list of unique algorithm recommendations
    if recommendations:
        return list(recommendations)
    else:
        return ["No specific algorithm recommendation found. Please provide more details."]

# Example usage
user_case = input("Enter the description of your problem: ")
recommended_algorithms = recommend_algorithms(user_case)
print("Recommended Algorithms:")
for algorithm in recommended_algorithms:
    print(f"- {algorithm}")
class AlgorithmRecommenderChatbot:
    def __init__(self):
        # Mapping keywords to potential algorithms
        self.algorithm_recommendations = {
            'sorting': ['Merge Sort', 'Quick Sort', 'Heap Sort'],
            'searching': ['Binary Search', 'DFS', 'BFS'],
            'shortest path': ['Dijkstra’s Algorithm', 'Bellman-Ford Algorithm', 'Floyd-Warshall Algorithm'],
            'graph': ['DFS', 'BFS', 'Kruskal’s Algorithm', 'Prim’s Algorithm'],
            'string matching': ['Knuth-Morris-Pratt (KMP)', 'Rabin-Karp', 'Boyer-Moore'],
            'optimization': ['Dynamic Programming', 'Greedy Algorithm'],
            'knapsack': ['DP (Knapsack)', 'Branch and Bound (Knapsack)'],
            'primes': ['Sieve of Eratosthenes', 'Miller-Rabin Test'],
            'matrix': ['Strassen’s Matrix Multiplication', 'Dynamic Programming'],
            'approximation': ['Approximation Algorithms (TSP)', 'Set Cover Approximation'],
            'pathfinding': ['A* Algorithm', 'Dijkstra’s Algorithm'],
            'minimum spanning tree': ['Kruskal’s Algorithm', 'Prim’s Algorithm'],
            'pattern': ['Dynamic Programming', 'Regular Expressions'],
            'backtracking': ['N-Queens Problem', 'Sudoku Solver', 'Graph Coloring'],
            'flow': ['Ford-Fulkerson', 'Edmonds-Karp']
        }

        # Attributes to store user answers
        self.problem_type = ""
        self.additional_details = ""

    def ask_questions(self):
        print("Hello! I’m here to help you find the best algorithm for your problem.")

        # Step 1: Asking about the type of problem
        self.problem_type = input("Could you describe the main type of problem you are dealing with? "
                                  "For example, is it about sorting, searching, graphs, optimization, etc.?\n").lower()

        # Step 2: Further questions based on initial input
        if "graph" in self.problem_type:
            self.additional_details = input("Got it! Is it related to shortest path, MST (minimum spanning tree), or "
                                            "finding strongly connected components?\n").lower()
        elif "string" in self.problem_type or "pattern" in self.problem_type:
            self.additional_details = input("Understood! Are you looking for exact string matching, pattern searching, or substring finding?\n").lower()
        elif "optimization" in self.problem_type:
            self.additional_details = input("Optimization! Is it related to the knapsack problem, pathfinding, or another optimization task?\n").lower()
        else:
            self.additional_details = input("Could you please share any more details that might help refine my suggestion?\n").lower()

    def recommend_algorithm(self):
        # Combine initial problem type and additional details to search for relevant algorithms
        combined_input = f"{self.problem_type} {self.additional_details}"

        recommendations = set()

        # Search for matches in the predefined dictionary
        for keyword, algorithms in self.algorithm_recommendations.items():
            if keyword in combined_input:
                recommendations.update(algorithms)

        # Display recommendations
        if recommendations:
            print("\nBased on your description, here are some algorithm recommendations:")
            for algo in recommendations:
                print(f"- {algo}")
        else:
            print("\nI'm sorry, I couldn't find a specific recommendation based on the provided details."
                  " You might try describing the problem differently.")

# Running the chatbot
chatbot = AlgorithmRecommenderChatbot()
chatbot.ask_questions()
chatbot.recommend_algorithm()
class AlgorithmRecommenderChatbot:
    def __init__(self):
        # Updated dictionary with algorithm descriptions
        self.algorithm_recommendations = {
            'sorting': [
                ("Merge Sort", "A divide-and-conquer algorithm that splits the array in half, sorts each half recursively, and merges them back together. Best used for large datasets where stability and O(n log n) time complexity are preferred."),
                ("Quick Sort", "An efficient sorting algorithm that uses a pivot to partition the array, then recursively sorts the partitions. Suitable for large datasets, though it has an average time complexity of O(n log n)."),
                ("Heap Sort", "A comparison-based algorithm that builds a max-heap from the array and extracts elements in sorted order. It has O(n log n) complexity and is useful when space is limited.")
            ],
            'searching': [
                ("Binary Search", "An efficient algorithm for finding an item in a sorted array by repeatedly dividing the search interval in half. It runs in O(log n) time and requires a sorted list."),
                ("DFS", "Depth-First Search explores as far as possible along each branch before backtracking, commonly used in tree/graph traversal."),
                ("BFS", "Breadth-First Search explores the neighbor nodes first before moving to the next level neighbors, often used in shortest path finding in unweighted graphs.")
            ],
            'shortest path': [
                ("Dijkstra’s Algorithm", "Finds the shortest path from a source to all other vertices in a weighted graph with non-negative weights. Efficient for dense graphs."),
                ("Bellman-Ford Algorithm", "Calculates shortest paths in a graph with negative weights. It’s slower than Dijkstra’s but works with graphs having negative edge weights."),
                ("Floyd-Warshall Algorithm", "A dynamic programming approach for finding shortest paths between all pairs of vertices. Suitable for dense graphs with time complexity O(V^3).")
            ],
            # Additional mappings with descriptions for other types
            'graph': [
                ("DFS", "Explores all nodes by moving as deep as possible along each branch before backtracking. Useful for connectivity checks and detecting cycles."),
                ("BFS", "Expands nodes in a level-wise manner, often used in finding shortest paths in unweighted graphs."),
                ("Kruskal’s Algorithm", "Finds a Minimum Spanning Tree by adding edges in increasing order of weight, avoiding cycles. Best for sparse graphs."),
                ("Prim’s Algorithm", "Builds a Minimum Spanning Tree by adding edges from the connected components with the lowest weight, more efficient for dense graphs.")
            ],
            'optimization': [
                ("Dynamic Programming", "Solves problems by breaking them into overlapping subproblems and storing their solutions. Useful for problems like the knapsack, where decisions depend on previous solutions."),
                ("Greedy Algorithm", "Selects the best option at each step, hoping to find a global optimum. Used in problems like activity selection and fractional knapsack.")
            ],
            'knapsack': [
                ("DP (Knapsack)", "Solves the knapsack problem by using a table to store maximum values for subproblems. Efficient for 0/1 Knapsack problems."),
                ("Branch and Bound (Knapsack)", "An optimization approach for solving knapsack with more constraints, using a state-space tree to explore feasible solutions.")
            ]
            # Other problem types with corresponding algorithms and descriptions...
        }

        # Attributes to store user answers
        self.problem_type = ""
        self.additional_details = ""

    def ask_questions(self):
        print("Hello! I’m here to help you find the best algorithm for your problem.")

        # Step 1: Asking about the type of problem
        self.problem_type = input("Could you describe the main type of problem you are dealing with? "
                                  "For example, is it about sorting, searching, graphs, optimization, etc.?\n").lower()

        # Step 2: Further questions based on initial input
        if "graph" in self.problem_type:
            self.additional_details = input("Got it! Is it related to shortest path, MST (minimum spanning tree), or "
                                            "finding strongly connected components?\n").lower()
        elif "string" in self.problem_type or "pattern" in self.problem_type:
            self.additional_details = input("Understood! Are you looking for exact string matching, pattern searching, or substring finding?\n").lower()
        elif "optimization" in self.problem_type:
            self.additional_details = input("Optimization! Is it related to the knapsack problem, pathfinding, or another optimization task?\n").lower()
        else:
            self.additional_details = input("Could you please share any more details that might help refine my suggestion?\n").lower()

    def recommend_algorithm(self):
        # Combine initial problem type and additional details to search for relevant algorithms
        combined_input = f"{self.problem_type} {self.additional_details}"

        recommendations = []

        # Search for matches in the predefined dictionary
        for keyword, algorithms in self.algorithm_recommendations.items():
            if keyword in combined_input:
                recommendations.extend(algorithms)

        # Display recommendations with descriptions
        if recommendations:
            print("\nBased on your description, here are some algorithm recommendations:")
            for algo, description in recommendations:
                print(f"\n- {algo}: {description}")
        else:
            print("\nI'm sorry, I couldn't find a specific recommendation based on the provided details."
                  " You might try describing the problem differently.")

# Running the chatbot
chatbot = AlgorithmRecommenderChatbot()
chatbot.ask_questions()
chatbot.recommend_algorithm()
class AlgorithmRecommenderChatbot:
    def __init__(self):
        # Detailed dictionary with in-depth descriptions of algorithms
        self.algorithm_recommendations = {
            'sorting': [
                ("Merge Sort", """Merge Sort is a stable, divide-and-conquer algorithm that splits the array into halves until each segment contains a single element.
                Then, it merges segments back together in sorted order. It has a time complexity of O(n log n) and is ideal for large datasets where stability is required.
                However, it requires additional space for the merged arrays, making its space complexity O(n).

                **Steps to use Merge Sort**:
                1. Divide the array into two halves.
                2. Recursively sort each half.
                3. Merge the sorted halves together.

                **Advantages**:
                - Consistent time complexity of O(n log n).
                - Stable sorting (preserves the order of equal elements).

                **Limitations**:
                - Requires additional space, making it less suitable for memory-constrained environments.

                **Typical Applications**: Merge Sort is commonly used in applications requiring stable sorting, such as linked lists and external sorting in databases where data needs to be merged in chunks.
                """),

                ("Quick Sort", """Quick Sort is a highly efficient, in-place sorting algorithm that selects a pivot and partitions the array into elements less than and greater than the pivot.
                The algorithm recursively sorts these partitions. It has an average time complexity of O(n log n), but in the worst case (when the array is already sorted or nearly sorted), it can degrade to O(n^2).
                Its space complexity is O(log n) due to the recursive stack.

                **Steps to use Quick Sort**:
                1. Choose a pivot (usually the last element or a random element).
                2. Partition the array into elements less than and greater than the pivot.
                3. Recursively apply the algorithm to partitions.

                **Advantages**:
                - In-place sorting (doesn't require additional memory).
                - Generally faster than Merge Sort for in-memory sorting.

                **Limitations**:
                - Not stable (order of equal elements may change).
                - Performance can degrade in already sorted arrays.

                **Typical Applications**: Used in general-purpose sorting and in-memory datasets, where its speed is an advantage over other algorithms like Merge Sort.
                """),

                ("Heap Sort", """Heap Sort is a comparison-based algorithm that converts the array into a max-heap and then repeatedly extracts the maximum element to get a sorted array.
                With a time complexity of O(n log n) and space complexity of O(1), it is efficient for in-place sorting when space is limited.

                **Steps to use Heap Sort**:
                1. Build a max-heap from the input data.
                2. Extract the maximum element, swap it with the last item in the heap, and reduce the heap size.
                3. Repeat the process until the heap is empty.

                **Advantages**:
                - In-place sorting with no additional space needed.
                - Consistent O(n log n) time complexity.

                **Limitations**:
                - Not stable (order of equal elements may change).
                - Slower than Quick Sort for smaller datasets.

                **Typical Applications**: Ideal in embedded systems or applications where memory constraints are strict.
                """)
            ],
            'shortest path': [
                ("Dijkstra’s Algorithm", """Dijkstra’s Algorithm finds the shortest path from a source vertex to all other vertices in a graph with non-negative edge weights.
                It uses a priority queue to greedily pick the shortest distance vertex at each step. Its time complexity is O((V + E) log V), where V is the number of vertices and E is the number of edges.

                **Steps to use Dijkstra’s Algorithm**:
                1. Initialize the distance to the source node as 0 and all other nodes as infinity.
                2. Use a priority queue to select the vertex with the smallest distance.
                3. For each neighbor of this vertex, calculate the new distance.
                4. Update distances if a shorter path is found.
                5. Repeat until all nodes are visited.

                **Advantages**:
                - Optimal for graphs with non-negative weights.

                **Limitations**:
                - Does not work with negative edge weights (use Bellman-Ford instead).

                **Typical Applications**: Used in navigation systems, routing protocols, and other shortest-path scenarios with non-negative weights.
                """),

                ("Bellman-Ford Algorithm", """The Bellman-Ford Algorithm computes the shortest paths from a source vertex to all other vertices in a graph with both positive and negative weights.
                It uses a relaxation process over all edges, repeating for V-1 times, where V is the number of vertices. It has a time complexity of O(V * E).

                **Steps to use Bellman-Ford Algorithm**:
                1. Initialize the source distance as 0 and other nodes as infinity.
                2. For each vertex, iterate over all edges, updating distances if a shorter path is found.
                3. After V-1 iterations, check for any negative-weight cycles.

                **Advantages**:
                - Handles negative weights and can detect negative-weight cycles.

                **Limitations**:
                - Slower than Dijkstra’s Algorithm for graphs with only positive weights.

                **Typical Applications**: Useful in financial modeling for arbitrage detection, and in graphs with potential negative weights.
                """),

                ("Floyd-Warshall Algorithm", """Floyd-Warshall is a dynamic programming algorithm that finds the shortest paths between all pairs of vertices.
                It has a time complexity of O(V^3) and is best suited for dense graphs.

                **Steps to use Floyd-Warshall Algorithm**:
                1. Initialize a matrix where each cell (i, j) represents the shortest path from i to j.
                2. For each intermediate vertex k, update the paths if a shorter path exists through k.

                **Advantages**:
                - Simple to implement for all-pairs shortest path.
                - Detects negative cycles in a graph.

                **Limitations**:
                - Inefficient for sparse graphs or very large graphs due to O(V^3) complexity.

                **Typical Applications**: Suitable for use in dense graphs, such as social network analysis or network routing where paths between all nodes are required.
                """)
            ]
            # Additional problem types with detailed descriptions...
        }

        # Attributes to store user answers
        self.problem_type = ""
        self.additional_details = ""

    def ask_questions(self):
        print("Hello! I’m here to help you find the best algorithm for your problem.")

        # Step 1: Asking about the type of problem
        self.problem_type = input("Could you describe the main type of problem you are dealing with? "
                                  "For example, is it about sorting, searching, graphs, optimization, etc.?\n").lower()

        # Step 2: Further questions based on initial input
        if "graph" in self.problem_type:
            self.additional_details = input("Got it! Is it related to shortest path, MST (minimum spanning tree), or "
                                            "finding strongly connected components?\n").lower()
        elif "string" in self.problem_type or "pattern" in self.problem_type:
            self.additional_details = input("Understood! Are you looking for exact string matching, pattern searching, or substring finding?\n").lower()
        elif "optimization" in self.problem_type:
            self.additional_details = input("Optimization! Is it related to the knapsack problem, pathfinding, or another optimization task?\n").lower()
        else:
            self.additional_details = input("Could you please share any more details that might help refine my suggestion?\n").lower()

    def recommend_algorithm(self):
        # Combine initial problem type and additional details to search for relevant algorithms
        combined_input = f"{self.problem_type} {self.additional_details}"

        recommendations = []

        # Search for matches in the predefined dictionary
        for keyword, algorithms in self.algorithm_recommendations.items():
            if keyword in combined_input:
                recommendations.extend(algorithms)

        # Display recommendations with detailed descriptions
        if recommendations:
            print("\nBased on your description, here are some algorithm recommendations:")
            for algo, description in recommendations:
                print(f"\n- {algo}:\n{description}")
        else:
            print("\nI'm sorry, I couldn't find a specific recommendation based on the provided details."
                  " You might try describing the problem differently.")

# Running the chatbot
chatbot = AlgorithmRecommenderChatbot()
chatbot.ask_questions()
chatbot.recommend_algorithm()
class AlgorithmRecommenderChatbot:
    def __init__(self):
        # Detailed dictionary with in-depth descriptions of algorithms
        self.algorithm_recommendations = {
            'sorting': [
                ("Merge Sort", """Merge Sort is a stable, divide-and-conquer algorithm that splits the array into halves until each segment contains a single element.
                Then, it merges segments back together in sorted order. It has a time complexity of O(n log n) and is ideal for large datasets where stability is required.
                However, it requires additional space for the merged arrays, making its space complexity O(n).

                **Steps to use Merge Sort**:
                1. Divide the array into two halves.
                2. Recursively sort each half.
                3. Merge the sorted halves together.

                **Advantages**:
                - Consistent time complexity of O(n log n).
                - Stable sorting (preserves the order of equal elements).

                **Limitations**:
                - Requires additional space, making it less suitable for memory-constrained environments.

                **Typical Applications**: Merge Sort is commonly used in applications requiring stable sorting, such as linked lists and external sorting in databases where data needs to be merged in chunks.
                """),

                ("Quick Sort", """Quick Sort is a highly efficient, in-place sorting algorithm that selects a pivot and partitions the array into elements less than and greater than the pivot.
                The algorithm recursively sorts these partitions. It has an average time complexity of O(n log n), but in the worst case (when the array is already sorted or nearly sorted), it can degrade to O(n^2).
                Its space complexity is O(log n) due to the recursive stack.

                **Steps to use Quick Sort**:
                1. Choose a pivot (usually the last element or a random element).
                2. Partition the array into elements less than and greater than the pivot.
                3. Recursively apply the algorithm to partitions.

                **Advantages**:
                - In-place sorting (doesn't require additional memory).
                - Generally faster than Merge Sort for in-memory sorting.

                **Limitations**:
                - Not stable (order of equal elements may change).
                - Performance can degrade in already sorted arrays.

                **Typical Applications**: Used in general-purpose sorting and in-memory datasets, where its speed is an advantage over other algorithms like Merge Sort.
                """),

                ("Heap Sort", """Heap Sort is a comparison-based algorithm that converts the array into a max-heap and then repeatedly extracts the maximum element to get a sorted array.
                With a time complexity of O(n log n) and space complexity of O(1), it is efficient for in-place sorting when space is limited.

                **Steps to use Heap Sort**:
                1. Build a max-heap from the input data.
                2. Extract the maximum element, swap it with the last item in the heap, and reduce the heap size.
                3. Repeat the process until the heap is empty.

                **Advantages**:
                - In-place sorting with no additional space needed.
                - Consistent O(n log n) time complexity.

                **Limitations**:
                - Not stable (order of equal elements may change).
                - Slower than Quick Sort for smaller datasets.

                **Typical Applications**: Ideal in embedded systems or applications where memory constraints are strict.
                """)
            ],
            'shortest path': [
                ("Dijkstra’s Algorithm", """Dijkstra’s Algorithm finds the shortest path from a source vertex to all other vertices in a graph with non-negative edge weights.
                It uses a priority queue to greedily pick the shortest distance vertex at each step. Its time complexity is O((V + E) log V), where V is the number of vertices and E is the number of edges.

                **Steps to use Dijkstra’s Algorithm**:
                1. Initialize the distance to the source node as 0 and all other nodes as infinity.
                2. Use a priority queue to select the vertex with the smallest distance.
                3. For each neighbor of this vertex, calculate the new distance.
                4. Update distances if a shorter path is found.
                5. Repeat until all nodes are visited.

                **Advantages**:
                - Optimal for graphs with non-negative weights.

                **Limitations**:
                - Does not work with negative edge weights (use Bellman-Ford instead).

                **Typical Applications**: Used in navigation systems, routing protocols, and other shortest-path scenarios with non-negative weights.
                """),

                ("Bellman-Ford Algorithm", """The Bellman-Ford Algorithm computes the shortest paths from a source vertex to all other vertices in a graph with both positive and negative weights.
                It uses a relaxation process over all edges, repeating for V-1 times, where V is the number of vertices. It has a time complexity of O(V * E).

                **Steps to use Bellman-Ford Algorithm**:
                1. Initialize the source distance as 0 and other nodes as infinity.
                2. For each vertex, iterate over all edges, updating distances if a shorter path is found.
                3. After V-1 iterations, check for any negative-weight cycles.

                **Advantages**:
                - Handles negative weights and can detect negative-weight cycles.

                **Limitations**:
                - Slower than Dijkstra’s Algorithm for graphs with only positive weights.

                **Typical Applications**: Useful in financial modeling for arbitrage detection, and in graphs with potential negative weights.
                """),

                ("Floyd-Warshall Algorithm", """Floyd-Warshall is a dynamic programming algorithm that finds the shortest paths between all pairs of vertices.
                It has a time complexity of O(V^3) and is best suited for dense graphs.

                **Steps to use Floyd-Warshall Algorithm**:
                1. Initialize a matrix where each cell (i, j) represents the shortest path from i to j.
                2. For each intermediate vertex k, update the paths if a shorter path exists through k.

                **Advantages**:
                - Simple to implement for all-pairs shortest path.
                - Detects negative cycles in a graph.

                **Limitations**:
                - Inefficient for sparse graphs or very large graphs due to O(V^3) complexity.

                **Typical Applications**: Suitable for use in dense graphs, such as social network analysis or network routing where paths between all nodes are required.
                """)
            ]
            # Additional problem types with detailed descriptions...
        }

        # Attributes to store user answers
        self.problem_type = ""
        self.additional_details = ""

    def ask_questions(self):
        print("Hello! I’m here to help you find the best algorithm for your problem.")

        # Step 1: Asking about the type of problem
        self.problem_type = input("Could you describe the main type of problem you are dealing with? "
                                  "For example, is it about sorting, searching, graphs, optimization, etc.?\n").lower()

        # Step 2: Further questions based on initial input
        if "graph" in self.problem_type:
            self.additional_details = input("Got it! Is it related to shortest path, MST (minimum spanning tree), or "
                                            "finding strongly connected components?\n").lower()
        elif "string" in self.problem_type or "pattern" in self.problem_type:
            self.additional_details = input("Understood! Are you looking for exact string matching, pattern searching, or substring finding?\n").lower()
        elif "optimization" in self.problem_type:
            self.additional_details = input("Optimization! Is it related to the knapsack problem, pathfinding, or another optimization task?\n").lower()
        else:
            self.additional_details = input("Could you please share any more details that might help refine my suggestion?\n").lower()

    def recommend_algorithm(self):
        # Combine initial problem type and additional details to search for relevant algorithms
        combined_input = f"{self.problem_type} {self.additional_details}"

        recommendations = []

        # Search for matches in the predefined dictionary
        for keyword, algorithms in self.algorithm_recommendations.items():
            if keyword in combined_input:
                recommendations.extend(algorithms)

        # Display recommendations with detailed descriptions
        if recommendations:
            print("\nBased on your description, here are some algorithm recommendations:")
            for algo, description in recommendations:
                print(f"\n- {algo}:\n{description}")
        else:
            print("\nI'm sorry, I couldn't find a specific recommendation based on the provided details."
                  " You might try describing the problem differently.")

# Running the chatbot
chatbot = AlgorithmRecommenderChatbot()
chatbot.ask_questions()
chatbot.recommend_algorithm()

