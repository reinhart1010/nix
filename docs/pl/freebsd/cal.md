---
layout: page
title: freebsd/cal (polski)
description: "Wyświetl kalendarz z wyróżnionym bieżącym dniem."
content_hash: fd3f1144929769cdff9e365d854412615a67cff0
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/freebsd/cal.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/freebsd/cal.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/freebsd/cal.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/freebsd/cal.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/cal.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/freebsd/cal.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cal

Wyświetl kalendarz z wyróżnionym bieżącym dniem.
Więcej informacji: <https://man.freebsd.org/cgi/man.cgi?cal>.

- Wyświetl kalendarz dla obecnego miesiąca:

`cal`

- Wyświetl kalendarz dla określonego roku:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rok</span>

- Wyświetl kalendarz dla określonego miesiąca i roku:

`cal `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">miesiąc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rok</span>

- Wyświetl cały kalendarz na bieżący rok (z ang. [y]ear):

`cal -y`

- Nie wyróżniaj (z ang. [h]ighlight) dzisiejszej daty i wyświetl [3] miesiące ją obejmujące:

`cal -h -3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">miesiąc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rok</span>

- Wyświetl 2 miesiące przed (z ang. [B]efore) i 3 po (z ang. [A]fter) określonym [m]iesiącu bieżącego roku:

`cal -A 3 -B 2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">miesiąc</span>

- Wyświetl dni [j]uliańskie (zaczynając od jeden, numerowane od 1 stycznia):

`cal -j`
