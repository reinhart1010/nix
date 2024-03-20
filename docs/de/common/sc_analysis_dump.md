---
layout: page
title: common/sc_analysis_dump (Deutsch)
description: "Ausgabe von Traceroute-Pfaden in einem leicht zu parsenden Format."
content_hash: b2d4df362a0cb1d560654f041e646e0d8733536e
last_modified_at: 2024-03-20
related_topics:
  - title: English version
    url: /en/common/sc_analysis_dump.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sc_analysis_dump.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sc_analysis_dump

Ausgabe von Traceroute-Pfaden in einem leicht zu parsenden Format.
Weitere Informationen: <https://www.caida.org/catalog/software/scamper/>.

- Gib die traceroute in `warts`-Dateien nacheinander in einem leicht zu parsendem Format aus:

`sc_analysis_dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.warts path/to/file2.warts ...</span>
