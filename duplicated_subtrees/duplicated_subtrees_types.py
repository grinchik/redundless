from typing import Dict, List, Tuple, FrozenSet, DefaultDict

Line = str
LineList = List[Line]

FileHash = str
FileSize = int
FilePath = str
FileName = str
FileTuple = Tuple[FileHash, FileSize, FilePath]
DirectoryPath = str
DirectoryMap = DefaultDict[DirectoryPath, List[FileTuple]]
FileEntity = Tuple[FileHash, FileSize, FileName]
FileEntityList = List[FileEntity]
FileEntry = Tuple[DirectoryPath, FileEntity]
FileEntryList = List[FileEntry]
FileEntityListGroupByDirectoryPath = Dict[DirectoryPath, FileEntityList]
DuplicatedSubTreeList = List[List[DirectoryPath]]
DirectoryPathFrozenSetByFileEntrySet = \
    Dict[
        FrozenSet[FileEntity],
        List[DirectoryPath],
    ]
