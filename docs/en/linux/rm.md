---
layout: page
title: linux/rm (English)
description: "Remove files or directories."
content_hash: 9c5ec0925430f765d7c7a21e329a3bacc8d1b446
last_modified_at: 2024-09-04
related_topics:
  - title: 한국어 version
    url: /ko/linux/rm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/rm.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rm

Remove files or directories.
See also: `rmdir`.
More information: <https://www.gnu.org/software/coreutils/rm>.

- Remove specific files:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Remove specific files ignoring nonexistent ones:

`rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Remove specific files interactively prompting before each removal:

`rm --interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Remove specific files printing info about each removal:

`rm --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>

- Remove specific files and directories recursively:

`rm --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory1 path/to/file_or_directory2 ...</span>

- Remove empty directories (this is considered the safe method):

`rm --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
