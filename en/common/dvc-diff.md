---
layout: page
title: common/dvc-diff (English)
description: "Show changes in DVC tracked file and directories."
content_hash: a6bf1613b1af2e1e972164e90784e8c70ac4c869
---
# dvc diff

Show changes in DVC tracked file and directories.
More information: <https://dvc.org/doc/command-reference/diff>.

- Compare DVC tracked files from different Git commits, tags, and branches w.r.t the current workspace:

`dvc diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit_hash/tag/branch</span>

- Compare the changes in DVC tracked files from 1 Git commit to another:

`dvc diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision_b</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision_a</span>

- Compare DVC tracked files, along with their latest hash:

`dvc diff --show-hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Compare DVC tracked files, displaying the output as JSON:

`dvc diff --show-json --show-hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Compare DVC tracked files, displaying the output as Markdown:

`dvc diff --show-md --show-hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
