---
layout: page
title: linux/distrobox-enter (Nederlands)
description: "Betreed een Distrobox container. Bekijk ook: `tldr distrobox`."
content_hash: e4269fced822bdd23301869de66b76f6146bbe8f
last_modified_at: 2023-11-26
related_topics:
  - title: English version
    url: /en/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-enter.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/distrobox-enter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# distrobox-enter

Betreed een Distrobox container. Bekijk ook: `tldr distrobox`.
Standaard commando dat wordt uitgevoerd is je SHELL, maar je kan verschillende shells of hele commando's specificeren. Indien gebruikt in een script/applicatie/service, kunt u de `--headless`-modus gebruiken om de tty en interactiviteit uit te schakelen.
Meer informatie: <https://distrobox.it/usage/distrobox-enter>.

- Betreed een Distrobox container:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Betreed een Distrobox container en voer een commando uit bij het inloggen:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh -l</span>

- Betreed een Distrobox container zonder een tty the instanteren:

`distrobox-enter --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uptime -p</span>
