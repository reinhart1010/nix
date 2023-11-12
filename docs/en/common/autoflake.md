---
layout: page
title: common/autoflake (English)
description: "A tool to remove unused imports and variables from Python code."
content_hash: 322ad02151b3cd483c18fc6176d2f919cabdccd8
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/common/autoflake.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autoflake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autoflake.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/autoflake.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autoflake.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autoflake

A tool to remove unused imports and variables from Python code.
More information: <https://github.com/myint/autoflake>.

- Remove unused variables from a single file and display the diff:

`autoflake --remove-unused-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Remove unused imports from multiple files and display the diffs:

`autoflake --remove-all-unused-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.py path/to/file2.py ...</span>

- Remove unused variables from a file, overwriting the file:

`autoflake --remove-unused-variables --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.py</span>

- Remove unused variables recursively from all files in a directory, overwriting each file:

`autoflake --remove-unused-variables --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
