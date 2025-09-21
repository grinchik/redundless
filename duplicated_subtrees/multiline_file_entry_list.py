from duplicated_subtrees_types import FileEntryList
from duplicated_subtrees_types import LineList
from file_entry_list import file_entry_list

def multiline_file_entry_list(
    line_list: LineList,
) -> FileEntryList:
    result: FileEntryList = []

    for line in line_list:
        for file_entry in file_entry_list(line):
            result.append(file_entry)

    return result
