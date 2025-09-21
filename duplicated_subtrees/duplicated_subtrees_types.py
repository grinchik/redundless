from typing import Dict, List, Tuple

FileHash = str
FileSize = int
FilePath = str
FileEntry = Tuple[FileHash, FileSize, FilePath]
DirectoryPath = str
DirectoryMap = Dict[DirectoryPath, List[FileEntry]]
