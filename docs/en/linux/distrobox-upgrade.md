---
layout: page
title: linux/distrobox-upgrade (English)
description: "Upgrade one or multiple distrobox containers."
content_hash: 9705036c3af57b8f8f058644bf81bcda7a3871a4
last_modified_at: 2023-11-20
related_topics:
  - title: Nederlands version
    url: /nl/linux/distrobox-upgrade.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-upgrade

Upgrade one or multiple distrobox containers.
Subcommand of `distrobox`. See also: `tldr distrobox`.
More information: <https://distrobox.it/usage/distrobox-upgrade>.

- Upgrade a container using the container's native package manager:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Upgrade all containers using the container's native package managers:

`distrobox-upgrade --all`

- Upgrade specific containers via the container's native package manager:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>
