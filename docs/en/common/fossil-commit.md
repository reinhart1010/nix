---
layout: page
title: common/fossil-commit (English)
description: "Commit files to a Fossil repository."
content_hash: 0b4fd240727df17df2532f37a23f3d32473ab2fc
last_modified_at: 2024-01-31
related_topics:
  - title: Nederlands version
    url: /nl/common/fossil-commit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fossil commit

Commit files to a Fossil repository.
More information: <https://fossil-scm.org/home/help/commit>.

- Create a new version containing all the changes in the current checkout; user will be prompted for a comment:

`fossil commit`

- Create a new version containing all the changes in the current checkout, using the specified comment:

`fossil commit --comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comment</span>`"`

- Create a new version containing all the changes in the current checkout with a comment read from a specific file:

`fossil commit --message-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/commit_message_file</span>

- Create a new version containing changes from the specified files; user will be prompted for a comment:

`fossil commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1 path/to/file2 ...</span>
