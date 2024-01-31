---
layout: page
title: osx/date (polski)
description: "Ustaw bądź wyświetl datę systemową."
content_hash: 60bb73a57acdbc3a8d1568493811774047c2108a
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/date.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/date.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/osx/date.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/date.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/date.html
    icon: bi bi-globe
tldri18n_status: 2
---
# date

Ustaw bądź wyświetl datę systemową.
Więcej informacji: <https://keith.github.io/xcode-man-pages/date.1.html>.

- Wyświetl aktualną datę w domyślnym formacie:

`date +%c`

- Wyświetl aktualną datę w formacie UTC i ISO 8601:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Wyświetl aktualną datę jako znacznik czasu Unix (sekundy od epoki systemu Unix):

`date +%s`

- Wyświetl określoną datę jako znacznik czasu Unix w domyślnym formacie:

`date -r 1473305798`
