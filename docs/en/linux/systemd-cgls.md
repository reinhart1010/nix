---
layout: page
title: linux/systemd-cgls (English)
description: "Show the contents of the selected Linux control group hierarchy in a tree."
content_hash: 96566f3b6eb82ca10195597a1c59c72ad1e0cd57
last_modified_at: 2023-10-13
---
# systemd-cgls

Show the contents of the selected Linux control group hierarchy in a tree.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-cgls.html>.

- Display the whole control group hierarchy on your system:

`systemd-cgls`

- Display a control group tree of a specific resource controller:

`systemd-cgls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cpu|memory|io</span>

- Display the control group hierarchy of one or more systemd units:

`systemd-cgls --unit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unit1 unit2 ...</span>
