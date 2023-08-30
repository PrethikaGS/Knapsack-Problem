import heapq
def knapsack_bf_bb(capacity, weights, values):
    """
    Best-First Branch-and-Bound algorithm for the 0-1 Knapsack problem.
    capacity: maximum weight capacity of the knapsack
    weights: list of weights of the items
    values: list of values of the items
    """
    # Calculate the bound for the root node
    bound = bound_value(capacity, weights, values)
    
    # Initialize the priority queue with the root node
    queue = [(-bound, 0, 0, [])]
    
    # Initialize the best solution found so far
    best_value = 0
    best_subset = []
    
    # Explore the search tree using Best-First Branch-and-Bound
    while queue:
        # Get the node with the highest priority (i.e., lowest bound)
        _, weight, value, subset = heapq.heappop(queue)
        
        # Check if this node represents a complete solution
        if weight > capacity:
            continue
        
        # Check if this node represents a new best solution
        if value > best_value:
            best_value = value
            best_subset = subset
        
        # Expand the node by considering the next item
        if len(subset) < len(weights):
            # Include the next item
            include_weight = weight + weights[len(subset)]
            include_value = value + values[len(subset)]
            include_subset = subset + [1]
            include_bound = bound_value(capacity - include_weight, weights[len(subset)+1:], values[len(subset)+1:]) + include_value
            heapq.heappush(queue, (-include_bound, include_weight, include_value, include_subset))
            
            # Exclude the next item
            exclude_weight = weight
            exclude_value = value
            exclude_subset = subset + [0]
            exclude_bound = bound_value(capacity - exclude_weight, weights[len(subset)+1:], values[len(subset)+1:]) + exclude_value
            heapq.heappush(queue, (-exclude_bound, exclude_weight, exclude_value, exclude_subset))
            
    return (best_value, best_subset)

def bound_value(capacity, weights, values):
    """
    Calculate the bound for a node in the search tree.
    """
    bound = 0
    for i in range(len(weights)):
        if weights[i] <= capacity:
            bound += values[i]
            capacity -= weights[i]
        else:
            bound += values[i] * (capacity / weights[i])
            break
    return bound
capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]
best_value, best_subset = knapsack_bf_bb(capacity, weights, values)
print("Best value:", best_value)
print("Best subset:", best_subset)
