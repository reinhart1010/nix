---
layout: page
title: linux/clamav (English)
description: "Open-source anti-virus program."
content_hash: 317402cd00385f9b6b77a3e7c31f5e5e62b56058
related_topics:
  - title: español version
    url: /es/linux/clamav.html
    icon: bi bi-globe
---
# clamav

Open-source anti-virus program.
Designed especially for e-mail scanning on mail gateways, but can be used in other contexts.
More information: <https://www.clamav.net>.

- Update virus definitions:

`freshclam`

- Scan a file for viruses:

`clamscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Scan directories recursively and print out infected files:

`clamscan --recursive --infected `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Scan directories recursively and move them into quarantine:

`clamscan --recursive --move=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>
