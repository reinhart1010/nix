---
layout: page
title: osx/opensnoop (English)
description: "Tool that tracks file opens on your system."
content_hash: e165f1bd848b63b8196cb34c963f7762756dbee0
related_topics:
  - title: 中文 version
    url: /zh/osx/opensnoop.html
    icon: bi bi-globe
---
# opensnoop

Tool that tracks file opens on your system.
More information: <https://ss64.com/osx/opensnoop.html>.

- Print all file opens as they occur:

`sudo opensnoop`

- Track all file opens by a process by name:

`sudo opensnoop -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process_name</span>`"`

- Track all file opens by a process by PID:

`sudo opensnoop -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Track which processes open a specified file:

`sudo opensnoop -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
