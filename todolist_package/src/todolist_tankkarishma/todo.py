class Todo:
    COMPLETED_SYMBOL = 'X'
    NOT_COMPLETED_SYMBOL = " "

    def __init__(self, name):
        self._title = name
        self.done = False

    @property
    def title(self):
        return self._title
    
    @property
    def done(self):
        return self._is_completed
    
    @done.setter
    def done(self, status):
        if not isinstance(status, bool):
            raise TypeError("Status must be True or False.")
        self._is_completed = status

    def __str__(self):
        completed_char = Todo.COMPLETED_SYMBOL if self.done else Todo.NOT_COMPLETED_SYMBOL
        return f"[{completed_char}] {self.title}"
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        
        return self.title == other.title and self.done == other.done

# # Test code for Todo
# def test_todo():
#     todo1 = Todo('Buy milk')
#     todo2 = Todo('Clean room')
#     todo3 = Todo('Go to gym')
#     todo4 = Todo('Clean room')

#     print(todo1)                  # [ ] Buy milk
#     print(todo2)                  # [ ] Clean room
#     print(todo3)                  # [ ] Go to gym
#     print(todo4)                  # [ ] Clean room

#     print(todo2 == todo4)         # True
#     print(todo1 == todo2)         # False
#     print(todo4.done)             # False

#     todo1.done = True
#     todo4.done = True
#     print(todo4.done)             # True

#     print(todo1)                  # [X] Buy milk
#     print(todo2)                  # [ ] Clean room
#     print(todo3)                  # [ ] Go to gym
#     print(todo4)                  # [X] Clean room

#     print(todo2 == todo4)         # False

#     todo4.done = False
#     print(todo4.done)             # False
#     print(todo4)                  # [ ] Clean room

# test_todo()