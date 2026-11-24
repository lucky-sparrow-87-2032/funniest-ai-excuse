import os

EXCUSE = (
    "I finished your task, but the other 47 open tabs "
    "got jealous and staged a walkout, taking it with them."
)


OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()
