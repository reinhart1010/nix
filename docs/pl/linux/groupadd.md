---
layout: page
title: linux/groupadd (polski)
description: "Dodaje grupę użytkowników do systemu."
content_hash: 954cf0ae80a02a26357c7d6f25b6afff0fc18272
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/groupadd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# groupadd

Dodaje grupę użytkowników do systemu.
Zobacz też `groups`, `groupdel`, `groupmod`.
Więcej informacji: <https://manned.org/groupadd>.

- Utwórz nową grupę:

`sudo groupadd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_grupy</span>

- Utwórz nową grupę systemową:

`sudo groupadd --system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_grupy</span>

- Utwórz nową grupę z określonym `id_grupy`:

`sudo groupadd --gid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_grupy</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_grupy</span>
