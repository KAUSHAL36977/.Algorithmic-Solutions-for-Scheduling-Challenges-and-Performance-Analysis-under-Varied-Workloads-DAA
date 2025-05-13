class SchedulingAlgorithmRecommender:
    def __init__(self):
        # Comprehensive dictionary with detailed descriptions of scheduling algorithms
        self.algorithm_recommendations = {
            'task scheduling': [
                ("Round Robin (RR)", """Round Robin is a CPU scheduling algorithm where each process is assigned a fixed time slot in a cyclic way.
                It has a time complexity of O(n) and is ideal for time-sharing systems.
                
                **Time Complexity**: O(n) where n is the number of processes
                **Space Complexity**: O(n) for the queue of processes
                
                **Key Parameters**:
                - Time quantum (the time slice allocated to each process)
                
                **Advantages**:
                - Fair allocation of CPU time
                - Good for general purpose computing
                - Low response time for short processes
                
                **Limitations**:
                - Higher waiting time for long processes
                - Performance depends heavily on time quantum selection
                - Context switching overhead
                
                **Typical Applications**: Operating systems, web servers handling multiple client requests, and real-time systems requiring fair resource allocation.
                """),
                
                ("Shortest Job First (SJF)", """Shortest Job First is a scheduling algorithm that selects the waiting process with the smallest execution time.
                It has a time complexity of O(n²) in worst case for non-preemptive version and is optimal for minimizing average waiting time.
                
                **Time Complexity**: O(n²) for selection, O(n log n) if heap is used
                **Space Complexity**: O(n)
                
                **Key Parameters**:
                - Job execution time estimates
                
                **Advantages**:
                - Minimizes average waiting time
                - Maximizes throughput
                - Optimal when all jobs arrive simultaneously
                
                **Limitations**:
                - Potential starvation of longer processes
                - Requires prior knowledge of execution time
                - Not practical for interactive systems
                
                **Typical Applications**: Batch processing systems, background task processing, and offline job scheduling where execution times are known.
                """),
                
                ("Priority Scheduling", """Priority Scheduling assigns priority to each process, and processes are scheduled based on this priority.
                It has a time complexity of O(n log n) with proper data structures and is suitable for systems with varying task importance.
                
                **Time Complexity**: O(n log n) with a priority queue
                **Space Complexity**: O(n)
                
                **Key Parameters**:
                - Priority values for each task
                - Aging mechanism (to prevent starvation)
                
                **Advantages**:
                - Allows important tasks to be executed first
                - Can be preemptive or non-preemptive
                - Flexible priority assignment
                
                **Limitations**:
                - Potential starvation of low-priority tasks
                - Priority inversion issues
                - Requires overhead for priority management
                
                **Typical Applications**: Real-time systems, operating systems, industrial control systems, and mission-critical applications requiring task prioritization.
                """)
            ],
            
            'job sequencing': [
                ("Greedy Job Sequencing", """Greedy Job Sequencing arranges jobs to maximize profit/performance when each job has a deadline and profit.
                It has a time complexity of O(n²) or O(n log n) with efficient data structures, and is suitable for profit maximization within deadlines.
                
                **Time Complexity**: O(n log n) for sorting + O(n*d) for sequencing, where d is the maximum deadline
                **Space Complexity**: O(d)
                
                **Key Parameters**:
                - Job deadlines
                - Job profit/priority values
                
                **Advantages**:
                - Maximizes total profit/value
                - Works well with deadline constraints
                - Relatively simple implementation
                
                **Limitations**:
                - Not optimal for all scheduling scenarios
                - Doesn't handle job dependencies
                - Greedy approach might miss global optimum
                
                **Typical Applications**: Project management, manufacturing scheduling, and resource allocation with deadline constraints and varying values.
                """),
                
                ("Earliest Deadline First (EDF)", """Earliest Deadline First is a dynamic scheduling algorithm that prioritizes tasks with the earliest deadline.
                It has a time complexity of O(n log n) and is optimal for meeting deadlines in preemptive scheduling scenarios.
                
                **Time Complexity**: O(n log n) with a priority queue
                **Space Complexity**: O(n)
                
                **Key Parameters**:
                - Task deadlines
                - Task execution times
                
                **Advantages**:
                - Optimal for meeting deadlines in preemptive scheduling
                - Dynamic priority assignment
                - High processor utilization
                
                **Limitations**:
                - Not optimal for overloaded systems
                - Overhead for frequent priority recalculation
                - Susceptible to domino effect on deadline misses
                
                **Typical Applications**: Real-time operating systems, multimedia applications, telecommunication systems, and embedded systems with deadline requirements.
                """)
            ],
            
            'resource allocation': [
                ("Banker's Algorithm", """Banker's Algorithm is a resource allocation and deadlock avoidance algorithm that ensures the system never enters an unsafe state.
                It has a time complexity of O(n²m) where n is the number of processes and m is the number of resource types.
                
                **Time Complexity**: O(n²m)
                **Space Complexity**: O(n+m)
                
                **Key Parameters**:
                - Available resources
                - Maximum resource requirements for each process
                - Currently allocated resources
                
                **Advantages**:
                - Prevents deadlocks
                - Dynamic resource allocation
                - Safe resource management
                
                **Limitations**:
                - Requires advance knowledge of maximum resource needs
                - Conservative approach may underutilize resources
                - Computational overhead for large systems
                
                **Typical Applications**: Operating systems, cloud resource management, database transaction systems, and critical resource allocation scenarios.
                """),
                
                ("Min-Max Fair Allocation", """Min-Max Fair Allocation distributes resources fairly by maximizing the minimum allocation to any process.
                It has a time complexity typically of O(n log n) and is ideal for fair resource distribution.
                
                **Time Complexity**: O(n log n)
                **Space Complexity**: O(n)
                
                **Key Parameters**:
                - Available resources
                - Process resource requirements
                
                **Advantages**:
                - Provides fairness in resource allocation
                - Prevents resource starvation
                - Balances system-wide resource usage
                
                **Limitations**:
                - May not optimize for overall system performance
                - Complex implementation for multiple resource types
                - Doesn't account for different priorities
                
                **Typical Applications**: Network bandwidth allocation, cloud computing resource management, shared computing environments, and fair service distribution.
                """)
            ],
            
            'workflow scheduling': [
                ("Critical Path Method (CPM)", """Critical Path Method identifies the sequence of dependent tasks that form the longest path through a project.
                It has a time complexity of O(V+E) where V is the number of tasks and E is the number of dependencies.
                
                **Time Complexity**: O(V+E)
                **Space Complexity**: O(V+E)
                
                **Key Parameters**:
                - Task durations
                - Task dependencies (precedence constraints)
                
                **Advantages**:
                - Identifies critical tasks affecting project timeline
                - Determines minimum project completion time
                - Helps in resource allocation decision making
                
                **Limitations**:
                - Doesn't account for resource constraints
                - Deterministic approach without handling uncertainties
                - May not capture all real-world constraints
                
                **Typical Applications**: Project management, construction scheduling, manufacturing process planning, and any workflow with task dependencies.
                """),
                
                ("Heterogeneous Earliest Finish Time (HEFT)", """HEFT is a task scheduling algorithm for heterogeneous computing systems that aims to minimize execution time.
                It has a time complexity of O(V²×P) where V is the number of tasks and P is the number of processors.
                
                **Time Complexity**: O(V²×P)
                **Space Complexity**: O(V+P)
                
                **Key Parameters**:
                - Task execution times on different processors
                - Communication costs between tasks
                - Task dependencies
                
                **Advantages**:
                - Efficiently schedules tasks on heterogeneous resources
                - Considers both computation and communication costs
                - Good performance with reasonable complexity
                
                **Limitations**:
                - Heuristic approach, not guaranteed to be optimal
                - May not perform well with highly dynamic workloads
                - Limited consideration of resource contention
                
                **Typical Applications**: Grid computing, cloud computing, parallel computing systems, and distributed computing environments with varied processing resources.
                """)
            ],
            
            'real-time scheduling': [
                ("Rate Monotonic Scheduling (RMS)", """Rate Monotonic Scheduling is a preemptive static-priority scheduling algorithm where priorities are assigned based on task periods.
                It has a time complexity of O(n log n) for initial sorting and is optimal among fixed-priority algorithms.
                
                **Time Complexity**: O(n log n)
                **Space Complexity**: O(n)
                
                **Key Parameters**:
                - Task periods
                - Task execution times
                
                **Advantages**:
                - Optimal for fixed-priority preemptive scheduling
                - Simple priority assignment
                - Predictable behavior
                
                **Limitations**:
                - Utilization bound of n(2^(1/n) - 1) approaching 69% for large n
                - Not optimal for all real-time task sets
                - Sensitive to period variations
                
                **Typical Applications**: Hard real-time systems, embedded systems, automotive control systems, and aerospace applications with periodic tasks.
                """),
                
                ("Deadline Monotonic Scheduling (DMS)", """Deadline Monotonic Scheduling assigns priorities based on relative deadlines rather than periods.
                It has a time complexity of O(n log n) and is suitable for systems where deadlines differ from periods.
                
                **Time Complexity**: O(n log n)
                **Space Complexity**: O(n)
                
                **Key Parameters**:
                - Task deadlines
                - Task execution times
                
                **Advantages**:
                - Optimal when deadlines are less than or equal to periods
                - Accommodates varied deadline requirements
                - Static priority assignment
                
                **Limitations**:
                - Not optimal for arbitrary deadlines
                - Subject to utilization constraints
                - May require complex schedulability analysis
                
                **Typical Applications**: Hard real-time systems, control systems, and applications where task deadlines are different from their periods.
                """)
            ],
            
            'multiprocessor scheduling': [
                ("List Scheduling", """List Scheduling maintains a list of tasks sorted by priority and assigns them to the first available processor.
                It has a time complexity of O(n log n + nm) where n is the number of tasks and m is the number of processors.
                
                **Time Complexity**: O(n log n + nm)
                **Space Complexity**: O(n + m)
                
                **Key Parameters**:
                - Task priorities/weights
                - Task dependencies
                - Number of processors
                
                **Advantages**:
                - Simple implementation
                - Works well for independent tasks
                - Adaptable to different priority schemes
                
                **Limitations**:
                - May not produce optimal schedules
                - Performance depends on priority heuristic
                - Limited handling of complex constraints
                
                **Typical Applications**: Parallel computing environments, compute clusters, batch processing systems, and multi-core CPU scheduling.
                """),
                
                ("Work Stealing", """Work Stealing is a scheduling algorithm where idle processors 'steal' tasks from busy processors' queues.
                It has a time complexity that depends on implementation but exhibits good load balancing characteristics.
                
                **Time Complexity**: Varies based on workload, typically O(P × T/P + P log P) for P processors and T total work
                **Space Complexity**: O(P + T)
                
                **Key Parameters**:
                - Task division/chunking strategy
                - Work queue structure
                - Stealing policy
                
                **Advantages**:
                - Dynamic load balancing
                - Good cache locality
                - Adaptive to varying task complexities
                
                **Limitations**:
                - Synchronization overhead
                - Complex implementation
                - Performance depends on task granularity
                
                **Typical Applications**: Multi-core processors, parallel computing frameworks, thread pools, and dynamic workload environments.
                """)
            ],
            
            'stochastic scheduling': [
                ("Monte Carlo Scheduling", """Monte Carlo Scheduling uses probabilistic methods to estimate scheduling outcomes under uncertainty.
                It has a time complexity dependent on the number of simulations and is useful for scheduling under uncertainty.
                
                **Time Complexity**: O(S × n log n) where S is the number of simulations
                **Space Complexity**: O(n)
                
                **Key Parameters**:
                - Probability distributions of task durations
                - Number of simulations
                - Confidence level requirements
                
                **Advantages**:
                - Accounts for uncertainty in task durations
                - Provides probabilistic completion estimates
                - Can incorporate risk assessment
                
                **Limitations**:
                - Computationally intensive
                - Results are estimates rather than guarantees
                - Requires knowledge of statistical distributions
                
                **Typical Applications**: Project management with uncertainties, risk assessment, and scheduling under variable conditions.
                """),
                
                ("Q-Learning for Dynamic Scheduling", """Q-Learning applies reinforcement learning to scheduling decisions, learning optimal policies through experience.
                It has a variable time complexity depending on state-space size and is suitable for adaptive scheduling.
                
                **Time Complexity**: O(|S|²|A|) per episode, where |S| is the state space size and |A| is the action space size
                **Space Complexity**: O(|S||A|)
                
                **Key Parameters**:
                - Learning rate
                - Discount factor
                - Exploration strategy
                - State and action representations
                
                **Advantages**:
                - Adapts to changing conditions
                - Can optimize for multiple objectives
                - Improves over time through experience
                
                **Limitations**:
                - Requires training period
                - Large state spaces can be challenging
                - Complex to design appropriate rewards
                
                **Typical Applications**: Dynamic resource allocation, adaptive computing environments, and scheduling problems with changing patterns.
                """)
            ],
            
            'cloud scheduling': [
                ("Min-Min Algorithm", """Min-Min Algorithm schedules tasks with the minimum completion time first to appropriate resources.
                It has a time complexity of O(n²m) where n is the number of tasks and m is the number of resources.
                
                **Time Complexity**: O(n²m)
                **Space Complexity**: O(nm)
                
                **Key Parameters**:
                - Expected task completion times on each resource
                - Resource availability
                
                **Advantages**:
                - Minimizes makespan for small tasks
                - Simple implementation
                - Good resource utilization
                
                **Limitations**:
                - May delay longer tasks indefinitely
                - Not optimal for all workload types
                - Centralized decision making
                
                **Typical Applications**: Cloud computing task allocation, grid computing, and heterogeneous computing environments.
                """),
                
                ("Max-Min Algorithm", """Max-Min Algorithm prioritizes tasks with the maximum completion time, assigning them to their best resources first.
                It has a time complexity of O(n²m) where n is the number of tasks and m is the number of resources.
                
                **Time Complexity**: O(n²m)
                **Space Complexity**: O(nm)
                
                **Key Parameters**:
                - Expected task completion times on each resource
                - Resource availability
                
                **Advantages**:
                - Handles large tasks efficiently
                - Balances the execution of small and large tasks
                - Good for heterogeneous workloads
                
                **Limitations**:
                - May delay small tasks
                - Not optimal for all workload patterns
                - Requires accurate completion time estimates
                
                **Typical Applications**: Cloud resource allocation, grid computing, and environments with mixed task sizes.
                """)
            ],
            
            'dynamic scheduling': [
                ("Backfilling", """Backfilling allows smaller jobs to fill gaps in the schedule while ensuring priority jobs are not delayed.
                It has a time complexity of O(n log n) and is efficient for maximizing resource utilization.
                
                **Time Complexity**: O(n log n)
                **Space Complexity**: O(n)
                
                **Key Parameters**:
                - Resource requirements for each job
                - Job execution time estimates
                - Job priorities
                
                **Advantages**:
                - Improves resource utilization
                - Reduces waiting time for small jobs
                - Maintains priorities for important jobs
                
                **Limitations**:
                - Requires accurate runtime estimates
                - Implementation complexity
                - Potential for priority inversion
                
                **Typical Applications**: High-performance computing clusters, batch job scheduling, and supercomputing environments.
                """),
                
                ("Gang Scheduling", """Gang Scheduling coordinates the simultaneous scheduling of related tasks across multiple processors.
                It has a time complexity of O(npm) where n is tasks, p is phases, and m is processors.
                
                **Time Complexity**: O(npm)
                **Space Complexity**: O(nm)
                
                **Key Parameters**:
                - Task groupings/gangs
                - Time slice allocation
                - Process migration cost
                
                **Advantages**:
                - Reduces waiting time for communicating processes
                - Improves parallel application performance
                - Minimizes context switching overhead
                
                **Limitations**:
                - Complex implementation
                - Potential resource underutilization
                - Synchronization overhead
                
                **Typical Applications**: Parallel computing systems, high-performance computing clusters, and tightly coupled parallel applications.
                """)
            ],
            
            'energy-aware scheduling': [
                ("DVFS-based Scheduling", """Dynamic Voltage and Frequency Scaling scheduling adjusts processor frequency to balance performance and energy consumption.
                It has a time complexity of O(n log n) for basic implementations.
                
                **Time Complexity**: O(n log n)
                **Space Complexity**: O(n)
                
                **Key Parameters**:
                - Power-performance profiles
                - Task deadlines
                - Energy budget
                
                **Advantages**:
                - Reduces energy consumption
                - Adapts to varying workloads
                - Can maintain performance requirements
                
                **Limitations**:
                - Hardware support required
                - Complex optimization problem
                - Potential performance degradation
                
                **Typical Applications**: Mobile computing, battery-powered systems, data centers, and green computing environments.
                """),
                
                ("Sleep Scheduling", """Sleep Scheduling determines when to put resources into low-power states to conserve energy during idle periods.
                It has a variable time complexity depending on prediction algorithms used.
                
                **Time Complexity**: Varies, typically O(n) for greedy approaches
                **Space Complexity**: O(n)
                
                **Key Parameters**:
                - Idle period predictions
                - Power state transition costs
                - Wake-up time requirements
                
                **Advantages**:
                - Significant energy savings for periodic workloads
                - Simple implementation for basic approaches
                - Complementary to other energy-saving techniques
                
                **Limitations**:
                - Prediction errors can impact performance
                - Transition costs may offset savings
                - Not suitable for all workload patterns
                
                **Typical Applications**: Server farms, sensor networks, mobile devices, and IoT deployments with intermittent activity.
                """)
            ]
        }

    def get_recommendations(self, problem_description):
        """
        Analyze the problem description and return recommended algorithms.
        
        Args:
            problem_description (str): User's description of their scheduling problem
            
        Returns:
            list: List of (algorithm_name, description) tuples
        """
        problem_description = problem_description.lower()
        recommendations = []
        
        # Check for keywords in the problem description
        for category, algorithms in self.algorithm_recommendations.items():
            if category in problem_description:
                recommendations.extend(algorithms)
        
        # Additional specific keyword matching for better recommendations
        if "cpu" in problem_description or "process" in problem_description:
            if not any(algo[0] == "Round Robin (RR)" for algo in recommendations):
                recommendations.extend(self.algorithm_recommendations['task scheduling'])
                
        if "deadline" in problem_description:
            deadline_algos = [algo for algo in self.algorithm_recommendations['real-time scheduling'] 
                             if "Deadline" in algo[0]]
            recommendations.extend(deadline_algos)
            
        if "energy" in problem_description or "power" in problem_description:
            recommendations.extend(self.algorithm_recommendations['energy-aware scheduling'])
            
        if "cloud" in problem_description or "virtual" in problem_description:
            recommendations.extend(self.algorithm_recommendations['cloud scheduling'])
            
        if "parallel" in problem_description or "multiprocessor" in problem_description or "multi-core" in problem_description:
            recommendations.extend(self.algorithm_recommendations['multiprocessor scheduling'])
            
        if "uncertainty" in problem_description or "probabilistic" in problem_description:
            recommendations.extend(self.algorithm_recommendations['stochastic scheduling'])
            
        if "project" in problem_description or "workflow" in problem_description:
            recommendations.extend(self.algorithm_recommendations['workflow scheduling'])
            
        if "resource" in problem_description or "allocation" in problem_description:
            recommendations.extend(self.algorithm_recommendations['resource allocation'])
            
        if "adaptive" in problem_description or "dynamic" in problem_description:
            recommendations.extend(self.algorithm_recommendations['dynamic scheduling'])
            
        if "job" in problem_description and ("sequence" in problem_description or "order" in problem_description):
            recommendations.extend(self.algorithm_recommendations['job sequencing'])
        
        # Remove duplicates while preserving order
        unique_recommendations = []
        seen = set()
        for algo in recommendations:
            if algo[0] not in seen:
                unique_recommendations.append(algo)
                seen.add(algo[0])
        
        return unique_recommendations

# Interactive UI for the Scheduling Algorithm Recommender
def main():
    print("Welcome to the Scheduling Algorithm Recommender!")
    print("This tool helps you find the best scheduling algorithms for your specific needs.")
    print("\nPlease describe your scheduling problem with details about:")
    print("- Type of resources being scheduled (CPU, machines, projects, etc.)")
    print("- Constraints (deadlines, priorities, dependencies, etc.)")
    print("- Optimization goals (minimizing time, maximizing throughput, energy efficiency, etc.)")
    print("- Environment characteristics (real-time, cloud, multiprocessor, etc.)\n")
    
    problem_description = input("Problem description: ")
    
    recommender = SchedulingAlgorithmRecommender()
    recommendations = recommender.get_recommendations(problem_description)
    
    if recommendations:
        print("\n===== RECOMMENDED SCHEDULING ALGORITHMS =====\n")
        for i, (algo, description) in enumerate(recommendations, 1):
            print(f"{i}. {algo}")
            print("-" * len(algo))
            print(f"{description}\n")
    else:
        print("\nNo specific algorithm recommendations found for your description.")
        print("Try adding more details about the scheduling context, constraints, or goals.")

if __name__ == "__main__":
    main()
