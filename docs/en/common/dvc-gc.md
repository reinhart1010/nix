---
layout: page
title: common/dvc-gc (English)
description: "Remove unused files and directories from the cache or remote storage."
content_hash: df2c525d85f681454b223f7842fdb432ff740a6f
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dvc gc

Remove unused files and directories from the cache or remote storage.
More information: <https://dvc.org/doc/command-reference/gc>.

- Garbage collect from the cache, keeping only versions referenced by the current workspace:

`dvc gc --workspace`

- Garbage collect from the cache, keeping only versions referenced by branch, tags, and commits:

`dvc gc --all-branches --all-tags --all-commits`

- Garbage collect from the cache, including the default cloud remote storage (if set):

`dvc gc --all-commits --cloud`

- Garbage collect from the cache, including a specific cloud remote storage:

`dvc gc --all-commits --cloud --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>
