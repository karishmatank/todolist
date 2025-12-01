import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        new_list = self.todos.to_list()
        self.assertIsInstance(new_list, list)
        self.assertEqual([self.todo1, self.todo2, self.todo3], new_list)

    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())

    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())

    def test_all_done(self):
        self.assertFalse(self.todos.all_done())

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add('todo')
        with self.assertRaises(TypeError):
            self.todos.add(TodoList("New Todos"))

    def test_todo_at(self):
        self.assertEqual(self.todo1, self.todos.todo_at(0))
        self.assertEqual(self.todo2, self.todos.todo_at(1))
        self.assertEqual(self.todo3, self.todos.todo_at(2))
        with self.assertRaises(IndexError):
            self.todos.todo_at(3)

    def test_mark_done_at(self):
        self.todos.mark_done_at(0)
        self.assertTrue(self.todo1.done)

        with self.assertRaises(IndexError):
            self.todos.mark_done_at(3)

        self.assertFalse(self.todo2.done)

    def test_mark_undone_at(self):
        self.todos.mark_undone_at(0)
        self.assertFalse(self.todo1.done)

        self.todos.mark_done_at(1)
        self.todos.mark_undone_at(1)
        self.assertFalse(self.todo2.done)

        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(3)

    def test_mark_all_done(self):
        self.todos.mark_all_done()
        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertTrue(self.todo3.done)

    def test_remove_at(self):
        with self.assertRaises(IndexError):
            self.todos.remove_at(5)
        
        self.todos.remove_at(0)
        self.assertNotIn(self.todo1, self.todos.to_list())

    def test_str(self):
        string = (
            "---- Today's Todos ----\n"
            "[ ] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym\n"
        )

        self.assertEqual(string, str(self.todos))

    def test_str_done_todo(self):
        self.todos.mark_done_at(0)

        string = (
            "---- Today's Todos ----\n"
            "[X] Buy milk\n"
            "[ ] Clean room\n"
            "[ ] Go to the gym\n"
        )

        self.assertEqual(string, str(self.todos))

    def test_str_all_done_todos(self):
        self.todos.mark_all_done()

        string = (
            "---- Today's Todos ----\n"
            "[X] Buy milk\n"
            "[X] Clean room\n"
            "[X] Go to the gym\n"
        )

        self.assertEqual(string, str(self.todos))

    def test_each(self):
        self.tracker = 0
        def increment_tracker(todo):
            self.tracker += 1

        self.todos.each(increment_tracker)
        self.assertEqual(3, self.tracker)

    def test_select(self):
        todo_name = "Buy milk"
        new_list = self.todos.select(lambda todo: todo.title == todo_name).to_list()
        self.assertEqual([self.todo1], new_list)


if __name__ == '__main__':
    unittest.main()