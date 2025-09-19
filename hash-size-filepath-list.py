import sys
import os
import hashlib
from typing import Optional, List

STDOUT_FD = sys.stdout.fileno()
CHUNK_SIZE_MiB = 4

def get_file_hash(file_path: str) -> Optional[str]:
    hasher = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(CHUNK_SIZE_MiB * 1024 * 1024)
                if not chunk:
                    break
                hasher.update(chunk)

        return hasher.hexdigest()

    except (IOError, OSError) as e:
        print(e, file=sys.stderr)
        return None

def get_file_size(file_path: str) -> Optional[int]:
    try:
        return os.path.getsize(file_path)

    except (IOError, OSError) as e:
        print(e, file=sys.stderr)
        return None

def main() -> None:
    file_path_list: List[str] = sys.argv[1:]

    for file_path in file_path_list:
        file_size = get_file_size(file_path)
        file_hash = get_file_hash(file_path)

        if file_size is not None and file_hash is not None:
            line = "\t".join([file_hash, str(file_size), file_path]) + "\n"
            os.write(STDOUT_FD, line.encode('utf-8'))

if __name__ == "__main__":
    main()
