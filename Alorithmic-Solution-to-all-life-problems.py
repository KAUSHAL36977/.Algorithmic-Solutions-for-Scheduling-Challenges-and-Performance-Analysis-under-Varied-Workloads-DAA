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
