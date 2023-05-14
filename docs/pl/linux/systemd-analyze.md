---
layout: page
title: linux/systemd-analyze (polski)
description: "Analizuj i debuguj menedżera systemu."
content_hash: 0c82b41792c3b5cf5199ec3de1fa583c7c1bd83d
last_modified_at: 2023-05-14
related_topics:
  - title: English version
    url: /en/linux/systemd-analyze.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># systemd-analyze

Analizuj i debuguj menedżera systemu.
Wyświetl szczegóły dotyczące czasiu procesu uruchamiania jednostek (usług, punktów montowania, urządzeń, gniazd):
Więcej informacji: <https://www.freedesktop.org/software/systemd/man/systemd-analyze.html>.

- Wyświetl wszystkie uruchomione jednostki, uporządkowane według czasu ich inicjalizacji:

`systemd-analyze blame`

- Wyświetl drzewo krytycznego czasowo łańcucha jednostek:

`systemd-analyze critical-chain`

- Utwórz plik SVG pokazujący kiedy każda usługa wystartowała, zaznaczając czas wykorzystany na inicjalizację:

`systemd-analyze plot > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.svg</span>

- Sporządź wykres zależności i przekonwertuj go do pliku SVG:

`systemd-analyze dot | dot -T`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku.svg</span>

- Wyświetl wyniki bezpieczeństwa działających jednostek:

`systemd-analyze security`
