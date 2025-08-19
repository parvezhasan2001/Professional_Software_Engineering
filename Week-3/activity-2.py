# Week-3 Activity-2

class DataProcessing:
    def __init__(self, filename):
        self.filename = filename

    def count_words(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            count = 0
            for line in file:
                words = line.strip().split()
                count += len(words)
            return count


def main():
    demoFile = DataProcessing("demo_file.txt")
    print(f"total number of words in file: {demoFile.count_words()} words")


if __name__ == "__main__":
    main()