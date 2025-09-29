from duplicated_subtrees_types import FileSignatureToDirectoryPathGroupList
from duplicated_subtrees_types import OutputStructure

def to_output(input: FileSignatureToDirectoryPathGroupList):
    result: OutputStructure = []

    for file_signature, directory_path_group in input:
        file_size_sum = sum(file_size for _, file_size in file_signature)
        result.append((file_size_sum, directory_path_group))

    return result
