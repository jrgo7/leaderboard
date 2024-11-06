from tkinter import simpledialog
from tkinter import messagebox
import bisect
import json

msg = """Congratulations! You are a PTetriS Master!

Please enter some info for record keeping.
What is your """

while True:
    # Get entry
    name = simpledialog.askstring(title="PTetriS Leaderboard Entry", prompt=msg + "name?")
    score = simpledialog.askinteger(title="PTetriS Leaderboard Entry", prompt=msg + "score?")
    if messagebox.askquestion("Confirm", f"Name: {name}\nScore: {score}\nAre you sure?") == messagebox.YES:
        break

new_record = {"name": name, "score": score}

# Insert into leaderboard.json
try:
    with open("leaderboard.json", "r") as fp:
        leaderboard = json.load(fp)
    bisect.insort(leaderboard, new_record, key=lambda record: -record["score"])
    with open("leaderboard.json", "w") as fp:
        json.dump(leaderboard, fp)
except FileNotFoundError:
    with open("leaderboard.json", "w") as fp:
        json.dump([new_record], fp)

# Export as .txt
out = "LEADERBOARD"
for rank, entry in enumerate(leaderboard[:5], start=1):
    out += f"\n{rank} {entry['name'][:12]}\n        {entry['score']:05}\n"

with open("leaderboard.txt", 'w') as fp:
    fp.write(out)