---
layout: page
title: common/lpstat (English)
description: "Show status information about printers."
content_hash: aad4052088b7975caee7b024c27b18fc9f9891f1
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/lpstat.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/lpstat.html
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

- Show a list of print jobs queued by a specific user:

`lpstat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>
