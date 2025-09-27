from duplicated_subtrees_types import DuplicatedSubTreeList

def duplicated_subtree_list(
    directory_path_group_list: DuplicatedSubTreeList, 
) -> DuplicatedSubTreeList:
    result: DuplicatedSubTreeList = []

    for directory_path_group in directory_path_group_list:
        if len(directory_path_group) > 1:
            result.append(directory_path_group)

    return result
