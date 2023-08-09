---
layout: page
title: common/cpio (English)
description: "Copies files in and out of archives."
content_hash: 1556229537ad1073451128b1e826c674536a26fc
last_modified_at: 2023-08-09
related_topics:
  - title: italiano version
    url: /it/common/cpio.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cpio.html
    icon: bi bi-globe
---
# cpio

Copies files in and out of archives.
Supports the following archive formats: cpio's custom binary, old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar, and POSIX.1 tar.
More information: <https://www.gnu.org/software/cpio>.

- Take a list of file names from `stdin` and add them [o]nto an archive in cpio's binary format:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3</span>`" | cpio -o > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.cpio</span>

- Copy all files and directories in a directory and add them [o]nto an archive, in [v]erbose mode:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` | cpio -ov > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.cpio</span>

- P[i]ck all files from an archive, generating [d]irectories where needed, in [v]erbose mode:

`cpio -idv < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.cpio</span>
