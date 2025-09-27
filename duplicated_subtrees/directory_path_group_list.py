from collections import defaultdict

from duplicated_subtrees_types import DirectoryMap
from duplicated_subtrees_types import DirectoryPathFrozenSetByFileEntrySet

def directory_path_group_list(directory_map: DirectoryMap):
    result: DirectoryPathFrozenSetByFileEntrySet = defaultdict(list)

    for directory_path, file_entity_list in directory_map.items():
        result[frozenset(file_entity_list)].append(directory_path)

    return list(result.values())
