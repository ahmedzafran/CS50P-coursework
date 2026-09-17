import csv, sys


def main():
    if 2 < len(sys.argv) < 4:
        file_name, output_name = sys.argv[1], sys.argv[2]
        if file_name.endswith(".csv"):
            try:
                preprocess(file_name, output_name)
            except ValueError as e:
                sys.exit(e)
        else:
            sys.exit("Not a CSV file")
    else:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")




def preprocess(file_name, output_name):
    try:
        with open(file_name, mode='r', newline='') as infile:
            reader = csv.DictReader(infile)
            with open(output_name, mode='w', newline='') as outfile:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    last, first = [name.strip() for name in row['name'].split(',')]
                    writer.writerow({'first': first, 'last': last, 'house': row['house']})
    except FileNotFoundError:
        raise ValueError(f"Could not read {file_name}")


main()


