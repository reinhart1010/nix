---
layout: page
title: openbsd/cal (polski)
description: "Wyświetl kalendarz z wyróżnionym bieżącym dniem."
content_hash: f126e9dff5df95b800aeca831f27179583809b50
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/openbsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

Wyświetl kalendarz z wyróżnionym bieżącym dniem.
Więcej informacji: <https://man.openbsd.org/cal>.

- Wyświetl kalendarz dla obecnego miesiąca:

`cal`

- Wyświetl kalendarz dla określonego roku:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rok</span>

- Wyświetl kalendarz dla określonego miesiąca i roku:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">miesiąc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rok</span>

- Wyświetl kalendarz dla obecnego roku (z ang. [y]ear):

`cal -y`

- Wyświetl dni [j]uliańskie (zaczynając od jeden, numerowane od 1 stycznia):

`cal -j`

- Użyj poniedziałku (z ang. [m]onday) jako początku tygodnia zamiast niedzieli:

`cal -m`

- Wyświetl numery tygodni (z ang. [w]eek) (niezgodne z `-j`):

`cal -w`
