---
layout: page
title: linux/systemd-socket-activate (English)
description: "Socket activation for systemd services."
content_hash: 22ea5f52977824cc81dc1cc44d7a6417751083b7
last_modified_at: 2023-10-25
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systemd-socket-activate

Socket activation for systemd services.
More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-socket-activate.html>.

- Activate a service when a specific socket is connected:

`systemd-socket-activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/socket.service</span>

- Activate multiple sockets for a service:

`systemd-socket-activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/socket1.service</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/socket2.service</span>

- Pass environment variables to the service being activated:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SYSTEMD_SOCKET_ACTIVATION=1</span>` systemd-socket-activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/socket.service</span>

- Activate a service along with a notification socket:

`systemd-socket-activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/socket.socket</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/service.service</span>

- Activate a service with a specified port:

`systemd-socket-activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/socket.service</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>
