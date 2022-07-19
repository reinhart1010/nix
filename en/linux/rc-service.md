---
layout: page
title: linux/rc-service (English)
description: "Locate and run OpenRC services with arguments."
content_hash: b9a1b4a70ca838a616fd6531779530f8b0585163
---
# rc-service

Locate and run OpenRC services with arguments.
See also `openrc`.
More information: <https://manned.org/rc-service>.

- Show a service's status:

`rc-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` status`

- Start a service:

`sudo rc-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` start`

- Stop a service:

`sudo rc-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` stop`

- Restart a service:

`sudo rc-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` restart`

- Simulate running a service's custom command:

`sudo rc-service --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>

- Actually run a service's custom command:

`sudo rc-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_name</span>

- Resolve the location of a service definition on disk:

`sudo rc-service --resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>
