# TODO решите задачу
import json
def task() -> float:
    with open("input.json") as f:
        data = json.load(f)
        mul = 0
        for obj in data:
            mul = obj["score"] * obj["weight"]+ mul
    return mul

print(round(task(),3))
