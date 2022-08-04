---
layout: page
title: common/git-ls-remote (English)
description: "Git command for listing references in a remote repository based on name or URL."
content_hash: 86249058454ea5daf1513c26608abb26e7fb7d0b
related_topics:
  - title: français version
    url: /fr/common/git-ls-remote.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-ls-remote.html
    icon: bi bi-globe
---
# git ls-remote

Git command for listing references in a remote repository based on name or URL.
If no name or URL are given, then the configured upstream branch will be used, or remote origin if the former is not configured.
More information: <https://git-scm.com/docs/git-ls-remote>.

- Show all references in the default remote repository:

`git ls-remote`

- Show only heads references in the default remote repository:

`git ls-remote --heads`

- Show only tags references in the default remote repository:

`git ls-remote --tags`

- Show all references from a remote repository based on name or URL:

`git ls-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_url</span>

- Show references from a remote repository filtered by a pattern:

`git ls-remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">repository_name</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>`"`
