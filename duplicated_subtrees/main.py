import sys
import json

from duplicate_subtree_roots import duplicate_subtree_roots
from to_output import to_output

from duplicated_subtrees_types import FileEntryList

if __name__ == '__main__':
    file_entry_list: FileEntryList = []

    for line in sys.stdin:
        file_hash, file_size, file_path = line.strip().split('\t')
        file_entry = (file_hash, int(file_size), file_path)
        file_entry_list.append(file_entry)

    result = duplicate_subtree_roots(file_entry_list)

    print(
        json.dumps(
            sorted(to_output(result), key=lambda x: x[0], reverse=True),
            ensure_ascii=False,
            indent=4,
            default=list,
        )
    )
