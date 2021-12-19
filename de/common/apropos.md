---
layout: page
title: common/apropos (Deutsch)
description: "Durchsuche die Handbuchseiten nach Namen und Beschreibungen."
content_hash: 557a8c26fe9773095b7f7b610fe89bc3305cf443
related_topics:
  - title: English version
    url: /en/common/apropos.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/apropos.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/apropos.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apropos.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/apropos.html
    icon: bi bi-globe
---
# apropos

Durchsuche die Handbuchseiten nach Namen und Beschreibungen.
Weitere Informationen: <https://manned.org/apropos>.

- Suche nach einem Schlüsselwort mit einem regulären Ausdruck:

`apropos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regulären_ausdruck</span>

- Suche ohne Beschränkung der Ausgabe auf die Terminal Breite:

`apropos -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regulären_ausdruck</span>

- Suche nach Seiten, die alle angegebenen Ausdrücke enthalten:

`apropos `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regulären_ausdruck_1</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regulären_ausdruck_2</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regulären_ausdruck_3</span>
