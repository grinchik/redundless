from typing import Dict, List, Tuple, FrozenSet, DefaultDict

Line = str
LineList = List[Line]

FileHash = str
FileSize = int
FilePath = str
FileName = str
FileEntry = Tuple[FileHash, FileSize, FilePath]
DirectoryPath = str
DirectoryMap = DefaultDict[DirectoryPath, List[FileEntry]]
DirectoryPathGroupList = List[List[DirectoryPath]]
DirectoryPathGroupByFileEntrySet = \
    Dict[
        FrozenSet[FileEntry],
        List[DirectoryPath],
    ]
