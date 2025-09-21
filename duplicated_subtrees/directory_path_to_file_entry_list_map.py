import os
from duplicated_subtrees_types import DirectoryMap
from duplicated_subtrees_types import FileTuple

def directory_path_to_file_entry_list_map(
    directory_path_to_file_entry_list_map: DirectoryMap, 
    file_entry: FileTuple,
) -> None:
    file_path = file_entry[2]
    directory_path = os.path.dirname(file_path)

    while True:
        if directory_path not in directory_path_to_file_entry_list_map:
            directory_path_to_file_entry_list_map[directory_path] = []

        directory_path_to_file_entry_list_map[directory_path].append(file_entry)

        if directory_path == '/':
            break

        directory_path = os.path.dirname(directory_path)
