from typing import Dict, List, Tuple

FileHash = str
FileSize = int
FilePath = str
FileName = str
FileTuple = Tuple[FileHash, FileSize, FilePath]
DirectoryPath = str
DirectoryMap = Dict[DirectoryPath, List[FileTuple]]
FileEntry = Tuple[DirectoryPath, Tuple[FileHash, FileSize, FileName]]
FileEntryList = List[FileEntry]
