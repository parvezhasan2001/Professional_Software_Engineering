# Week-3 Activity-1

class DataProcessing:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_file(self, content):
        file = open(self.file_path, "w", encoding="UTF-8")
        file.write(content)
        file.close()
        print("Content written successfully.")

    def read_file(self):
        file = open(self.file_path, "r", encoding="UTF-8")
        data = file.read()
        file.close()
        return data


# Example usage
if __name__ == "__main__":
    file_handler = DataProcessing("Week3/demo.txt")

    # Read current txt
    content1 = file_handler.read_file()
    print("content of the file: \n",content1)

    # Write to the file
    file_handler.write_file("Hello, this is a new line in the file.\nThis is another line.")