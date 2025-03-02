---
layout: page
title: linux/groupadd (polski)
description: "Dodaje grupę użytkowników do systemu."
content_hash: 09f98de3537677a7b8058e9de4deaed44049be7c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/groupadd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/groupadd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/groupadd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# groupadd

Dodaje grupę użytkowników do systemu.
Zobacz także `groups`, `groupdel`, `groupmod`.
Więcej informacji: <https://manned.org/groupadd>.

- Utwórz nową grupę:

`sudo groupadd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_grupy</span>

- Utwórz nową grupę systemową:

`sudo groupadd --system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_grupy</span>

- Utwórz nową grupę z określonym `id_grupy`:

`sudo groupadd --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_grupy</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_grupy</span>
