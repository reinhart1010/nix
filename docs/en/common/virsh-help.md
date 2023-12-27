---
layout: page
title: common/virsh-help (English)
description: "Display information about `virsh` commands or command groups."
content_hash: f45141802769a01b853f38874ea7c69d85d85e25
last_modified_at: 2023-12-27
related_topics:
  - title: 한국어 version
    url: /ko/common/virsh-help.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/virsh-help.html
    icon: bi bi-globe
tldri18n_status: 2
---
# virsh-help

Display information about `virsh` commands or command groups.
See also: `virsh`.
More information: <https://manned.org/virsh>.

- List the `virsh` commands grouped into related categories:

`virsh help`

- List the command categories:

`virsh help | grep "keyword"`

- List the commands in a category:

`virsh help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">category_keyword</span>

- Display help for a command:

`virsh help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
