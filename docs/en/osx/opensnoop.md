---
layout: page
title: osx/opensnoop (English)
description: "Tool that tracks file opens on your system."
content_hash: 2cc47a8032275e07b0eb14a084910e21e988666c
last_modified_at: 2024-01-31
related_topics:
  - title: español version
    url: /es/osx/opensnoop.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/opensnoop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# opensnoop

Tool that tracks file opens on your system.
More information: <https://keith.github.io/xcode-man-pages/opensnoop.1m.html>.

- Print all file opens as they occur:

`sudo opensnoop`

- Track all file opens by a process by name:

`sudo opensnoop -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>`"`

- Track all file opens by a process by PID:

`sudo opensnoop -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Track which processes open a specified file:

`sudo opensnoop -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
