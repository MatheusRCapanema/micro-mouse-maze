import random

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}

    def has_unvisited_neighbors(self, grid):
        neighbors = []
        
        if self.x > 0:
            top = grid[self.x - 1][self.y]
            if not top.visited:
                neighbors.append(("top", top))
        
        if self.y < len(grid[0]) - 1:
            right = grid[self.x][self.y + 1]
            if not right.visited:
                neighbors.append(("right", right))
                
        if self.x < len(grid) - 1:
            bottom = grid[self.x + 1][self.y]
            if not bottom.visited:
                neighbors.append(("bottom", bottom))
        
        if self.y > 0:
            left = grid[self.x][self.y - 1]
            if not left.visited:
                neighbors.append(("left", left))
        
        return neighbors

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(x, y) for y in range(cols)] for x in range(rows)]
        self.current_cell = self.grid[0][0]
        self.stack = []

    def generate_maze(self):
        self.current_cell.visited = True
        self.stack.append(self.current_cell)

        while len(self.stack) > 0:
            cell = self.stack[-1]
            neighbors = cell.has_unvisited_neighbors(self.grid)

            if len(neighbors) == 0:
                self.stack.pop()
            else:
                direction, next_cell = random.choice(neighbors)
                self.remove_wall(cell, next_cell, direction)
                next_cell.visited = True
                self.stack.append(next_cell)

    def remove_wall(self, current, next, direction):
        if direction == "top":
            current.walls["top"] = False
            next.walls["bottom"] = False
        elif direction == "right":
            current.walls["right"] = False
            next.walls["left"] = False
        elif direction == "bottom":
            current.walls["bottom"] = False
            next.walls["top"] = False
        elif direction == "left":
            current.walls["left"] = False
            next.walls["right"] = False

    def get_graph_representation(self):
        # Representação do labirinto como um grafo.
        graph = {}
        for row in self.grid:
            for cell in row:
                cell_id = cell.x * self.cols + cell.y
                graph[cell_id] = []

                if not cell.walls["top"] and cell.x > 0:
                    graph[cell_id].append((cell.x - 1) * self.cols + cell.y)
                if not cell.walls["right"] and cell.y < self.cols - 1:
                    graph[cell_id].append(cell.x * self.cols + (cell.y + 1))
                if not cell.walls["bottom"] and cell.x < self.rows - 1:
                    graph[cell_id].append((cell.x + 1) * self.cols + cell.y)
                if not cell.walls["left"] and cell.y > 0:
                    graph[cell_id].append(cell.x * self.cols + (cell.y - 1))
                
        return graph

maze = Maze(10, 10)
maze.generate_maze()
print(maze.get_graph_representation())
