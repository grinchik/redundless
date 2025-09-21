import os

from duplicated_subtrees_types import FileEntryList
from duplicated_subtrees_types import DirectoryPath

def file_entry_list(
    line: str,
) -> FileEntryList:
    result: FileEntryList = []

    file_hash, file_size, file_path = line.split('\t')

    directory_path: DirectoryPath = os.path.dirname(file_path)

    while True:
        file_name = file_path \
            .removeprefix(directory_path) \
            .removeprefix('/')

        file_entry = (directory_path, (file_hash, int(file_size), file_name))
        result.append(file_entry)

        if directory_path == '/':
            break

        directory_path = os.path.dirname(directory_path)

    return result
