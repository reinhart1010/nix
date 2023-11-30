---
layout: page
title: common/7za (Nederlands)
description: "Bestandsarchiver met een hoge compressieverhouding."
content_hash: e74dc565b64297f8178af8295171bcc7dc028dcc
last_modified_at: 2023-11-30
related_topics:
  - title: বাংলা version
    url: /bn/common/7za.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/7za.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/7za.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/7za.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/7za.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/7za.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/7za.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/7za.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/7za.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/7za.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/7za.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/7za.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/7za.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/7za.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/7za.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/7za.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># 7za

Bestandsarchiver met een hoge compressieverhouding.
Vergelijkbaar met `7z`, behalve dat het minder bestandstypes ondersteunt, maar platformonafhankelijk is.
Meer informatie: <https://manned.org/7za>.

- Archiveer een bestand of map:

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Versleutel een bestaand archief (inclusief bestandsnamen):

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/versleuteld.7z</span>` -p`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wachtwoord</span>` -mhe=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>

- Pak een archief uit met behoud van de originele map structuur:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>

- Pak een archief uit naar een specifieke map:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>` -o`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitkomst</span>

- Pak een archief uit naar `stdout`:

`7za x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>` -so`

- Archiveren met een specifiek archieftype:

`7za a -t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7z|bzip2|gzip|lzip|tar|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Geef een [l]ijst met de inhoud van het archiefbestand:

`7za l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>

- Zet het niveau van compressie (hoger betekent meer compressie, maar langzamer):

`7za a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/archief.7z</span>` -mx=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|3|5|7|9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>
