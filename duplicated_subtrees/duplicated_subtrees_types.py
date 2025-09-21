from typing import Dict, List, Tuple

Line = str
LineList = List[Line]

FileHash = str
FileSize = int
FilePath = str
FileName = str
FileTuple = Tuple[FileHash, FileSize, FilePath]
DirectoryPath = str
DirectoryMap = Dict[DirectoryPath, List[FileTuple]]
FileEntity = Tuple[FileHash, FileSize, FileName]
FileEntityList = List[FileEntity]
FileEntry = Tuple[DirectoryPath, Tuple[FileHash, FileSize, FileName]]
FileEntryList = List[FileEntry]
FileEntityListGroupByDirectoryPath = Dict[DirectoryPath, FileEntityList]
DuplicatedSubTreeList = List[List[DirectoryPath]]
