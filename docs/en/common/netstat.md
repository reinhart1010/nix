---
layout: page
title: common/netstat (English)
description: "Display network-related information such as open connections, open socket ports, etc."
content_hash: a7569e59328a8d04899c0c8ad11a53475c7c564b
last_modified_at: 2024-04-18
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

Display network-related information such as open connections, open socket ports, etc.
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
