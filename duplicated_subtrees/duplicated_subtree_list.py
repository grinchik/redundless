from collections import defaultdict

from duplicated_subtrees_types import FileEntryList
from duplicated_subtrees_types import DuplicatedSubTreeList
from duplicated_subtrees_types import FileEntityListGroupByDirectoryPath
from duplicated_subtrees_types import DirectoryPathFrozenSetByFileEntrySet

def file_entity_list_grouped_by_directory_path(file_entry_list: FileEntryList):
    result: FileEntityListGroupByDirectoryPath = defaultdict(list)

    for directory_path, file_entity in file_entry_list:
        result[directory_path].append(file_entity)

    return result

def lift_of_directory_path_lists(group: FileEntityListGroupByDirectoryPath):
    result: DirectoryPathFrozenSetByFileEntrySet = defaultdict(list)

    for directory_path, file_entity_list in group.items():
        result[frozenset(file_entity_list)].append(directory_path)

    return result.values()

def duplicated_subtree_list(
    file_entry_list: FileEntryList, 
) -> DuplicatedSubTreeList:
    result: DuplicatedSubTreeList = []

    directory_path_list_list = lift_of_directory_path_lists(
        file_entity_list_grouped_by_directory_path(
            file_entry_list,
        ),
    )

    for directory_path_list in directory_path_list_list:
        if len(directory_path_list) > 1:
            result.append(directory_path_list)

    return result
