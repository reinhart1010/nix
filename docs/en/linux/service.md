---
layout: page
title: linux/service (English)
description: "Manage services by running init scripts."
content_hash: af2c3bac0350aedfc11e1fedd13bfbb951718c99
related_topics:
  - title: català version
    url: /ca/linux/service.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/service.html
    icon: bi bi-globe
---
# service

Manage services by running init scripts.
The full script path should be omitted (`/etc/init.d/` is assumed).
More information: <https://manned.org/service>.

- List the name and status of all services:

`service --status-all`

- Start/Stop/Restart/Reload service (start/stop should always be available):

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|restart|reload</span>

- Do a full restart (runs script twice with start and stop):

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` --full-restart`

- Show the current status of a service:

`service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` status`
