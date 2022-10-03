---
layout: page
title: common/fossil-commit (English)
description: "Commit files to a Fossil repository."
content_hash: 5a98a89daeba13e47ac2ba3221d0d4b3c4f96277
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># fossil commit

Commit files to a Fossil repository.
More information: <https://fossil-scm.org/home/help/commit>.

- Create a new version containing all the changes in the current checkout; user will be prompted for a comment:

`fossil commit`

- Create a new version containing all the changes in the current checkout, using the specified comment:

`fossil commit --comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comment</span>`"`

- Create a new version containing all the changes in the current checkout with a comment read from a specific file:

`fossil commit --message-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/commit_message_file</span>

- Create a new version containing changes from the specified files; user will be prompted for a comment:

`fossil commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>
