from utils import add_task, list_tasks

if __name__ == "__main__":
    add_task("Apprendre Git")
    add_task("Écrire des tests")
    print("Tâches actuelles :", list_tasks())
