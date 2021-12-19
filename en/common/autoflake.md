---
layout: page
title: common/autoflake (English)
description: "A tool to remove unused imports and variables from Python code."
content_hash: 7690bd23f2f02832afaa60c6f1d49bf4d445e205
related_topics:
  - title: italiano version
    url: /it/common/autoflake.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/autoflake.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autoflake.html
    icon: bi bi-globe
---
# autoflake

A tool to remove unused imports and variables from Python code.
More information: <https://github.com/myint/autoflake>.

- Remove unused variables from a single file and display the diff:

`autoflake --remove-unused-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py</span>

- Remove unused imports from multiple files and display the diffs:

`autoflake --remove-all-unused-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2.py</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3.py</span>

- Remove unused variables from a file, overwriting the file:

`autoflake --remove-unused-variables --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.py</span>

- Remove unused variables recursively from all files in a directory, overwriting each file:

`autoflake --remove-unused-variables --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
