---
layout: page
title: common/lprm (Nederlands)
description: "Annuleer wachtende printtaken van een server."
content_hash: 878553be20acf695a24b06011d0cdb06b396c3a6
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/lprm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/lprm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/lprm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># lprm

Annuleer wachtende printtaken van een server.
Bekijk ook: `lpq`.
Meer informatie: <https://www.cups.org/doc/man-lprm.html>.

- Annuleer de huidige taak op de standaard printer:

`lprm`

- Annuleer een taak van een specifieke server:

`lprm -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">server[:poort]</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">taak_id</span>

- Annuleer meerdere taken met een beveiligde verbinding naar de server:

`lprm -E `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">taak_id1 taak_id2 ...</span>

- Annuleer alle taken:

`lprm -`

- Annuleer de huidige taak van een specifieke printer of klasse:

`lprm -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestemming[/instantie]</span>
