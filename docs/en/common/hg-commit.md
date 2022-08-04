---
layout: page
title: common/hg-commit (English)
description: "Commit all staged or specified files to the repository."
content_hash: 0e0e8221ae045b4c159826dc8617963d7dd60509
---
# hg commit

Commit all staged or specified files to the repository.
More information: <https://www.mercurial-scm.org/doc/hg.1.html#commit>.

- Commit staged files to the repository:

`hg commit`

- Commit a specific file or directory:

`hg commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Commit with a specific message:

`hg commit --message `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">message</span>

- Commit all files matching a specified pattern:

`hg commit --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Commit all files, excluding those that match a specified pattern:

`hg commit --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>

- Commit using the interactive mode:

`hg commit --interactive`
