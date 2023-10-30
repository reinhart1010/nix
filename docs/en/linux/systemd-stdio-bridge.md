---
layout: page
title: linux/systemd-stdio-bridge (English)
description: "Implement a proxy between `stdin`/`stdout` and a D-Bus."
content_hash: a80eea5ae4bb75ce0c284f0a32003c4b612235ad
last_modified_at: 2023-10-30
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systemd-stdio-bridge

Implement a proxy between `stdin`/`stdout` and a D-Bus.
Note: It expects to receive an open connection via `stdin`/`stdout` when started, and will create a new connection to the specified bus.
More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-stdio-bridge.html>.

- Forward `stdin`/`stdout` to the local system bus:

`systemd-stdio-bridge`

- Forward `stdin`/`stdout` to a specific user's D-Bus:

`systemd-stdio-bridge --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>

- Forward `stdin`/`stdout` to the local system bus within a specific container:

`systemd-stdio-bridge --machine=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mycontainer</span>

- Forward `stdin`/`stdout` to a custom D-Bus address:

`systemd-stdio-bridge --bus-path=unix:path=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/custom/dbus/socket</span>
