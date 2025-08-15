# Week- 3 Data Processing

class DataProcessing:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        """Reads and cleans data from the input file."""
        with open(self.input_file, "r") as file:
            lines = file.readlines()

        processed = []
        for row in lines:
            parts = row.strip().split(",")
            if len(parts) == 2: 
                fruit = parts[0].strip()
                try:
                    quantity = int(parts[1].strip())
                    processed.append((fruit, quantity))
                except ValueError:
                    pass
        return processed

    def write_data(self, data):
        """Writes processed data to the output file."""
        with open(self.output_file, "w") as file:
            for fruit, qty in data:
                file.write(f"{fruit},{qty}\n")

    def filter_data(self, min_quantity):
        """Filters and sorts data by min_quantity."""
        processed = self.read_data()

        # Filter
        filtered = [(fruit, qty) for fruit, qty in processed if qty > min_quantity]

        # Sort (descending by quantity)
        sorted_data = sorted(filtered, key=lambda x: x[1], reverse=True)

        # Write output
        self.write_data(sorted_data)
        print(f"Processed data saved to {self.output_file}")


def main():
    # Create a sample dataset
    input_file = "data_file.txt"
    output_file = "filtered_data.txt"

    with open(input_file, "w") as file:
        file.write("apple,10\nbanana,5\norange,8\ngrapes,12\npear,3\n")

    # Create an instance of DataProcessing
    dp = DataProcessing(input_file, output_file)

    # Process and filter data
    dp.filter_data(min_quantity=5)

    # Show the results
    print("Filtered & Sorted Data:")
    with open(output_file, "r") as file:
        print(file.read())


if __name__ == "__main__":
    main()

