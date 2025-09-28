from typing import Dict, List, Tuple, Set, FrozenSet, DefaultDict

Line = str
LineList = List[Line]

FileHash = str
FileSize = int
FilePath = str
FileName = str
FileEntry = Tuple[FileHash, FileSize, FilePath]
DirectoryPath = str
DirectoryMap = DefaultDict[DirectoryPath, List[FileEntry]]
DirectoryPathGroup = List[DirectoryPath]
DirectoryPathGroupList = List[DirectoryPathGroup]
DirectoryPathListByFileEntrySet = \
    Dict[
        FrozenSet[FileEntry],
        List[DirectoryPath],
    ]
FileHashSet = Set[FileHash]
