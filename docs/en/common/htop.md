---
layout: page
title: common/htop (English)
description: "Display dynamic real-time information about running processes. An enhanced version of `top`."
content_hash: 41b4700e6b35c316adff4887c4371ab6583e398f
last_modified_at: 2024-07-25
related_topics:
  - title: español version
    url: /es/common/htop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/htop.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/htop.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/htop.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/htop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/htop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/htop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# htop

Display dynamic real-time information about running processes. An enhanced version of `top`.
More information: <https://htop.dev/>.

- Start `htop`:

`htop`

- Start `htop` displaying processes owned by a specific user:

`htop --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>

- Display processes hierarchically in a tree view to show the parent-child relationships:

`htop --tree`

- Sort processes by a specified `sort_item` (use `htop --sort help` for available options):

`htop --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sort_item</span>

- Start `htop` with the specified delay between updates, in tenths of a second (i.e. 50 = 5 seconds):

`htop --delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>

- See interactive commands while running htop:

`?`

- Switch to a different tab:

`tab`

- Display help:

`htop --help`
