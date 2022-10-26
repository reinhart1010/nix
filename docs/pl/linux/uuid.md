---
layout: page
title: linux/uuid (polski)
description: "Twórz i dekoduj uniwersalne identyfikatory (UUID)."
content_hash: 3851f37e916b30e578dc78879e616ca6784be27b
related_topics:
  - title: English version
    url: /en/linux/uuid.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># uuid

Twórz i dekoduj uniwersalne identyfikatory (UUID).
Zobacz też `uuidgen`.
Więcej informacji: <https://manned.org/uuid>.

- Stwórz UUIDv1 (oparte o zegar systemowy i - jeśli dostępne - adres sprzętowy):

`uuid`

- Stwórz UUIDv4 (losowy):

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- Stwórz wiele UUIDv4 na raz:

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ilość_uuid</span>

- Stwórz UUIDv4 w konkretnym formacie:

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">BIN|STR|SIV</span>

- Stwórz UUIDv4 i zapisz do pliku:

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>

- Stwórz UUIDv5 (oparty o podaną nazwę obiektu) w przestrzeni nazw:

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` ns:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DNS|URL|OID|X500</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_obiektu</span>

- Dekoduj podany UUID:

`uuid -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>
