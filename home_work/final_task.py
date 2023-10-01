print("--------------------Первое задание----------------------")
#1
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


class TaskManager:
    def __init__(self):
        self.task_stack = Stack()

    def new_task(self, task, priority):
        for index, (existing_task, existing_priority) in enumerate(self.task_stack.stack):
            if existing_task == task:
                if priority < existing_priority:
                    self.task_stack.stack[index] = (task, priority)
                print(f"Дубликат задачи '{task}'. Оставлен дубль с большим приоритетом.")

        return self.task_stack.push((task, priority))

    def str(self):
        sorted_tasks = sorted(self.task_stack.stack, key=lambda x: x[1])
        tasks_by_priority = {}
        for task, priority in sorted_tasks:
            if priority in tasks_by_priority:
                tasks_by_priority[priority].append(task)
            else:
                tasks_by_priority[priority] = [task]

        result = ''
        for priority, tasks in tasks_by_priority.items():
            result += f"{priority} {'; '.join(tasks)}\n"

        return result


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("поесть", 4)
manager.new_task("сдать дз", 2)
print(manager.str())


#2
print("--------------------Второе задание----------------------")


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_dict = {}

    @property
    def cache(self):
        return next(iter(self.cache_dict.items()))[0] if self.cache_dict else None

    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        if key in self.cache_dict:
            self.cache_dict.pop(key)
        elif len(self.cache_dict) >= self.capacity:
            self.cache_dict.pop(next(iter(self.cache_dict)))

        self.cache_dict[key] = value

    def get(self, key):
        if key in self.cache_dict:
            value = self.cache_dict.pop(key)
            self.cache_dict[key] = value
            return value
        else:
            return None

    def print_cache(self):
        print("LRU Cache:")
        for key, value in self.cache_dict.items():
            print(f"{key} : {value}")


cache = LRUCache(3)

cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

cache.print_cache()

print(cache.get("key2"))


#3
print("--------------------Третье задание----------------------")


def cache_check(func):
    cache_fibo = {}

    def wrapper(*args):
        if args in cache_fibo:
            return cache_fibo[args]
        result = func(*args)
        cache_fibo[args] = result
        return result

    return wrapper


@cache_check
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(3))


#4
print("--------------------Четвертое задание----------------------")


class Cell:

    def __init__(self, number):
        self.number = number
        self.value = ' '

    def is_empty(self):
        return self.value == ' '


class Board:
    def __init__(self):
        self.cells = []
        for i in range(1, 10):
            self.cells.append(Cell(i))

    def display(self):
        for i in range(0, 9, 3):
            print(f'{self.cells[i].value} | {self.cells[i + 1].value} | {self.cells[i + 2].value}')
            if i < 6:
                print('---------')

    def is_full(self):
        for cell in self.cells:
            if cell.is_empty():
                return False
        return True

    def check_winner(self, player):
        patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                    [0, 3, 6], [1, 4, 7], [2, 5, 8],
                    [0, 4, 8], [2, 4, 6]]

        for pattern in patterns:
            a, b, c = pattern
            if self.cells[a].value == self.cells[b].value == self.cells[c].value == player.symbol:
                return True
        return False

    def make_move(self, cell_number, player):
        if not 1 <= cell_number <= 9:
            print("Некорректный номер клетки")
            return False

        cell = self.cells[cell_number - 1]
        if not cell.is_empty():
            print("Клетка занята")
            return False

        cell.value = player.symbol
        return True


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


def play_game():
    board = Board()

    player1 = Player("Игрок 1", "X")
    player2 = Player("Игрок 2", "O")

    current_player = player1

    while True:
        board.display()

        cell_number = int(input(f'{current_player.name}, выберите номер клетки для хода: '))

        if board.make_move(cell_number, current_player):
            if board.check_winner(current_player):
                board.display()
                print(f'{current_player.name} победил!')
                break

            if board.is_full():
                board.display()
                print("Ничья!")
                break

            current_player = player2 if current_player == player1 else player1


play_game()
