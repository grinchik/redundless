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
