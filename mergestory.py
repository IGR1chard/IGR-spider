import os
import re
import cn2an

def normalize_file_names(input_directory):
    # Get a list of all text files in the directory
    text_files = [file for file in os.listdir(input_directory) if file.endswith('.txt')]
    # print(text_files)
    # Iterate through each text file
    for text_file in text_files:
        # Extract the chapter number and title from the original file name
        match = re.match(r'^第(\S+)章：(.+)$', text_file)
        # print(match)
        if match:
            chinese_number = match.group(1)
            print(chinese_number)
            title = match.group(2)

            # Convert the Chinese number to Arabic numeral
            arabic_number = cn2an.cn2an(chinese_number)
            print(arabic_number)
            # Create the new file name without adding "txt" at the end
            new_file_name = f"第{arabic_number}章 {title}"
            # print(new_file_name)
            # Rename the file
            old_file_path = os.path.join(input_directory, text_file)
            new_file_path = os.path.join(input_directory, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {text_file} -> {new_file_name}")

# Example usage
def extract_arabic_number(file_name):
    # Extract the Arabic number from the filename
    match = re.match(r'^第(\d+)章', file_name)
    if match:
        return int(match.group(1))
    return None

def merge_files(input_directory, output_file_path):
    # Get a list of all text files in the directory
    text_files = [file for file in os.listdir(input_directory) if file.endswith('.txt')]

    # Sort the files based on the extracted Arabic numbers
    sorted_files = sorted(text_files, key=lambda x: extract_arabic_number(x))

    # Open the output file for writing
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Iterate through each sorted text file
        for text_file in sorted_files:
            file_path = os.path.join(input_directory, text_file)

            # Read the content of the current text file
            with open(file_path, 'r', encoding='utf-8') as current_file:
                file_content = current_file.read()

            # Write the content to the output file
            output_file.write(f"=== {text_file} ===\n")
            output_file.write(file_content + '\n')

    print(f"Merged content saved to: {output_file_path}")

# Example usage






# Example usage
# Directory where your text files are located
# input_directory = 'D:/Download/2077/《》正文/'
input_directory = 'D:/Download/2077/修仙合并/2/'
output_file_path = 'D:/Download/2077/修仙合并/修仙界第一大祸害.txt'
merge_files(input_directory, output_file_path)
# normalize_file_names(input_directory)
# Output file to store the merged content




