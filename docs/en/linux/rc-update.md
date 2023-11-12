---
layout: page
title: linux/rc-update (English)
description: "Add and remove OpenRC services to and from runlevels."
content_hash: c530ba1901e49824d1446517e7397be2c3784658
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# rc-update

Add and remove OpenRC services to and from runlevels.
See also `openrc`.
More information: <https://manned.org/rc-update>.

- List all services and the runlevels they are added to:

`rc-update show`

- Add a service to a runlevel:

`sudo rc-update add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runlevel</span>

- Delete a service from a runlevel:

`sudo rc-update delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">runlevel</span>

- Delete a service from all runlevels:

`sudo rc-update --all delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service_name</span>
