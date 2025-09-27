import os
from duplicated_subtrees_types import DirectoryMap
from duplicated_subtrees_types import DirectoryPath
from duplicated_subtrees_types import FileEntry

def directory_path_to_file_entry_list_map(
    directory_path_to_file_entry_list_map: DirectoryMap, 
    file_entry: FileEntry,
) -> None:
    file_hash = file_entry[0]
    file_size = file_entry[1]
    file_path = file_entry[2]
    directory_path: DirectoryPath = os.path.dirname(file_path)

    while True:
        file_name = file_path \
            .removeprefix(directory_path) \
            .removeprefix('/')

        directory_path_to_file_entry_list_map[directory_path].append(
            (file_hash, int(file_size), file_name),
        )

        if directory_path == '/':
            break

        directory_path = os.path.dirname(directory_path)
