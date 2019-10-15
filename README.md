# kottans-backend

# Git intro.
I first learned about Git.
Everything is new for me. 

## Unix shell
[quiz1](task-unix-shell/quiz1.png)
[quiz2](task-unix-shell/quiz2.png)
[quiz3](task-unix-shell/quiz3.png)
[quiz4](task-unix-shell/quiz4.png?raw=true "Optional Title")

I got a ton of info about Linux terminal command, bash scripts.

## Git Collaboration

[Screenshot](task-git-collaboration/task-done.png)

Github issues was new for me, contributing rules is a good idea. 

## Memory Management

Answers:
1. Segmentation fault.
2. Heap is enlarged to make room for the requested block.
3. Data segment contents static variables initialized in source code, text segment is read-only and contents program code.
```
5617a111d000-5617a1221000 r-xp 00000000 08:01 15206325                   /bin/bash
5617a1420000-5617a1424000 r--p 00103000 08:01 15206325                   /bin/bash
5617a1424000-5617a142d000 rw-p 00107000 08:01 15206325                   /bin/bash
5617a142d000-5617a1437000 rw-p 00000000 00:00 0 
5617a1dc1000-5617a1f2d000 rw-p 00000000 00:00 0                          [heap]
7f0dcc9d8000-7f0dcc9e3000 r-xp 00000000 08:01 9442157                    /lib/x86_64-linux-gnu/libnss_files-2.27.so
7f0dcc9e3000-7f0dccbe2000 ---p 0000b000 08:01 9442157                    /lib/x86_64-linux-gnu/libnss_files-2.27.so
7f0dccbe2000-7f0dccbe3000 r--p 0000a000 08:01 9442157                    /lib/x86_64-linux-gnu/libnss_files-2.27.so
7f0dccbe3000-7f0dccbe4000 rw-p 0000b000 08:01 9442157                    /lib/x86_64-linux-gnu/libnss_files-2.27.so
7f0dccbe4000-7f0dccbea000 rw-p 00000000 00:00 0 
7f0dccbea000-7f0dccc01000 r-xp 00000000 08:01 9442151                    /lib/x86_64-linux-gnu/libnsl-2.27.so
7f0dccc01000-7f0dcce00000 ---p 00017000 08:01 9442151                    /lib/x86_64-linux-gnu/libnsl-2.27.so
7f0dcce00000-7f0dcce01000 r--p 00016000 08:01 9442151                    /lib/x86_64-linux-gnu/libnsl-2.27.so
7f0dcce01000-7f0dcce02000 rw-p 00017000 08:01 9442151                    /lib/x86_64-linux-gnu/libnsl-2.27.so
7f0dcce02000-7f0dcce04000 rw-p 00000000 00:00 0 
7f0dcce04000-7f0dcce0f000 r-xp 00000000 08:01 9442168                    /lib/x86_64-linux-gnu/libnss_nis-2.27.so
7f0dcce0f000-7f0dcd00e000 ---p 0000b000 08:01 9442168                    /lib/x86_64-linux-gnu/libnss_nis-2.27.so
7f0dcd00e000-7f0dcd00f000 r--p 0000a000 08:01 9442168                    /lib/x86_64-linux-gnu/libnss_nis-2.27.so
7f0dcd00f000-7f0dcd010000 rw-p 0000b000 08:01 9442168                    /lib/x86_64-linux-gnu/libnss_nis-2.27.so
7f0dcd010000-7f0dcd018000 r-xp 00000000 08:01 9442153                    /lib/x86_64-linux-gnu/libnss_compat-2.27.so
7f0dcd018000-7f0dcd218000 ---p 00008000 08:01 9442153                    /lib/x86_64-linux-gnu/libnss_compat-2.27.so
7f0dcd218000-7f0dcd219000 r--p 00008000 08:01 9442153                    /lib/x86_64-linux-gnu/libnss_compat-2.27.so
7f0dcd219000-7f0dcd21a000 rw-p 00009000 08:01 9442153                    /lib/x86_64-linux-gnu/libnss_compat-2.27.so
7f0dcd21a000-7f0dcd671000 r--p 00000000 08:01 13900535                   /usr/lib/locale/locale-archive
7f0dcd671000-7f0dcd858000 r-xp 00000000 08:01 9442067                    /lib/x86_64-linux-gnu/libc-2.27.so
7f0dcd858000-7f0dcda58000 ---p 001e7000 08:01 9442067                    /lib/x86_64-linux-gnu/libc-2.27.so
7f0dcda58000-7f0dcda5c000 r--p 001e7000 08:01 9442067                    /lib/x86_64-linux-gnu/libc-2.27.so
7f0dcda5c000-7f0dcda5e000 rw-p 001eb000 08:01 9442067                    /lib/x86_64-linux-gnu/libc-2.27.so
7f0dcda5e000-7f0dcda62000 rw-p 00000000 00:00 0 
7f0dcda62000-7f0dcda65000 r-xp 00000000 08:01 9442090                    /lib/x86_64-linux-gnu/libdl-2.27.so
7f0dcda65000-7f0dcdc64000 ---p 00003000 08:01 9442090                    /lib/x86_64-linux-gnu/libdl-2.27.so
7f0dcdc64000-7f0dcdc65000 r--p 00002000 08:01 9442090                    /lib/x86_64-linux-gnu/libdl-2.27.so
7f0dcdc65000-7f0dcdc66000 rw-p 00003000 08:01 9442090                    /lib/x86_64-linux-gnu/libdl-2.27.so
7f0dcdc66000-7f0dcdc8b000 r-xp 00000000 08:01 9442225                    /lib/x86_64-linux-gnu/libtinfo.so.5.9
7f0dcdc8b000-7f0dcde8b000 ---p 00025000 08:01 9442225                    /lib/x86_64-linux-gnu/libtinfo.so.5.9
7f0dcde8b000-7f0dcde8f000 r--p 00025000 08:01 9442225                    /lib/x86_64-linux-gnu/libtinfo.so.5.9
7f0dcde8f000-7f0dcde90000 rw-p 00029000 08:01 9442225                    /lib/x86_64-linux-gnu/libtinfo.so.5.9
7f0dcde90000-7f0dcdeb7000 r-xp 00000000 08:01 9442039                    /lib/x86_64-linux-gnu/ld-2.27.so
7f0dce099000-7f0dce09e000 rw-p 00000000 00:00 0 
7f0dce0b0000-7f0dce0b7000 r--s 00000000 08:01 14288493                   /usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache
7f0dce0b7000-7f0dce0b8000 r--p 00027000 08:01 9442039                    /lib/x86_64-linux-gnu/ld-2.27.so
7f0dce0b8000-7f0dce0b9000 rw-p 00028000 08:01 9442039                    /lib/x86_64-linux-gnu/ld-2.27.so
7f0dce0b9000-7f0dce0ba000 rw-p 00000000 00:00 0 
7ffdddb1e000-7ffdddb3f000 rw-p 00000000 00:00 0                          [stack]
7ffdddb89000-7ffdddb8c000 r--p 00000000 00:00 0                          [vvar]
7ffdddb8c000-7ffdddb8e000 r-xp 00000000 00:00 0                          [vdso]
ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]
```
Examples:
`Heap - 5617a1dc1000-5617a1f2d000`, `Stack - 7ffdddb1e000-7ffdddb3f000`, `MMS - 7f0dcc9d8000-7f0dcc9e3000`

All content is new for me, I'm not sure I understood all of this right.