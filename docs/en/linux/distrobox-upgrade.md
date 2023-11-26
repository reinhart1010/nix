---
layout: page
title: linux/distrobox-upgrade (English)
description: "Upgrade one or multiple Distrobox containers. See also: `tldr distrobox`."
content_hash: 14f11248239b704475d9a783da58bcc7bb535faf
last_modified_at: 2023-11-26
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

Upgrade one or multiple Distrobox containers. See also: `tldr distrobox`.
More information: <https://distrobox.it/usage/distrobox-upgrade>.

- Upgrade a container using the container's native package manager:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Upgrade all containers using the container's native package managers:

`distrobox-upgrade --all`

- Upgrade specific containers via the container's native package manager:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>
