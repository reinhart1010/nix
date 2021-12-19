---
layout: page
title: common/cut (Deutsch)
description: "Schneide Felder von stdin oder einer Datei aus."
content_hash: 2f5063c9f0ef3482155add7ebd62685afb1c1108
related_topics:
  - title: English version
    url: /en/common/cut.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cut.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cut.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cut.html
    icon: bi bi-globe
---
# cut

Schneide Felder von stdin oder einer Datei aus.
Weitere Informationen: <https://www.gnu.org/software/coreutils/cut>.

- Schneide die ersten 16 Zeichen jeder Zeile von stdin aus:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-16</span>

- Schneide die ersten 16 Zeichen jeder Zeile der angegebenen Datei aus:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-16</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Schneide alles ab dem dritten Zeichen bis zum Ende der Zeile aus:

`cut -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3-</span>

- Schneide das fünfte Feld jeder Zeile aus und nutze den Doppelpunkt als Trennzeichen (standardmäßig Tab):

`cut -d'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>`' -f`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Schneide das 2. und 10. Feld jeder Zeile aus und nutze Semikolon als Trennzeichen:

`cut -d'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">;</span>`' -f`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,10</span>

- Schneide alles ab dem dritten Zeichen bis zum Ende der Zeile aus und nutze Leerzeichen als Trennzeichen:

`cut -d'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"> </span>`' -f`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3-</span>
