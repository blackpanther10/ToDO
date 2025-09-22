from src.utils import add_task, list_tasks

def test_add_task():
    add_task("Test tâche")
    assert "Test tâche" in list_tasks()
