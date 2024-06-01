'''Counts the number of unique words in the file check_file.txt'''
import re
import os
from bar_graph import create_bar_graph
# Add the parent directory to sys.path
current_dir = os.path.dirname(__file__)
blacklist_file_path = os.path.join(current_dir, '..', 'uniquewordcount', 'blacklist.txt')
default_check_file_path = os.path.join(current_dir, '..', 'uniquewordcount', 'check_file.txt')

MAX_X_AXIS = 10

def unique_word_counter(file, is_output, is_create_bar_graph):
    '''Counts the number of unique words in the file check_file.txt'''
    word_dict = {}
    charlist=["“",",","!","”","?","."]

    try:
        isinstance(is_create_bar_graph, bool) and isinstance(is_output, bool)
    except TypeError:
        print("Argument is_output or is_create_bar_graph not bool. May cause stability issues")

    try:
        with open(file, "r", encoding='utf-8') as f:
            lines = f.read()
            lines = lines.lower()
            for ch in charlist:
                lines = lines.replace(ch,"")
            # Blacklist words
            try:
                with open(blacklist_file_path, "r", encoding='utf-8') as b:
                    for word in b:
                        # Set words to lower case and remove leading white space/spaces
                        word = word.lower()
                        word = word.strip()
                        # Use Reg expressions to catch whole words
                        pattern = r'\b' + re.escape(word) + r'\b'
                        lines = re.sub(pattern, '', lines)
                        # Remove any extra spaces left behind after removal
                        lines = re.sub(r'\s+', ' ', lines).strip()
            except IOError as e:
                print(f"I/O error({0}): {1}".format(e.errno, e.strerror), ": ", blacklist_file_path)
            lines = lines.split()
            # Count the words in the dict
            for element in lines:
                if element in word_dict:
                    pass
                else:
                    count = lines.count(element)
                    word_dict.update({element:count})
    except IOError as e:
        print (f"I/O error({0}): {1}".format(e.errno, e.strerror), ": ", file)
    sorted_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))

    # Output to file
    if is_output is True:
        output_results_to_file(sorted_dict)

    if is_create_bar_graph is True:
        create_bar_graph(sorted_dict, MAX_X_AXIS)

    return sorted_dict

def output_results_to_file(output_dict):
    '''Takes a dict and outputs results to file'''
    with open("output.txt","w", encoding='utf-8') as o:
        for key, value in output_dict.items():
            o.write(f"{key}: {value}\n")
    return output_dict

unique_word_counter(default_check_file_path, True, True)
