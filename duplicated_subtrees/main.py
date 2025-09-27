import sys
import json

from collections import defaultdict

from subtree_root_list import subtree_root_list
from duplicated_subtree_list import duplicated_subtree_list
from directory_path_group_list import directory_path_group_list
from directory_path_to_file_entry_list_map import directory_path_to_file_entry_list_map

from duplicated_subtrees_types import DirectoryMap
from duplicated_subtrees_types import FileTuple

if __name__ == '__main__':
    directory_map: DirectoryMap = defaultdict(list)

    for line in sys.stdin:
        file_hash, file_size, file_path = line.strip().split('\t')
        file_entry: FileTuple = (file_hash, int(file_size), file_path)
        directory_path_to_file_entry_list_map(directory_map, file_entry)

    result = subtree_root_list(
        duplicated_subtree_list(
            directory_path_group_list(
                directory_map,
            ),
        ),
    )

    print(json.dumps(subtree_root_list(result), indent=4))
