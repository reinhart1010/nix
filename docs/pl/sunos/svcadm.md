---
layout: page
title: sunos/svcadm (polski)
description: "Manipuluj instancjami usług."
content_hash: 6e36eb42e38c1b707a9809cb8cfa5c4739f51139
last_modified_at: 2024-05-10
related_topics:
  - title: English version
    url: /en/sunos/svcadm.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/svcadm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/svcadm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/svcadm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/svcadm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/svcadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# svcadm

Manipuluj instancjami usług.
Więcej informacji: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Włącz usługę w bazie danych usług:

`svcadm enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_usługi</span>

- Wyłącz usługę:

`svcadm disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_usługi</span>

- Ponownie uruchom aktywną usługę:

`svcadm restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_usługi</span>

- Ponownie odczytaj pliki konfiguracyjne:

`svcadm refresh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_usługi</span>

- Usuń usługę ze stanu konserwacji i ją uruchom:

`svcadm clear `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nazwa_usługi</span>
