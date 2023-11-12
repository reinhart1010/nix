---
layout: page
title: common/dvc-fetch (English)
description: "Download DVC tracked files and directories from a remote repository."
content_hash: f8083c861134ec8304f8efa76afbc0fc3cd60f88
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# dvc fetch

Download DVC tracked files and directories from a remote repository.
More information: <https://dvc.org/doc/command-reference/fetch>.

- Fetch the latest changes from the default remote upstream repository (if set):

`dvc fetch`

- Fetch changes from a specific remote upstream repository:

`dvc fetch --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_name</span>

- Fetch the latest changes for a specific target/s:

`dvc fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target/s</span>

- Fetch changes for all branch and tags:

`dvc fetch --all-branches --all-tags`

- Fetch changes for all commits:

`dvc fetch --all-commits`
