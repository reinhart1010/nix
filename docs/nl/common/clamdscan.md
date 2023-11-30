---
layout: page
title: common/clamdscan (Nederlands)
description: "Een command-line virus scanner die gebruik maakt van de ClamAV Daemon."
content_hash: 77778edcd3cddb204885d38a0e626a82f3ef27b0
last_modified_at: 2023-11-30
related_topics:
  - title: English version
    url: /en/common/clamdscan.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/clamdscan.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/clamdscan.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/clamdscan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># clamdscan

Een command-line virus scanner die gebruik maakt van de ClamAV Daemon.
Meer informatie: <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>.

- Scan een bestand of map op kwetsbaarheden:

`clamdscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Scan data van `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | clamdscan -`

- Scan de huidige map en toon alleen geïnfecteerde bestanden:

`clamdscan --infected`

- Sla het scan rapport op in een log bestand:

`clamdscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/log_bestand</span>

- Verplaats geïnfecteerde bestanden naar een specifieke map:

`clamdscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/quarantaine_map</span>

- Verwijder geïnfecteerde bestanden:

`clamdscan --remove`

- Gebruik meerdere threads voor het scannen van een map:

`clamdscan --multiscan`

- Geef de bestandsdescriptor door in plaats van het bestand naar de daemon:

`clamdscan --fdpass`
