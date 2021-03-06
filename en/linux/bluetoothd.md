---
layout: page
title: linux/bluetoothd (English)
description: "Daemon to manage bluetooth devices."
content_hash: 6935788dc873bf42de6a992ef40f5802b847091f
related_topics:
  - title: 中文 version
    url: /zh/linux/bluetoothd.html
    icon: bi bi-globe
---
# bluetoothd

Daemon to manage bluetooth devices.
More information: <https://manned.org/bluetoothd>.

- Start the daemon:

`bluetoothd`

- Start the daemon, logging to stdout:

`bluetoothd --nodetach`

- Start the daemon with a specific configuration file (defaults to `/etc/bluetooth/main.conf`):

`bluetoothd --configfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Start the daemon with verbose output to stderr:

`bluetoothd --debug`

- Start the daemon with verbose output coming from specific files in the bluetoothd or plugins source:

`bluetoothd --debug=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file3</span>
