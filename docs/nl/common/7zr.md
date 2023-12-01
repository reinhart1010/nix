---
layout: page
title: common/7zr (Nederlands)
description: "Bestandsarchiver met een hoge compressieverhouding."
content_hash: 5128ac94dc64693d0705345467b54d44de74446d
last_modified_at: 2023-12-01
related_topics:
  - title: বাংলা version
    url: /bn/common/7zr.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/7zr.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7zr.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/7zr.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/7zr.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7zr.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7zr.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7zr.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7zr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7zr.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7zr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7zr.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/7zr.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7zr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7zr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# 7zr

Bestandsarchiver met een hoge compressieverhouding.
Vergelijkbaar met `7z`, behalve dat het alleen `.7z`-bestanden ondersteunt.
Meer informatie: <https://manned.org/7zr>.

- Archiveer een bestand of map:

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Versleutel een bestaand archief (inclusief bestandsnamen):

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/versleuteld.7z</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wachtwoord</span>` -mhe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>

- Pak een archief uit met behoud van de originele map structuur:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>

- Pak een archief uit naar een specifieke map:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>` -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitkomst</span>

- Pak een archief uit naar `stdout`:

`7zr x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>` -so`

- Geef een [l]ijst met de inhoud van het archiefbestand:

`7zr l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>

- Zet het niveau van compressie (hoger betekent meer compressie, maar langzamer):

`7zr a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>` -mx=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|3|5|7|9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>
