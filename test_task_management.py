import unittest
from io import StringIO
from unittest.mock import patch
from datetime import datetime
import task_management


# Assuming your functions are in a module named task_manager.py

class TestTaskManagerFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # This will be called once before running any tests
        pass

    @classmethod
    def tearDownClass(cls):
        # This will be called once after running all tests
        pass

    def setUp(self):
        # This will be called before each test
        self.test_task_name = "Test Task"
        self.test_priority = "High"
        self.test_due_date = "2024-01-30"
        self.test_category = "Test Category"
        self.sample_task = {
            'name': 'Sample Task',
            'created_at': str(datetime.now()),
            'completed': False
        }

    def tearDown(self):
        # This will be called after each test
        pass

    def test_add_task(self):
        with patch('builtins.input', return_value=self.test_task_name):
            task_management.add_task(self.test_task_name)
        self.assertEqual(task_management.tasks[-1]['name'], self.test_task_name)

    def test_mark_completed(self):
        task_management.tasks.append(self.sample_task)
        with patch('builtins.input', return_value=self.sample_task['name']):
            task_management.mark_completed(self.sample_task['name'])
        self.assertTrue(task_management.tasks[-1]['completed'])

    def test_prioritize_task(self):
        task_management.tasks.append(self.sample_task)
        with patch('builtins.input', side_effect=[self.sample_task['name'], self.test_priority]):
            task_management.prioritize_task(self.sample_task['name'], self.test_priority)
        self.assertEqual(task_management.tasks[-1]['priority'], self.test_priority)

    def test_set_due_date(self):
        task_management.tasks.append(self.sample_task)
        with patch('builtins.input', side_effect=[self.sample_task['name'], self.test_due_date]):
            task_management.set_due_date(self.sample_task['name'], self.test_due_date)
        self.assertEqual(task_management.tasks[-1]['due_date'], self.test_due_date)

    def test_categorize_task(self):
        task_management.tasks.append(self.sample_task)
        with patch('builtins.input', side_effect=[self.sample_task['name'], self.test_category]):
            task_management.categorize_task(self.sample_task['name'], self.test_category)
        self.assertEqual(task_management.tasks[-1]['category'], self.test_category)

    def test_show_tasks(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            task_management.show_tasks()
            self.assertIn("Task List", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
