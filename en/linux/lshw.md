---
layout: page
title: linux/lshw (English)
description: "List detailed information about hardware configurations as root user."
content_hash: 9fe508a6175651a3a3f38e9eef6e27add3db9db1
---
# lshw

List detailed information about hardware configurations as root user.
More information: <https://manned.org/lshw>.

- Launch the GUI:

`sudo lshw -X`

- List all hardware in tabular format:

`sudo lshw -short`

- List all disks and storage controllers in tabular format:

`sudo lshw -class disk -class storage -short`

- Save all network interfaces to an HTML file:

`sudo lshw -class network -html > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interfaces.html</span>
