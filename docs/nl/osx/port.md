---
layout: page
title: osx/port (Nederlands)
description: "Pakketbeheerder voor macOS."
content_hash: b0bb9a3129b3203394255cfe55a572c79bfb6c49
last_modified_at: 2024-06-20
related_topics:
  - title: English version
    url: /en/osx/port.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/port.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/port.html
    icon: bi bi-globe
tldri18n_status: 2
---
# port

Pakketbeheerder voor macOS.
Meer informatie: <https://www.macports.org>.

- Zoek naar een pakket:

`port search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekterm</span>

- Installeer een pakket:

`sudo port install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Lijst geïnstalleerde pakketten:

`port installed`

- Update port en haal de nieuwste lijst met beschikbare pakketten op:

`sudo port selfupdate`

- Upgrade verouderde pakketten:

`sudo port upgrade outdated`

- Verwijder oude versies van geïnstalleerde pakketten:

`sudo port uninstall inactive`
