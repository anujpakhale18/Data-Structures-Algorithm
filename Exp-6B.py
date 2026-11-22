from collections import deque


class Node:
    def __init__(self, employee_id):
        self.employee_id = employee_id
        self.left = None
        self.right = None


class EmployeeBST:
    def __init__(self):
        self.root = None

    def insert(self, employee_id):
        new_node = Node(employee_id)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if employee_id < current.employee_id:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif employee_id > current.employee_id:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            else:
                print(f"Duplicate employee ID {employee_id} ignored.")
                return

    def level_order(self):
        if self.root is None:
            print("Tree is empty.")
            return

        queue = deque([self.root])
        level = 0

        while queue:
            level_size = len(queue)
            print(f"Level {level}: ", end="")

            for _ in range(level_size):
                node = queue.popleft()
                print(node.employee_id, end=" ")

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            print()
            level += 1

    def height(self, node):
        # Height is measured in edges.
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def print_leaf_nodes(self, node):
        if node is None:
            return

        if node.left is None and node.right is None:
            print(node.employee_id, end=" ")
            return

        self.print_leaf_nodes(node.left)
        self.print_leaf_nodes(node.right)


def main():
    employee_tree = EmployeeBST()

    n = int(input("Enter number of employees: "))

    if n < 0:
        print("Number of employees cannot be negative.")
        return

    for i in range(n):
        employee_id = int(input(f"Enter employee ID {i + 1}: "))
        employee_tree.insert(employee_id)

    print("\nEmployee BST - Level-wise:")
    employee_tree.level_order()

    print("\nHeight of Employee BST (in edges):",
          employee_tree.height(employee_tree.root))

    print("Leaf Nodes of Employee BST: ", end="")
    employee_tree.print_leaf_nodes(employee_tree.root)
    print()


if __name__ == "__main__":
    main()