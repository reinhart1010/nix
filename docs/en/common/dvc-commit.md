---
layout: page
title: common/dvc-commit (English)
description: "Record changes to DVC-tracked files in the project."
content_hash: 12b3cac07f7e997f3441f7c36542fe275d7ee791
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dvc commit

Record changes to DVC-tracked files in the project.
More information: <https://dvc.org/doc/command-reference/commit>.

- Commit changes to all DVC-tracked files and directories:

`dvc commit`

- Commit changes to a specified DVC-tracked target:

`dvc commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Recursively commit all DVC-tracked files in a directory:

`dvc commit --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
