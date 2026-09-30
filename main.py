class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recoverFromPreorder(traversal):
    stack = []

    i = 0

    while i < len(traversal):

        # Рахуємо кількість тире
        depth = 0

        while i < len(traversal) and traversal[i] == "-":
            depth += 1
            i += 1

        # Зчитуємо значення вузла
        value = 0

        while i < len(traversal) and traversal[i].isdigit():
            value = value * 10 + int(traversal[i])
            i += 1

        node = TreeNode(value)

        # Повертаємося до батьківського вузла
        while len(stack) > depth:
            stack.pop()

        # Якщо є батько
        if stack:
            parent = stack[-1]

            if parent.left is None:
                parent.left = node
            else:
                parent.right = node

        # Додаємо поточний вузол у стек
        stack.append(node)

    return stack[0]


def treeToList(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)

        if node is None:
            result.append(None)
            continue

        result.append(node.val)

        queue.append(node.left)
        queue.append(node.right)

    # Видаляємо зайві None в кінці
    while result and result[-1] is None:
        result.pop()

    return result


# Приклад 1
traversal1 = "1-2--3--4-5--6--7"

root1 = recoverFromPreorder(traversal1)

print("Приклад 1:")
print(treeToList(root1))


# Приклад 2
traversal2 = "1-2--3---4-5--6---7"

root2 = recoverFromPreorder(traversal2)

print("Приклад 2:")
print(treeToList(root2))


# Приклад 3
traversal3 = "1-401--349---90--88"

root3 = recoverFromPreorder(traversal3)

print("Приклад 3:")
print(treeToList(root3))