from enum import Enum

class Status(Enum):
    INITIAL = "initial"
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    
    
class Task:
    status: Status = Status.INITIAL
    activity: str
    
    
def main():
    task = Task()
    task.status = Status.QUEUED,
    task.activity = "some activity"
    print(type(task.status))
    print(task.status)
    # print(task.status.value) # fails because task.status is a tuple not a Status object 
    # https://github.com/python/cpython/issues/100098

    
if __name__ == "__main__":
    main()