import itertools
import os

from duplicated_subtrees_types import DirectoryPathGroupList

def subtree_root_list(
    subtree_list: DirectoryPathGroupList, 
) -> DirectoryPathGroupList:
    dir_set = set(itertools.chain.from_iterable(subtree_list))

    result: DirectoryPathGroupList = []

    for dup_dir_path_list in subtree_list:
        subresult = \
            list(
                filter(
                    lambda dir_path:
                        not os.path.dirname(dir_path) in dir_set,
                        dup_dir_path_list
                    ),
                )

        result.append(subresult)

    return list(filter(lambda x: len(x) > 1, result))
