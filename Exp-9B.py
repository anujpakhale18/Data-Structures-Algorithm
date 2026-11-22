class Graph:
    def __init__(self, substations):
        self.substations = substations
        self.adj = [
            [0 for _ in range(substations)]
            for _ in range(substations)
        ]

    def add_connection(self, source, destination, cost):
        # Undirected weighted graph.
        self.adj[source][destination] = cost
        self.adj[destination][source] = cost

    def display_network(self):
        print("\nPower Distribution Weighted Adjacency Matrix:")
        print("   ", *range(self.substations))

        for i in range(self.substations):
            print(i, self.adj[i])

    def prim_mst(self, start):
        if start < 0 or start >= self.substations:
            print("Invalid starting substation.")
            return

        INF = float("inf")
        key = [INF] * self.substations
        parent = [-1] * self.substations
        in_mst = [False] * self.substations

        key[start] = 0

        for _ in range(self.substations):
            # Select the unvisited substation with minimum connection cost.
            min_key = INF
            u = -1

            for v in range(self.substations):
                if not in_mst[v] and key[v] < min_key:
                    min_key = key[v]
                    u = v

            # No reachable unvisited substation means the network is disconnected.
            if u == -1:
                print("Power distribution network is disconnected.")
                print("All substations cannot be connected.")
                return

            in_mst[u] = True

            # Update connection costs of adjacent substations.
            for v in range(self.substations):
                cost = self.adj[u][v]

                if (cost > 0 and not in_mst[v]
                        and cost < key[v]):
                    key[v] = cost
                    parent[v] = u

        print("\nMinimum Spanning Tree (MST):")
        print("Connection\tWiring Cost")

        total_cost = 0

        for v in range(self.substations):
            if parent[v] != -1:
                cost = self.adj[v][parent[v]]
                print(f"{parent[v]} - {v}\t\t{cost}")
                total_cost += cost

        print("Total Minimum Wiring Cost:", total_cost)


def main():
    substations = int(input("Enter number of substations: "))

    if substations <= 0:
        print("Number of substations must be greater than zero.")
        return

    network = Graph(substations)

    connections = int(input("Enter number of possible connections: "))

    if connections < 0:
        print("Number of connections cannot be negative.")
        return

    print("Enter each connection as: source destination wiring_cost")
    print(f"Valid substations: 0 to {substations - 1}")

    for i in range(connections):
        source, destination, cost = map(
            int, input(f"Connection {i + 1}: ").split()
        )

        if not (0 <= source < substations and
                0 <= destination < substations):
            print("Invalid substation number.")
            return

        if source == destination:
            print("Connection between the same substation is not allowed.")
            return

        if cost <= 0:
            print("Wiring cost must be positive.")
            return

        network.add_connection(source, destination, cost)

    network.display_network()

    start = int(input(
        "\nEnter starting substation for Prim's algorithm: "
    ))

    network.prim_mst(start)


if __name__ == "__main__":
    main()