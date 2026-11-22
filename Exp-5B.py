class Node:
    def __init__(self, admission_no, name, course):
        self.admission_no = admission_no
        self.name = name
        self.course = course
        self.left = None
        self.right = None


class StudentAdmissionBST:
    def __init__(self):
        self.root = None

    def insert(self, admission_no, name, course):
        new_node = Node(admission_no, name, course)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if admission_no < current.admission_no:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif admission_no > current.admission_no:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            else:
                print(f"Admission number {admission_no} already exists.")
                return

    def inorder_non_recursive(self):
        stack = []
        current = self.root
        result = []

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(
                (current.admission_no, current.name, current.course)
            )
            current = current.right

        return result

    def preorder_non_recursive(self):
        if self.root is None:
            return []

        stack = [self.root]
        result = []

        while stack:
            current = stack.pop()
            result.append(
                (current.admission_no, current.name, current.course)
            )

            # Push right first so that left is processed first.
            if current.right is not None:
                stack.append(current.right)

            if current.left is not None:
                stack.append(current.left)

        return result


def main():
    tree = StudentAdmissionBST()

    n = int(input("Enter number of students: "))

    if n < 0:
        print("Number of students cannot be negative.")
        return

    for i in range(n):
        print(f"\nEnter details of student {i + 1}:")
        admission_no = int(input("Enter admission number: "))
        name = input("Enter student name: ")
        course = input("Enter course: ")

        tree.insert(admission_no, name, course)

    print("\nInorder Traversal (Non-Recursive):")
    for record in tree.inorder_non_recursive():
        print(
            "Admission No:", record[0],
            "| Name:", record[1],
            "| Course:", record[2]
        )

    print("\nPreorder Traversal (Non-Recursive):")
    for record in tree.preorder_non_recursive():
        print(
            "Admission No:", record[0],
            "| Name:", record[1],
            "| Course:", record[2]
        )


if __name__ == "__main__":
    main()