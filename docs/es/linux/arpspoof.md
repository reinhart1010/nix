---
layout: page
title: linux/arpspoof (español)
description: "Forja respuestas ARP para interceptar paquetes."
content_hash: 32ea26ef154f8cfce1e7fb2965d662e46f6b6d57
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/arpspoof.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/arpspoof.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arpspoof

Forja respuestas ARP para interceptar paquetes.
Más información: <https://monkey.org/~dugsong/dsniff>.

- Envenena todos los hosts para interceptar paquetes en la [i]nterfaz para el host:

`sudo arpspoof -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_del_host</span>

- Envenena el objetivo para interceptar paquetes en la [i]nterfaz para el host:

`sudo arpspoof -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_del_objetivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_del_host</span>

- Envenena tanto el objetivo como el host para interceptar paquetes en la [i]nterfaz para el host:

`sudo arpspoof -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` -r -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_del_objetivo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_del_host</span>
