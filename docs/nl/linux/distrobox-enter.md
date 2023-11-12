---
layout: page
title: linux/distrobox-enter (Nederlands)
description: "Betreed een distrobox container."
content_hash: c17ece8ab58d908d1cfcf230858e2a01397d9f79
last_modified_at: 2023-11-12
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

Betreed een distrobox container.
Subcommando van `distrobox`. Bekijk ook: `tldr distrobox`.
Standaard commando dat wordt uitgevoerd is je SHELL, maar je kan verschillende shells of hele commando's specificeren. Indien gebruikt in een script/applicatie/service, kunt u de `--headless`-modus gebruiken om de tty en interactiviteit uit te schakelen.
Meer informatie: <https://distrobox.privatedns.org/usage/distrobox-enter.html>.

- Betreed een distrobox container:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Betreed een distrobox container en voer een commando uit bij het inloggen:

`distrobox-enter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh -l</span>

- Betreed een distrobox container zonder een tty the instanteren:

`distrobox-enter --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uptime -p</span>
