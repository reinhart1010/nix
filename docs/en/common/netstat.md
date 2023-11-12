---
layout: page
title: common/netstat (English)
description: "Displays network-related information such as open connections, open socket ports, etc."
content_hash: 60028e5f42890a4f8e5af2601594563ba0d8b593
last_modified_at: 2023-11-12
related_topics:
  - title: 한국어 version
    url: /ko/common/netstat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/netstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# netstat

Displays network-related information such as open connections, open socket ports, etc.
More information: <https://man7.org/linux/man-pages/man8/netstat.8.html>.

- List all ports:

`netstat --all`

- List all listening ports:

`netstat --listening`

- List listening TCP ports:

`netstat --tcp`

- Display PID and program names:

`netstat --program`

- List information continuously:

`netstat --continuous`

- List routes and do not resolve IP addresses to hostnames:

`netstat --route --numeric`

- List listening TCP and UDP ports (+ user and process if you're root):

`netstat --listening --program --numeric --tcp --udp --extend`
