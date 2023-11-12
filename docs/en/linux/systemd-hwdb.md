---
layout: page
title: linux/systemd-hwdb (English)
description: "Hardware database management tool."
content_hash: 26f1f7c1368ed2f7c4db49cc091cab842bec6073
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# systemd-hwdb

Hardware database management tool.
More information: <https://www.freedesktop.org/software/systemd/man/systemd-hwdb.html>.

- Update the binary hardware database in `/etc/udev`:

`systemd-hwdb update`

- Query the hardware database and print the result for a specific modalias:

`systemd-hwdb query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modalias</span>

- Update the binary hardware database, returning a non-zero exit value on any parsing error:

`systemd-hwdb --strict update`

- Update the binary hardware database in `/usr/lib/udev`:

`systemd-hwdb --usr update`

- Update the binary hardware database in the specified root path:

`systemd-hwdb --root=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/root</span>` update`
