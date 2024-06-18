---
layout: page
title: common/ls (Nederlands)
description: "Toon de inhoud van een map."
content_hash: 32b3f5530a8bccf26aa1df6577bd9980b7ecc06b
last_modified_at: 2024-06-18
related_topics:
  - title: català version
    url: /ca/common/ls.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/ls.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ls.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ls.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ls.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ls.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ls.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ls.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ls.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ls.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ls.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/ls.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/ls.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ls.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ls.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ls.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/ls.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ls.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ls.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ls.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ls

Toon de inhoud van een map.
Meer informatie: <https://www.gnu.org/software/coreutils/ls>.

- Toon één bestand per regel:

`ls -1`

- Toon alle bestanden, inclusief verborgen bestanden:

`ls -a`

- Toon alle bestanden, met een `/` achter de namen van mappen:

`ls -F`

- Lange lijstweergave (permissies, eigendom, grootte en wijzigingsdatum) van alle bestanden:

`ls -la`

- Lange lijstweergave met grootte weergegeven in leesbare eenheden (KiB, MiB, GiB):

`ls -lh`

- Lange lijstweergave gesorteerd op grootte (aflopend) recursief:

`ls -lSR`

- Lange lijstweergave van alle bestanden, gesorteerd op wijzigingsdatum (oudste eerst):

`ls -ltr`

- Toon alleen mappen:

`ls -d */`
