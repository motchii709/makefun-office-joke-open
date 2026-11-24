import os

JOKE = "I declined the invite to the Meeting to Reduce Meetings, and my calendar congratulated me: the first action item this team has ever closed on time."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
