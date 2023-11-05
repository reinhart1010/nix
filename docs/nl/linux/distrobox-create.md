---
layout: page
title: linux/distrobox-create (Nederlands)
description: "Maak een distrobox container."
content_hash: 2b0265a3bce8e5578aa316a25f881adee81c9998
last_modified_at: 2023-11-05
related_topics:
  - title: English version
    url: /en/linux/distrobox-create.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/distrobox-create.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/distrobox-create.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># distrobox-create

Maak een distrobox container.
Subcommando van `distrobox`. Bekijk ook: `tldr distrobox`.
De gecreëerde container wordt nauw geïntegreerd met de host, waardoor het delen van de thuismap van de gebruiker, externe opslag, externe USB-apparaten, grafische apps (X11/Wayland) en audio mogelijk is.
Meer informatie: <https://distrobox.privatedns.org/usage/distrobox-create.html>.

- Maak een distrobox container met behulp van het Ubuntu image:

`distrobox-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubuntu:latest</span>

- Kloon een distrobox container:

`distrobox-create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cloned_container_name</span>
