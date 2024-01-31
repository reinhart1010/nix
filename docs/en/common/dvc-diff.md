---
layout: page
title: common/dvc-diff (English)
description: "Show changes in DVC tracked file and directories."
content_hash: 489f862296b8c294d861c3478a12af1443ea23e0
last_modified_at: 2024-01-31
tldri18n_status: 2
---
# dvc diff

Show changes in DVC tracked file and directories.
More information: <https://dvc.org/doc/command-reference/diff>.

- Compare DVC tracked files from different Git commits, tags, and branches w.r.t the current workspace:

`dvc diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash/tag/branch</span>

- Compare the changes in DVC tracked files from 1 Git commit to another:

`dvc diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision2</span>

- Compare DVC tracked files, along with their latest hash:

`dvc diff --show-hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Compare DVC tracked files, displaying the output as JSON:

`dvc diff --show-json --show-hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Compare DVC tracked files, displaying the output as Markdown:

`dvc diff --show-md --show-hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
