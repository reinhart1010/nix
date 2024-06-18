---
layout: page
title: common/netstat (English)
description: "Display network-related information such as open connections, open socket ports, etc."
content_hash: ff7964a28c6c01d04610c2efb56a356c92d01871
last_modified_at: 2024-06-18
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
More information: <https://manned.org/netstat>.

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
