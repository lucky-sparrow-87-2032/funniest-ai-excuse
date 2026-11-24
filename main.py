import os

LINE = "I finished your task, but the other 47 open tabs got jealous and staged a walkout, taking it with them."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
