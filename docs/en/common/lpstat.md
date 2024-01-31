---
layout: page
title: common/lpstat (English)
description: "Show status information about printers."
content_hash: 2c9b61e682e9ec9e9fd23c0da2aeeaad3a790fc9
last_modified_at: 2024-01-31
related_topics:
  - title: Deutsch version
    url: /de/common/lpstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/lpstat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lpstat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lpstat

Show status information about printers.
More information: <https://manned.org/lpstat>.

- List printers present on the machine and whether they are enabled for printing:

`lpstat -p`

- Show the default printer:

`lpstat -d`

- Display all available status information:

`lpstat -t`

- List print jobs queued by a specific user:

`lpstat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>
