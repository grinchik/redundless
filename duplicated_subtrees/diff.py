import sys

from pathlib import Path

from typing import List, Tuple, Set

from filter import should_filter_file_path

Line = str
LineList = List[Line]

FileHash = str
FileSize = int
FilePath = str
FileName = str
FileEntry = Tuple[FileHash, FileSize, FilePath]
FileEntryList = List[FileEntry]

def read_lines(file_path: Path):
    with file_path.open('r', encoding='utf-8') as file:
        for line in file:
            yield line

if __name__ == '__main__':
    base: Set[FileHash] = set()
    file_entry_list_b: FileEntryList = []

    file_path_a = Path(sys.argv[1])
    file_path_b = Path(sys.argv[2])

    for line in read_lines(file_path_a):
        file_hash, _, file_path = line.strip().split('\t')
        if should_filter_file_path(file_path):
            continue
        file_entry = (file_hash, file_path)
        base.add(file_hash)

    for line in read_lines(file_path_b):
        file_hash, _, file_path = line.strip().split('\t')
        if should_filter_file_path(file_path):
            continue
        if file_hash not in base:
            print('\t'.join([file_path]))
