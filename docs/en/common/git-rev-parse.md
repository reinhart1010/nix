---
layout: page
title: common/git-rev-parse (English)
description: "Display metadata related to revisions."
content_hash: 142691ab1ecdfb4058455f465e3de3448b4592d5
last_modified_at: 2024-02-15
related_topics:
  - title: español version
    url: /es/common/git-rev-parse.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-rev-parse.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-rev-parse.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-rev-parse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git rev-parse

Display metadata related to revisions.
More information: <https://git-scm.com/docs/git-rev-parse>.

- Get the commit hash of a branch:

`git rev-parse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name</span>

- Get the current branch name:

`git rev-parse --abbrev-ref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Get the absolute path to the root directory:

`git rev-parse --show-toplevel`
