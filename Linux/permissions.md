# Linux File Permissions

Linux controls access to files and directories using permissions.

## Permission Types

- **r (Read)** = 4
- **w (Write)** = 2
- **x (Execute)** = 1

Example:

```
-rwxr-xr--
```

This means:

- Owner: Read, Write, Execute
- Group: Read, Execute
- Others: Read

---

## View Permissions

```bash
ls -l
```

Example output:

```bash
-rwxr-xr-- 1 prince users 1024 Jul 15 file.txt
```

---

## Change Permissions

```bash
chmod 755 file.txt
```

Meaning:

- Owner = 7 (rwx)
- Group = 5 (r-x)
- Others = 5 (r-x)

---

## Common chmod Values

| Permission | Value |
|------------|------:|
| rwx | 7 |
| rw- | 6 |
| r-x | 5 |
| r-- | 4 |
| --- | 0 |

Examples:

```bash
chmod 777 file.txt
chmod 755 script.sh
chmod 644 notes.txt
chmod 600 private.key
```

---

## Change File Owner

```bash
sudo chown william file.txt
```

Change owner and group:

```bash
sudo chown william:developers file.txt
```

---

## Change Group

```bash
sudo chgrp developers file.txt
```

---

## Default Permissions (umask)

Check current umask:

```bash
umask
```

Set a new umask:

```bash
umask 022
```

---

## Recursive Permissions

```bash
chmod -R 755 myfolder
```

Apply permissions to all files and subfolders.

---

## Interview Questions

### What is the difference between chmod and chown?

- **chmod** changes permissions.
- **chown** changes the owner of a file.

### What does chmod 755 mean?

Owner has read, write, and execute permissions. Group and others have read and execute permissions.

### What command displays file permissions?

```bash
ls -l
```
