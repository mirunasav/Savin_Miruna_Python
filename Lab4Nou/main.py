class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"stack size: {stack.size()}")
print(f"peek: {stack.peek()}")
print(f"pop element: {stack.pop()}")
print(f"stack top after popping: {stack.peek()}")


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def poll(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def size(self):
        return len(self.items)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f"queue size: {queue.size()}")
print(f"peek: {queue.peek()}")
print(f"dequeue element: {queue.poll()}")
print(f"queue first element after dequeuing: {queue.peek()}")
print(f"poll element: {queue.poll()}")
print(f"poll element: {queue.poll()}")
print(f"poll element: {queue.poll()}")  # dequeue from empty queue


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.values = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        return self.values[row][col]

    def set(self, row, col, value):
        self.values[row][col] = value

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.cols != other.rows:
            print("cannot multiply these matrixes")
            return None

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.get(i, k) * other.get(k, j)
                result.set(i, j, total)
        return result

    def transform(self, transform_function):
        for i in range(self.rows):
            for j in range(self.cols):
                self.set(i, j, transform_function(self.get(i, j)))

    def __str__(self):
        matrix_str = ""
        for row in self.values:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str


matrix = Matrix(2, 3)

matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)

print(f"Matrix:\n{matrix}")
transposedMatrix = matrix.transpose()
print(f"Transposed matrix:\n{transposedMatrix}")

print(f"multitply matrix with its transpose:\n{matrix.multiply(transposedMatrix)}")

matrix.transform(lambda x: x+1)
print(f"matrix after increasing values with 1: \n{matrix}")
