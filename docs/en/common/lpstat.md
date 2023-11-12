---
layout: page
title: common/lpstat (English)
description: "Show status information about printers."
content_hash: 56db9e779160cd9c270d2baa9204a6478a8dfa5b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/lpstat.html
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

- Show a list of print jobs queued by the specified user:

`lpstat -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>
