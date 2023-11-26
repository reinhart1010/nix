---
layout: page
title: linux/distrobox-create (Nederlands)
description: "Maak een Distrobox container. Bekijk ook: `tldr distrobox`."
content_hash: 25127f204ecdd1977ca605c2170029bd4c52a789
last_modified_at: 2023-11-26
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
tldri18n_status: 2
---
# distrobox-create

Maak een Distrobox container. Bekijk ook: `tldr distrobox`.
De gecreëerde container wordt nauw geïntegreerd met de host, waardoor het delen van de thuismap van de gebruiker, externe opslag, externe USB-apparaten, grafische apps (X11/Wayland) en audio mogelijk is.
Meer informatie: <https://distrobox.it/usage/distrobox-create>.

- Maak een Distrobox container met behulp van het Ubuntu image:

`distrobox-create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ubuntu:latest</span>

- Kloon een Distrobox container:

`distrobox-create --clone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cloned_container_name</span>
