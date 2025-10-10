import sys
import os

from typing import List
from typing import FrozenSet

FilePath = str
Prefix = str
Postfix = str

EXCLUDED_SET: FrozenSet[FilePath] = frozenset([
])

PREFIX_LIST: List[Prefix] = [
]

POSTFIX_LIST: List[Postfix] = [
    '/.DS_Store',
    '/Thumbs.db',
    '/desktop.ini',
]

def should_filter_file_path(file_path: FilePath) -> bool:
    if os.path.dirname(file_path) in EXCLUDED_SET:
        return True

    if any(file_path.startswith(prefix) for prefix in PREFIX_LIST):
        return True

    if any(file_path.endswith(postfix) for postfix in POSTFIX_LIST):
        return True

    return False

if __name__ == '__main__':
    for line in sys.stdin:
        _, _, file_path = line.strip().split('\t')

        if should_filter_file_path(file_path):
            continue

        print(line, end='')
