# redundless

## Requirements

* Linux with `bash`
* GNU coreutils (provides `sha256sum`, `nproc`)
* GNU findutils (provides `find`, `xargs`)

## Generating a hash list

1. Ensure the filesystem is mounted read-only (recommended for data integrity)
1. Generate hash file list:

```
./hash-filelist.sh /storage $(nproc) > storage.sha256sum.txt
```

Here `/storage` is the starting directory to traverse, and `$(nproc)` returns the number of CPU cores.
