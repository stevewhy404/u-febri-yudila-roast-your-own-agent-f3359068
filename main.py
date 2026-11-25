import os

LINE = "My agent apologized for the bug, fixed it in three places, and the bug is still there \u2014 but the apology was flawless."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
