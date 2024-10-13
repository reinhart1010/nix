---
layout: page
title: common/dust (English)
description: "Dust gives an instant overview of which directories are using disk space."
content_hash: 03544e7a2bd1e5948a9973c8935fc7e4c505c933
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/dust.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dust.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dust

Dust gives an instant overview of which directories are using disk space.
More information: <https://github.com/bootandy/dust>.

- Display information for the current directory:

`dust`

- Display information about one or more directories:

`dust `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory1 path/to/directory2 ...</span>

- Display 30 directories (defaults to 21):

`dust --number-of-lines 30`

- Display information for the current directory, up to 3 levels deep:

`dust --depth 3`

- Display the biggest directories at the top in descending order:

`dust --reverse`

- Ignore all files and directories with a specific name:

`dust --ignore-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_or_directory_name</span>

- Do not display percent bars and percentages:

`dust --no-percent-bars`
