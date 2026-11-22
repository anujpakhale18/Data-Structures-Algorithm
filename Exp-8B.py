from collections import deque


class Graph:
    def __init__(self, users):
        self.users = users
        self.adj = [[] for _ in range(users)]

    def add_friendship(self, user1, user2):
        # Undirected friendship: store the connection in both lists.
        self.adj[user1].append(user2)
        self.adj[user2].append(user1)

    def display_network(self):
        print("\nFriendship Network (Adjacency List):")
        for user in range(self.users):
            print(f"{user} -> {self.adj[user]}")

    def bfs_level_by_level(self, start_user):
        if start_user < 0 or start_user >= self.users:
            print("Invalid starting user.")
            return

        visited = [False] * self.users
        queue = deque([start_user])
        visited[start_user] = True
        level = 0

        while queue:
            level_size = len(queue)
            print(f"Level {level}: ", end="")

            for _ in range(level_size):
                user = queue.popleft()
                print(user, end=" ")

                # Visit friends in ascending order.
                for friend in sorted(self.adj[user]):
                    if not visited[friend]:
                        visited[friend] = True
                        queue.append(friend)

            print()
            level += 1


def main():
    users = int(input("Enter number of users: "))

    if users <= 0:
        print("Number of users must be greater than zero.")
        return

    network = Graph(users)

    friendships = int(input("Enter number of friendships: "))

    if friendships < 0:
        print("Number of friendships cannot be negative.")
        return

    print("Enter each friendship as user1 and user2 (0 to",
          users - 1, "):")

    for i in range(friendships):
        user1, user2 = map(
            int, input(f"Friendship {i + 1}: ").split()
        )

        if (0 <= user1 < users and
                0 <= user2 < users):
            network.add_friendship(user1, user2)
        else:
            print("Invalid friendship. Please enter valid user numbers.")
            return

    network.display_network()

    start = int(input("\nEnter starting user for BFS: "))

    print("\nBFS Level-by-Level:")
    network.bfs_level_by_level(start)


if __name__ == "__main__":
    main()