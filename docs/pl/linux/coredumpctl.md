---
layout: page
title: linux/coredumpctl (polski)
description: "Pobieraj i przetwarzaj zapisane zrzuty pamięci i metadane."
content_hash: 56dd5de6c28816ba1ec8a08e480a1ec3bca23e84
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/coredumpctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/coredumpctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/coredumpctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# coredumpctl

Pobieraj i przetwarzaj zapisane zrzuty pamięci i metadane.
Więcej informacji: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- Wyświetl wszystkie zapisane zrzuty pamięci:

`coredumpctl list`

- Wyświetl zapisane zrzuty pamięci podanego programu:

`coredumpctl list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Wyświetl informacje o zrzutach pamięci programu o podanym PID:

`coredumpctl info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Wywołaj debugger używając ostatniego zrzutu pamięci programu:

`coredumpctl debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>

- Wyodrębnij ostatni zrzut pamięci programu do pliku:

`coredumpctl --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ścieżka/do/pliku</span>` dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">program</span>
