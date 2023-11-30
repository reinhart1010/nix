---
layout: page
title: common/clamscan (Nederlands)
description: "Een command-line virus scanner."
content_hash: 40d7f2a568b58cedf5e7547e9de67e14216328ef
last_modified_at: 2023-11-30
related_topics:
  - title: English version
    url: /en/common/clamscan.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/clamscan.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/clamscan.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/clamscan.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/common/clamscan.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/clamscan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># clamscan

Een command-line virus scanner.
Meer informatie: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- Scan een bestand op kwetsbaarheden:

`clamscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Scan alle bestanden recursief in een specifieke map:

`clamscan -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Scan data van `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` | clamscan -`

- Specificeer een virus database bestand of map van bestanden:

`clamscan --database `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/database_bestand_of_map</span>

- Scan de huidige map en toon alleen geïnfecteerde bestanden:

`clamscan --infected`

- Sla het scan rapport op in een log bestand:

`clamscan --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/log_bestand</span>

- Verplaats geïnfecteerde bestanden naar een specifieke map:

`clamscan --move `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/quarantine_map</span>

- Verwijder geïnfecteerde bestanden:

`clamscan --remove yes`
