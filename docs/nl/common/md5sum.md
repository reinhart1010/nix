---
layout: page
title: common/md5sum (Nederlands)
description: "Bereken MD5 cryptografische checksums."
content_hash: 80e72280eb2ed78a193b373859eddd63335524f1
last_modified_at: 2024-12-09
related_topics:
  - title: English version
    url: /en/common/md5sum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/md5sum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/md5sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/md5sum.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/md5sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># md5sum

Bereken MD5 cryptografische checksums.
Meer informatie: <https://www.gnu.org/software/coreutils/md5sum>.

- Bereken de MD5 checksum voor één of meer bestanden:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Bereken en sla de lijst van MD5 checksums op in een bestand:

`md5sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.md5</span>

- Bereken een MD5 checksum van `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | md5sum`

- Lees een bestand met MD5 checksums en bestandsnamen en verifieer dat alle bestanden overeenkomende checksums hebben:

`md5sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.md5</span>

- Toon alleen een bericht voor ontbrekende bestanden of wanneer verificatie mislukt:

`md5sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.md5</span>

- Toon alleen een bericht wanneer verificatie mislukt, negeer ontbrekende bestanden:

`md5sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.md5</span>

- Controleer een bekende MD5 checksum van een bestand:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bekende_md5_checksum_van_het_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` | md5sum --check`
