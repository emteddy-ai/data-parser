import os
import json
import argparse

from data_parser.parsers import JsonParser, CsvParser

def main():
    parser = argparse.ArgumentParser(description='Data Parser')
    parser.add_argument('-f', '--file', required=True, help='Input file path')
    parser.add_argument('-o', '--output', required=True, help='Output file path')
    parser.add_argument('-t', '--type', choices=['json', 'csv'], required=True, help='File type')
    args = parser.parse_args()

    file_path = args.file
    output_path = args.output
    file_type = args.type

    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File {file_path} not found')

    if file_type == 'json':
        parser = JsonParser()
    elif file_type == 'csv':
        parser = CsvParser()

    with open(file_path, 'r') as file:
        data = parser.parse(file)

    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    main()