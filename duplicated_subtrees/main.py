import sys
import json

from collections import defaultdict

from high_level_directory_path_group_list import high_level_directory_path_group_list
from directory_path_list_by_file_entity_list_set import directory_path_list_by_file_entity_list_set
from directory_path_to_file_entry_list_map import directory_path_to_file_entry_list_map
from to_output import to_output

from duplicated_subtrees_types import DirectoryMap
from duplicated_subtrees_types import FileEntry

if __name__ == '__main__':
    directory_map: DirectoryMap = defaultdict(list)

    for line in sys.stdin:
        file_hash, file_size, file_path = line.strip().split('\t')
        file_entry: FileEntry = (file_hash, int(file_size), file_path)
        directory_path_to_file_entry_list_map(directory_map, file_entry)

    result = high_level_directory_path_group_list(
        directory_path_list_by_file_entity_list_set(
            directory_map,
        ),
    )

    print(json.dumps(to_output(result), indent=4, default=list))
