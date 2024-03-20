---
layout: page
title: common/sc_ttlexp (Deutsch)
description: "Ausgabe der Quelladressen von ICMP TTL expire-Nachrichten in `warts`-Dateien."
content_hash: 0a2532f2682a0850ced55c9b91b51af52bed71bb
last_modified_at: 2024-03-20
related_topics:
  - title: English version
    url: /en/common/sc_ttlexp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sc_ttlexp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sc_ttlexp

Ausgabe der Quelladressen von ICMP TTL expire-Nachrichten in `warts`-Dateien.
Weitere Informationen: <https://www.caida.org/catalog/software/scamper/>.

- Gib die Quelladressen von ICMP TTL expire-Nachrichten in einer `warts`-Datei nacheinander aus:

`sc_ttlexp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.warts path/to/file2.warts ...</span>
