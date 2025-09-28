from collections import defaultdict

from duplicated_subtrees_types import DirectoryMap
from duplicated_subtrees_types import DirectoryPathListByFileEntrySet

def directory_path_list_by_file_entity_list_set(directory_map: DirectoryMap):
    result: DirectoryPathListByFileEntrySet = defaultdict(list)

    for directory_path, file_entity_list in directory_map.items():
        result[frozenset(file_entity_list)].append(directory_path)

    return result
