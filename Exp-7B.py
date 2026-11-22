class Graph:
    def __init__(self, locations):
        self.locations = locations
        self.adj = [[0 for _ in range(locations)]
                    for _ in range(locations)]
        self.visited = [False] * locations

    def add_road(self, source, destination):
        # Undirected road network: update both directions.
        self.adj[source][destination] = 1
        self.adj[destination][source] = 1

    def display_network(self):
        print("\nRoad Network Adjacency Matrix:")
        print("  ", *range(self.locations))

        for i in range(self.locations):
            print(i, self.adj[i])

    def dfs_util(self, location, traversal):
        self.visited[location] = True
        traversal.append(location)

        # Explore connected locations in ascending order.
        for neighbour in range(self.locations):
            if (self.adj[location][neighbour] == 1
                    and not self.visited[neighbour]):
                self.dfs_util(neighbour, traversal)

    def dfs(self, start_location):
        if (start_location < 0 or
                start_location >= self.locations):
            print("Invalid starting location.")
            return []

        self.visited = [False] * self.locations
        traversal = []

        self.dfs_util(start_location, traversal)

        return traversal


def main():
    locations = int(input("Enter number of locations: "))

    if locations <= 0:
        print("Number of locations must be greater than zero.")
        return

    network = Graph(locations)

    roads = int(input("Enter number of roads: "))

    if roads < 0:
        print("Number of roads cannot be negative.")
        return

    print("Enter each road as source and destination (0 to",
          locations - 1, "):")

    for i in range(roads):
        source, destination = map(
            int, input(f"Road {i + 1}: ").split()
        )

        if (0 <= source < locations and
                0 <= destination < locations):
            network.add_road(source, destination)
        else:
            print("Invalid road. Please enter valid location numbers.")
            return

    network.display_network()

    start = int(input("\nEnter starting location for DFS: "))
    traversal = network.dfs(start)

    if traversal:
        print("DFS Road Exploration:",
              " -> ".join(map(str, traversal)))

        if len(traversal) < locations:
            print("Unconnected locations:",
                  *[location for location in range(locations)
                    if location not in traversal])


if __name__ == "__main__":
    main()