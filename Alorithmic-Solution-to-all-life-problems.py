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

