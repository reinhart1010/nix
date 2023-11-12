---
layout: page
title: common/hg-log (English)
description: "Display the revision history of the repository."
content_hash: d46cf4b9f19686c0aceddf6eb15cc392ce6e1463
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# hg log

Display the revision history of the repository.
More information: <https://www.mercurial-scm.org/doc/hg.1.html#log>.

- Display the entire revision history of the repository:

`hg log`

- Display the revision history with an ASCII graph:

`hg log --graph`

- Display the revision history with file names matching a specified pattern:

`hg log --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Display the revision history, excluding file names that match a specified pattern:

`hg log --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Display the log information for a specific revision:

`hg log --rev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>

- Display the revision history for a specific branch:

`hg log --branch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch</span>

- Display the revision history for a specific date:

`hg log --date `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">date</span>

- Display revisions committed by a specific user:

`hg log --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>
