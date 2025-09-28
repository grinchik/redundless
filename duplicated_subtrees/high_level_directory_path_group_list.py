from duplicated_subtrees_types import DirectoryPathListByFileEntrySet
from duplicated_subtrees_types import FileHashSet
from duplicated_subtrees_types import DirectoryPathGroupList

def high_level_directory_path_group_list(
    directory_path_list_by_file_entry_set_dict: DirectoryPathListByFileEntrySet, 
):
    # Converting dict to list
    step_1 = \
        list(directory_path_list_by_file_entry_set_dict.items())

    # Sorting by file entry set size
    step_2 = sorted(
        step_1,
        key=lambda x: len(x[0]),
        reverse=True,
    )

    # Rejecting groups without duplicates
    step_3 = [
        x
        for x in step_2
        if len(x[1]) > 1
    ]

    # Mapping file entity to file hash only
    step_4 = [
        (
            frozenset([item[0] for item in group[0]]),
            group[1],
        )
        for group in step_3
    ]

    # Rejecting directory path group if file hash set has already been included
    included_file_hash_set: FileHashSet = set()
    result: DirectoryPathGroupList = []

    for file_hash_set, directory_path_group in step_4:
        if file_hash_set.issubset(included_file_hash_set): continue

        included_file_hash_set.update(file_hash_set)
        result.append(directory_path_group)

    return result
