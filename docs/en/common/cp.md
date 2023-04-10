---
layout: page
title: common/cp (English)
description: "Copy files and directories."
content_hash: 5eef61ec77680e89668695350698b0a3bde1b138
last_modified_at: 2023-04-10
related_topics:
  - title: català version
    url: /ca/common/cp.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/cp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cp.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cp.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cp.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cp.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/cp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cp.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/cp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cp.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cp.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cp.html
    icon: bi bi-globe
---
# cp

Copy files and directories.
More information: <https://www.gnu.org/software/coreutils/cp>.

- Copy a file to another location:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_file.ext</span>

- Copy a file into another directory, keeping the filename:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_file.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_parent_directory</span>

- Recursively copy a directory's contents to another location (if the destination exists, the directory is copied inside it):

`cp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Copy a directory recursively, in verbose mode (shows files as they are copied):

`cp -vR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Copy multiple files at once to a directory:

`cp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Copy text files to another location, in interactive mode (prompts user before overwriting):

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Follow symbolic links before copying:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">link</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>

- Use the first argument as the destination directory (useful for `xargs ... | cp -t <DEST_DIR>`):

`cp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/target_directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>
