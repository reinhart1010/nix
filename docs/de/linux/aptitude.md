---
layout: page
title: linux/aptitude (Deutsch)
description: "Debian und Ubuntu Paket Management Tool."
content_hash: b9206abb6c6672f8d18a9f015bb87aea178ca3ae
related_topics:
  - title: català version
    url: /ca/linux/aptitude.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/aptitude.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/aptitude.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/aptitude.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/aptitude.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/aptitude.html
    icon: bi bi-globe
---
# aptitude

Debian und Ubuntu Paket Management Tool.
Weitere Informationen: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Synchronisiere die Paketliste und verfügbaren Versionen. Dieser Command sollte zuerst ausgeführt werden bevor weitere aptitude Commands ausgeführt werden:

`aptitude update`

- Installiere ein neues Paket und seine Abhängigkeiten:

`aptitude install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Suche nach einem Paket:

`aptitude search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Suche nach einem installierten Paket (`?installed` ist ein aptitude Suchbegriff):

`aptitude search ?installed (`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>`)`

- Entferne ein Paket und alle Abhängigkeiten:

`aptitude remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Aktualisiere installierte Pakete auf die neusten Versionen:

`aptitude upgrade`

- Aktualisiere installierte Pakete (wie `aptitude upgrade`), inklusive obsoleter Pakete und installiere zusätzliche Pakete um die neuen Paket-Abhängigkeiten zu erfüllen:

`aptitude full-upgrade`

- Friere ein installiertes Paket ein und verhindere, dass es automatisch aktualisiert wird:

`aptitude hold '?installed(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>`)'`
