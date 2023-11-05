---
layout: page
title: linux/distrobox-upgrade (Nederlands)
description: "Upgrade een of meerdere distrobox containers."
content_hash: b7ceb63cbf5d283672548b16205e664a690f5cc5
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/linux/distrobox-upgrade.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-upgrade.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># distrobox-upgrade

Upgrade een of meerdere distrobox containers.
Subcommando van `distrobox`. Bekijk ook: `tldr distrobox`.
Meer informatie: <https://distrobox.privatedns.org/usage/distrobox-upgrade.html>.

- Upgrade een container met behulp van de native pakketbeheerder van de container:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Upgrade alle containers met behulp van de native pakketbeheerder van de container:

`distrobox-upgrade --all`

- Upgrade specifieke containers met behulp van de native pakketbeheerder van de container:

`distrobox-upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container1 container2 ...</span>
