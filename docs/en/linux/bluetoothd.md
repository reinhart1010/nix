---
layout: page
title: linux/bluetoothd (English)
description: "Daemon to manage bluetooth devices."
content_hash: 5b6016d2346451de61ab5d535c1a7364708f6f88
last_modified_at: 2024-01-31
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/linux/bluetoothd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bluetoothd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bluetoothd

Daemon to manage bluetooth devices.
More information: <https://manned.org/bluetoothd>.

- Start the daemon:

`bluetoothd`

- Start the daemon, logging to `stdout`:

`bluetoothd --nodetach`

- Start the daemon with a specific configuration file (defaults to `/etc/bluetooth/main.conf`):

`bluetoothd --configfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Start the daemon with verbose output to `stderr`:

`bluetoothd --debug`

- Start the daemon with verbose output coming from specific files in the bluetoothd or plugins source:

`bluetoothd --debug=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1:path/to/file2:...</span>
