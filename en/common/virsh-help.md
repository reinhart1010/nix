---
layout: page
title: common/virsh-help (English)
description: "Display information about `virsh` commands or command groups."
content_hash: e53ec9005ca0d318165e31cf535fb1a84cee0f3b
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

- Show help for a command:

`virsh help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>
