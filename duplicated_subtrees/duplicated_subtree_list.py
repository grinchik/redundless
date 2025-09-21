from collections import defaultdict

from duplicated_subtrees_types import FileEntryList
from duplicated_subtrees_types import DuplicatedSubTreeList
from duplicated_subtrees_types import FileEntityListGroupByDirectoryPath

def duplicated_subtree_list(
    file_entry_list: FileEntryList, 
) -> DuplicatedSubTreeList:
    # FIXME: Naïve proof-of-concept implementation, must review and optimize

    result: DuplicatedSubTreeList = []

    group: FileEntityListGroupByDirectoryPath = defaultdict(list)

    for directory_path, file_entry in file_entry_list:
        group[directory_path].append(file_entry)

    for directory_path_outer, file_entry_list_outer in group.items():
        subresult = [directory_path_outer]

        file_entry_list_outer = set(file_entry_list_outer)

        for directory_path_inner, file_entry_list_inner in group.items():
            file_entry_list_inner = set(file_entry_list_inner)

            if directory_path_outer == directory_path_inner:
                continue

            if file_entry_list_outer == file_entry_list_inner:
                subresult.append(directory_path_inner)

        if len(subresult) > 1:
            result.append(subresult)

    return result
