---
layout: page
title: osx/date (polski)
description: "Ustaw bądź wyświetl datę systemową."
content_hash: d2e7baa5aa2a92ce56e9b00827d6916f563dba0c
related_topics:
  - title: English version
    url: /en/osx/date.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/date.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/date.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># date

Ustaw bądź wyświetl datę systemową.
Więcej informacji: <https://ss64.com/osx/date.html>.

- Wyświetl aktualną datę w domyślnym formacie:

`date +%c`

- Wyświetl aktualną datę w formacie UTC i ISO 8601:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Wyświetl aktualną datę jako znacznik czasu Unix (sekundy od epoki systemu Unix):

`date +%s`

- Wyświetl określoną datę jako znacznik czasu Unix w domyślnym formacie:

`date -r 1473305798`
