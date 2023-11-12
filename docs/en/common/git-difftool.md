---
layout: page
title: common/git-difftool (English)
description: "Show file changes using external diff tools. Accepts the same options and arguments as `git diff`."
content_hash: 93d186eac651a11b39b80bee429785aab4c1814b
last_modified_at: 2023-11-12
related_topics:
  - title: français version
    url: /fr/common/git-difftool.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-difftool.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-difftool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# git difftool

Show file changes using external diff tools. Accepts the same options and arguments as `git diff`.
See also: `git diff`.
More information: <https://git-scm.com/docs/git-difftool>.

- List available diff tools:

`git difftool --tool-help`

- Set the default diff tool to meld:

`git config --global diff.tool "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">meld</span>`"`

- Use the default diff tool to show staged changes:

`git difftool --staged`

- Use a specific tool (opendiff) to show changes since a given commit:

`git difftool --tool=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">opendiff</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>
