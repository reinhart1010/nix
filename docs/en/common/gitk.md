---
layout: page
title: common/gitk (English)
description: "Browse Git repositories graphically."
content_hash: 95b9f141013d859cbac62306e02147ad1b19ae17
last_modified_at: 2024-04-26
related_topics:
  - title: Türkçe version
    url: /tr/common/gitk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gitk

Browse Git repositories graphically.
See also: `git-gui`, `git-cola`, `tig`.
More information: <https://git-scm.com/docs/gitk>.

- Show the repository browser for the current Git repository:

`gitk`

- Show repository browser for a specific file or directory:

`gitk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- Show commits made since 1 week ago:

`gitk --since="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1 week ago</span>`"`

- Show commits older than 1/1/2016:

`gitk --until="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1/1/2015</span>`"`

- Show at most 100 changes in all branches:

`gitk --max-count=100 --all`
