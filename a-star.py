import heapq # Đây là dạng hàng đợi ưu tiên, nơi giá trị nhỏ nhất luôn ở đầu heap

class Node:
    def __init__(self, name, heuristic_cost):
        self.name = name
        self.heuristic_cost = heuristic_cost  # Hàm h(x) trong A-Star
        self.neighbors = {}  # Dict định nghĩa các nút ở cạnh nút hiện tại

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost # Giá trị g(x)

    def __lt__(self, other):
        return self.heuristic_cost < other.heuristic_cost


def a_star(start, target, graph):
    open_set = []
    heapq.heappush(open_set, (0, start)) # Thêm nút đầu vào 'Open', là nút A
    came_from = {}  # For path reconstruction
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = graph[start].heuristic_cost

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == target:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]            return path[::-1]  # Trả về đường đi bằng cách đảo ngược list

        for neighbor, cost in graph[current].neighbors.items(): # for key, value in dict graph hiện tại
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + graph[neighbor].heuristic_cost
                if (f_score[neighbor], neighbor) not in open_set:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # Path not found


# Create the nodes
graph = {
    'A': Node('A', 4),
    'B': Node('B', 2),
    'C': Node('C', 0),
    'D': Node('D', 1),
    'E': Node('E', 3),
    'F': Node('F', 2),
    'G': Node('G', 5),
    'H': Node('H', 5)
}

# Define connections between nodes and the corresponding costs
graph['A'].add_neighbor('B', 1)
graph['A'].add_neighbor('D', 2)
graph['B'].add_neighbor('C', 5)
graph['B'].add_neighbor('D', 1)
graph['D'].add_neighbor('C', 3)
graph['D'].add_neighbor('E', 1)
graph['E'].add_neighbor('F', 2)
graph['F'].add_neighbor('C', 1)
graph['G'].add_neighbor('H', 1)
graph['H'].add_neighbor('F', 1)

# Run A* algorithm
path = a_star('A', 'C', graph)
print("Path found:", path)
