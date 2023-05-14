---
layout: page
title: linux/timedatectl (polski)
description: "Kontroluj datę i czas systemowy."
content_hash: 0572c6052d5c751d8446160ba24f480d6ec516d8
last_modified_at: 2023-05-14
related_topics:
  - title: English version
    url: /en/linux/timedatectl.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># timedatectl

Kontroluj datę i czas systemowy.
Więcej informacji: <https://manned.org/timedatectl>.

- Sprawdź aktualny czas zegara systemowego:

`timedatectl`

- Bezpośrednio ustaw czas lokalny zegara systemowego:

`timedatectl set-time "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yyyy-MM-dd hh:mm:ss</span>`"`

- Wyświetl dostępne strefy czasowe:

`timedatectl list-timezones`

- Ustaw systemową strefę czasową:

`timedatectl set-timezone `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">strefa_czasowa</span>

- Włącz synchronizację czasu poprzez Network Time Protocol (NTP):

`timedatectl set-ntp on`

- Zmień standard czasu zegara sprzętowego na czas lokalny:

`timedatectl set-local-rtc 1`
