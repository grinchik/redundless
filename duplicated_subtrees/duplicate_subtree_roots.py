from collections import defaultdict

from duplicated_subtrees_types import DirectoryMap
from duplicated_subtrees_types import FileEntryList

from directory_path_to_file_entry_list_map import directory_path_to_file_entry_list_map
from high_level_directory_path_group_list import high_level_directory_path_group_list
from directory_path_list_by_file_entity_list_set import directory_path_list_by_file_entity_list_set

def duplicate_subtree_roots(file_entry_list: FileEntryList):
    directory_map: DirectoryMap = defaultdict(list)

    for file_entry in file_entry_list:
        directory_path_to_file_entry_list_map(directory_map, file_entry)

    return high_level_directory_path_group_list(
        directory_path_list_by_file_entity_list_set(
            directory_map,
        ),
    )
