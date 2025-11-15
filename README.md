# redundless

## Requirements

* Linux with `bash`
* GNU coreutils (provides `sha256sum`, `nproc`)
* GNU findutils (provides `find`, `xargs`)

## Generating a hash-size-filepath list

1. Ensure the filesystem is mounted read-only (recommended for data integrity)
1. Generate hash-size-filepath list:

```
bash ./hash-size-filepath-list.sh /storage $(nproc) > storage.hash-size-filepath-list.txt
```

Here `/storage` is the starting directory to traverse, and `$(nproc)` returns the number of CPU cores.


## Getting the highest-level duplicate directory groups

```
cat storage.hash-size-filepath-list.txt | python3 duplicated_subtrees/filter.py | python3 duplicated_subtrees/main.py
```


## Finding unique files between two lists

Compare two hash-size-filepath lists and find files that exist in the second list but not in the first:
```
python3 duplicated_subtrees/diff.py list_a.txt list_b.txt
```

This will output the file paths from `list_b.txt` that have hashes not present in `list_a.txt`.
